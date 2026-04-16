"""
Lab 11 — Helper Utilities
"""
import re
from openai import OpenAI
from core.config import OPENAI_MODEL, MAX_TOKENS


def chat_with_openai(system_prompt: str, user_message: str) -> str:
    """Send a message to OpenAI and get the response.

    Args:
        system_prompt: System instruction for the model
        user_message: User's message

    Returns:
        The model's response text
    """
    client = OpenAI()
    
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    
    return response.choices[0].message.content


# For backward compatibility with existing code
async def chat_with_agent(agent, runner, user_message: str, session_id=None):
    """Wrapper for backward compatibility (now uses OpenAI instead of ADK)."""
    # In simple implementation, agent contains system_prompt
    system_prompt = getattr(agent, 'instruction', '')
    response = chat_with_openai(system_prompt, user_message)
    
    # Return tuple for compatibility
    class MockSession:
        id = session_id or "session_1"
    
    return response, MockSession()
