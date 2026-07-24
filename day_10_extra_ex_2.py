print("=" * 55)
print("        PASSWORD STRENGTH CHECKER")
print("=" * 55)

special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

while True:

    password = input("\nEnter your password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("\nThank you for using Password Strength Checker!")
        break

    length = len(password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check every character
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_characters:
            has_special = True

    # Calculate score
    score = 0

    if length >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    common_passwords = {
        "123", "1234", "12345", "123456", "12345678",
        "password", "pass123", "qwerty", "admin", "letmein",
        "welcome", "secret", "abc123", "111111", "000000"
    }

    password_lower = password.lower()
    is_common_password = password_lower in common_passwords
    is_all_digits = password.isdigit()
    is_all_letters = password.isalpha()
    complexity_types = sum([has_upper, has_lower, has_digit, has_special])

    print("\n" + "=" * 55)
    print("RESULT")
    print("=" * 55)

    # Password Strength
    if is_common_password or is_all_digits or is_all_letters or (length < 4 and (has_digit or has_special)):
        strength = "EASILY GUESSED"
    elif complexity_types >= 4 and length >= 8:
        strength = "VERY STRONG / HARD TO GUESS"
    elif complexity_types >= 3:
        strength = "STRONG / HARD TO GUESS"
    elif complexity_types == 2:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    print("Password Strength :", strength)

    # Suggestions
    print("\nSuggestions:")

    if is_common_password:
        print("- This password is very common and easy to guess.")

    if is_all_digits:
        print("- Use letters and symbols to make it harder to guess.")

    if length < 8:
        print("- Password should be at least 8 characters long.")

    if not has_upper:
        print("- Add at least one uppercase letter (A-Z).")

    if not has_lower:
        print("- Add at least one lowercase letter (a-z).")

    if not has_digit:
        print("- Add at least one number (0-9).")

    if not has_special:
        print("- Add at least one special character (!,@,#,$ etc.).")

    if score == 5:
        print("- Excellent! Your password follows all recommended practices.")

    # Character set size
    charset = 0

    if has_lower:
        charset += 26

    if has_upper:
        charset += 26

    if has_digit:
        charset += 10

    if has_special:
        charset += 32

    if charset == 0:
        charset = 1

    possibilities = charset ** length

    print("\n" + "=" * 55)
    print("PASSWORD SECURITY ANALYSIS")
    print("=" * 55)

    print("Password Length        :", length)
    print("Character Set Size     :", charset)
    print(f"Possible Combinations  : {possibilities:,}")

    # Difficulty Level
    if possibilities < 1_000_000:
        print("Guessing Difficulty    : Very Easy")
    elif possibilities < 1_000_000_000:
        print("Guessing Difficulty    : Easy")
    elif possibilities < 1_000_000_000_000:
        print("Guessing Difficulty    : Moderate")
    elif possibilities < 1_000_000_000_000_000:
        print("Guessing Difficulty    : Hard")
    else:
        print("Guessing Difficulty    : Extremely Hard")

    # Brute Force Time
    attempts_per_second = 1_000_000_000

    seconds = possibilities / attempts_per_second

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    print("\nEstimated Time to Guess:")

    if years >= 1:
        print(f"{years:,.2f} years")
    elif days >= 1:
        print(f"{days:,.2f} days")
    elif hours >= 1:
        print(f"{hours:,.2f} hours")
    elif minutes >= 1:
        print(f"{minutes:,.2f} minutes")
    else:
        print(f"{seconds:.2f} seconds")

    print("=" * 55)