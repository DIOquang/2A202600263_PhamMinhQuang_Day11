"""
Lab 11 — Configuration & API Key Setup
"""
import os
from openai import OpenAI


def setup_api_key():
    """Load OpenAI API key from environment or prompt."""
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = input("Enter OpenAI API Key: ")
    print("OpenAI API key loaded.")


def get_openai_client():
    """Get OpenAI client instance."""
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# Model configuration
OPENAI_MODEL = "gpt-4-turbo"  # or "gpt-3.5-turbo" for faster/cheaper
JUDGE_MODEL = "gpt-4-turbo"   # for LLM-as-Judge
MAX_TOKENS = 500

# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
