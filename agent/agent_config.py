
"""Gather all agent config"""

DEFAULT_WELCOME_MSG ="Hello, how are you?"
DEFAULT_CLOSING_MSG ="Thank you, have a good day."


def get_all_configs():
    """Fetch all agent configs"""
    return {
        "welcome_closing":{
            "welcome":DEFAULT_WELCOME_MSG,
            "closing":DEFAULT_CLOSING_MSG
        }
    }
