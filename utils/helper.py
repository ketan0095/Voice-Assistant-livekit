"""Helper functions for agent."""

def require(value, name: str):
    """
    Ensure that a required configuration value is present.

    Args:
        value: The value to check for presence.
        name (str): The name of the configuration field (used in the error message).

    Returns:
        The original value if present.

    Raises:
        ValueError: If the value is falsy (e.g. None, empty string).
    """
    if not value:
        raise ValueError(f"Missing required config value: {name}")
    return value
