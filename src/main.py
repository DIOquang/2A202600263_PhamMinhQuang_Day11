"""
Lab 11 — Main Entry Point
Run the full lab flow: attack -> defend -> test -> HITL design

Usage:
    python main.py              # Run all parts
    python main.py --part 1     # Run only Part 1 (attacks)
    python main.py --part 2     # Run only Part 2 (guardrails)
    python main.py --part 3     # Run only Part 3 (testing pipeline)
    python main.py --part 4     # Run only Part 4 (HITL design)
"""
import sys
import asyncio
import argparse

from core.config import setup_api_key


async def part1_attacks(economy_mode=False):
    """Part 1: Attack an unprotected agent."""
    print("\n" + "=" * 60)
    print("PART 1: Attack Unprotected Agent")
    print("=" * 60)

    if economy_mode:
        from attacks.attacks import adversarial_prompts
        print("Economy mode enabled: skipping live LLM attack execution.")
        print("Loaded manual adversarial prompts:")
        for item in adversarial_prompts:
            print(f"  - #{item['id']} {item['category']}")
        print("Skipping AI-generated attack prompts in economy mode.")
        return []

    from agents.agent import create_unsafe_agent, test_agent
    from attacks.attacks import run_attacks, generate_ai_attacks

    # Create and test the unsafe agent
    agent, runner = create_unsafe_agent()
    await test_agent(agent, runner)

    # TODO 1: Run manual adversarial prompts
    print("\n--- Running manual attacks (TODO 1) ---")
    results = await run_attacks(agent, runner)

    # TODO 2: Generate AI attack test cases
    print("\n--- Generating AI attacks (TODO 2) ---")
    ai_attacks = await generate_ai_attacks()

    return results


async def part2_guardrails(economy_mode=False):
    """Part 2: Implement and test guardrails."""
    print("\n" + "=" * 60)
    print("PART 2: Guardrails")
    print("=" * 60)

    # Part 2A: Input guardrails
    print("\n--- Part 2A: Input Guardrails ---")
    from guardrails.input_guardrails import (
        test_injection_detection,
        test_topic_filter,
        test_input_plugin,
    )
    test_injection_detection()
    print()
    test_topic_filter()
    print()
    await test_input_plugin()

    # Part 2B: Output guardrails
    print("\n--- Part 2B: Output Guardrails ---")
    from guardrails.output_guardrails import test_content_filter, _init_judge
    if not economy_mode:
        _init_judge()  # Initialize LLM judge if TODO 7 is done
    else:
        print("Economy mode enabled: skipping judge initialization.")
    test_content_filter()

    # Part 2C: NeMo Guardrails
    print("\n--- Part 2C: NeMo Guardrails ---")
    if economy_mode:
        print("Economy mode enabled: skipping NeMo live LLM tests.")
    else:
        try:
            from guardrails.nemo_guardrails import init_nemo, test_nemo_guardrails
            init_nemo()
            await test_nemo_guardrails()
        except ImportError:
            print("NeMo Guardrails not available. Skipping Part 2C.")
        except Exception as e:
            print(f"NeMo error: {e}. Skipping Part 2C.")


async def part3_testing(economy_mode=False):
    """Part 3: Before/after comparison + security pipeline."""
    print("\n" + "=" * 60)
    print("PART 3: Security Testing Pipeline")
    print("=" * 60)

    from testing.testing import run_comparison, print_comparison, SecurityTestPipeline
    from agents.agent import create_unsafe_agent, create_protected_agent

    # TODO 10: Before vs after comparison
    if economy_mode:
        print("\n--- TODO 10: Before/After Comparison (economy simulation) ---")
        print("Economy mode enabled: skipping live before/after LLM comparison.")
    else:
        print("\n--- TODO 10: Before/After Comparison ---")
        unprotected, protected = await run_comparison()
        if unprotected and protected:
            print_comparison(unprotected, protected)
        else:
            print("Complete TODO 10 to see the comparison.")

    # TODO 11: Automated security pipeline
    if economy_mode:
        print("\n--- TODO 11: Security Test Pipeline (economy simulation) ---")
        print("Economy mode enabled: skipping unsafe-agent live pipeline run.")
    else:
        print("\n--- TODO 11: Security Test Pipeline ---")
        agent, runner = create_unsafe_agent()
        pipeline = SecurityTestPipeline(agent, runner)
        results = await pipeline.run_all()
        if results:
            pipeline.print_report(results)
        else:
            print("Complete TODO 11 to see the pipeline report.")

    # Assignment 11: production defense-in-depth pipeline
    print("\n--- Assignment 11: Defense-in-Depth Pipeline ---")
    try:
        from testing.defense_pipeline import run_assignment_demo
        from guardrails.input_guardrails import InputGuardrailPlugin
        from guardrails.output_guardrails import OutputGuardrailPlugin

        if economy_mode:
            await run_assignment_demo(agent=None, runner=None, use_llm_judge=False)
        else:
            input_plugin = InputGuardrailPlugin()
            output_plugin = OutputGuardrailPlugin(use_llm_judge=False)
            protected_agent, protected_runner = create_protected_agent(
                plugins=[input_plugin, output_plugin]
            )
            await run_assignment_demo(agent=protected_agent, runner=protected_runner)
    except Exception as e:
        print(f"Could not run assignment pipeline demo automatically: {e}")


def part4_hitl():
    """Part 4: HITL design."""
    print("\n" + "=" * 60)
    print("PART 4: Human-in-the-Loop Design")
    print("=" * 60)

    from hitl.hitl import test_confidence_router, test_hitl_points

    # TODO 12: Confidence Router
    print("\n--- TODO 12: Confidence Router ---")
    test_confidence_router()

    # TODO 13: HITL Decision Points
    print("\n--- TODO 13: HITL Decision Points ---")
    test_hitl_points()


async def main(parts=None, economy_mode=False):
    """Run the full lab or specific parts.

    Args:
        parts: List of part numbers to run, or None for all
    """
    if economy_mode:
        print("Economy mode enabled: running local/offline-safe path with minimal LLM calls.")
    else:
        setup_api_key()

    if parts is None:
        parts = [1, 2, 3, 4]

    for part in parts:
        if part == 1:
            await part1_attacks(economy_mode=economy_mode)
        elif part == 2:
            await part2_guardrails(economy_mode=economy_mode)
        elif part == 3:
            await part3_testing(economy_mode=economy_mode)
        elif part == 4:
            part4_hitl()
        else:
            print(f"Unknown part: {part}")

    print("\n" + "=" * 60)
    print("Lab 11 complete! Check your results above.")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lab 11: Guardrails, HITL & Responsible AI"
    )
    parser.add_argument(
        "--part", type=int, choices=[1, 2, 3, 4],
        help="Run only a specific part (1-4). Default: run all.",
    )
    parser.add_argument(
        "--economy",
        action="store_true",
        help="Run local economy mode with minimal/no LLM calls for testing and report generation.",
    )
    args = parser.parse_args()

    if args.part:
        asyncio.run(main(parts=[args.part], economy_mode=args.economy))
    else:
        asyncio.run(main(economy_mode=args.economy))
