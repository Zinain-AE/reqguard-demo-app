from auth.reset_password import reset_password

def test_reset_password_sends_email():
    assert reset_password("user@example.com") is True

def test_reset_password_rejects_invalid_email():
    assert reset_password("not-an-email") is False
