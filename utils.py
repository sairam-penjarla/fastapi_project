def verify_token(provided_token: str, config_token: str) -> bool:
    return provided_token == config_token
