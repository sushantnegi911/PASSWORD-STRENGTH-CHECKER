import re
def password_strength(password: str) -> str:
    """Return password strength: Strong, Medium, or Weak."""
    if len(password) < 8:
        return "Weak"

    has_letter = bool(re.search(r"[A-Za-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    if has_letter and has_digit and has_special:
        return "Strong"
    if has_letter and has_digit:
        return "Medium"
    return "Weak"
if __name__ == "__main__":
    pwd = input("Enter a password: ")
    print(password_strength(pwd))
