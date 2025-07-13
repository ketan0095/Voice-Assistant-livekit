def require(value, name: str):
    if not value:
        raise ValueError(f"Missing required config value: {name}")
    return value