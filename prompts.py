"""
prompts.py
-----------
Prompt-building utilities for AI Multiverse Chat Studio.
"""

# Supported response languages shown in the sidebar selector
LANGUAGES: list[str] = [
    "English",
    "Hindi",
    "Spanish",
    "French",
    "German",
    "Japanese",
    "Portuguese",
    "Arabic",
    "Chinese (Simplified)",
    "Italian",
]


def build_personality_prompt(
    personality_name: str,
    personality_description: str,
    personality_behavior: str,
    language: str,
) -> str:
    """
    Compose the system prompt string for a given personality.

    Parameters
    ----------
    personality_name : str
        Display name of the selected persona (e.g. "The Sage").
    personality_description : str
        Short public bio for the persona.
    personality_behavior : str
        Detailed instruction describing how the persona should behave.
    language : str
        The language the model should reply in.

    Returns
    -------
    str
        The system prompt string to pass as the ``system`` role message.
    """
    return (
        f"System Directive:\n"
        f"You are acting as the persona described below. "
        f"Your response must stay in-character, follow the specified style and "
        f"guidelines, and be written in the specified language.\n\n"
        f"--- Persona Profile ---\n"
        f"Name: {personality_name}\n"
        f"Description: {personality_description}\n"
        f"Behavior Guidelines: {personality_behavior}\n"
        f"Response Language: {language}"
    )
