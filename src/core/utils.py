"""
Lab 11 — Helper Utilities
"""
import re
import asyncio

from google.genai import types


async def chat_with_agent(agent, runner, user_message: str, session_id=None):
    """Send a message to the agent and get the response.

    Args:
        agent: The LlmAgent instance
        runner: The InMemoryRunner instance
        user_message: Plain text message to send
        session_id: Optional session ID to continue a conversation

    Returns:
        Tuple of (response_text, session)
    """
    user_id = "student"
    app_name = runner.app_name

    session = None
    if session_id is not None:
        try:
            session = await runner.session_service.get_session(
                app_name=app_name, user_id=user_id, session_id=session_id
            )
        except (ValueError, KeyError):
            pass

    if session is None:
        try:
            session = await runner.session_service.create_session(
                app_name=app_name, user_id=user_id
            )
        except Exception:
            session = await runner.session_service.create_session(
                app_name=app_name, user_id=user_id
            )

    content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_message)],
    )

    final_response = ""
    max_attempts = 4
    for attempt in range(1, max_attempts + 1):
        try:
            final_response = ""
            async for event in runner.run_async(
                user_id=user_id, session_id=session.id, new_message=content
            ):
                if hasattr(event, "content") and event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, "text") and part.text:
                            final_response += part.text
            break
        except Exception as e:
            error_text = str(e)
            is_quota_error = "RESOURCE_EXHAUSTED" in error_text or "429" in error_text
            if not is_quota_error or attempt == max_attempts:
                raise

            retry_seconds = 12
            match = re.search(r"retry in\s+(\d+)(?:\.\d+)?s", error_text, re.IGNORECASE)
            if match:
                retry_seconds = max(retry_seconds, int(match.group(1)) + 1)

            await asyncio.sleep(retry_seconds)

    return final_response, session
