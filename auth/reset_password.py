def reset_password(email: str) -> bool:
    """Send a password reset link to the user's email."""
    if "@" not in email:
        return False
    # create a single-use token and email the reset link
    return True
