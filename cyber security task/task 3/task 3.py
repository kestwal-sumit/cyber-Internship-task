import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one uppercase letter (A-Z).")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one lowercase letter (a-z).")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one digit (0–9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>\/?]', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one special character (e.g., @, #, $, !).")

    # Determine strength
    if score == 5:
        strength = "🟢 Strong"
    elif 3 <= score < 5:
        strength = "🟡 Moderate"
    else:
        strength = "🔴 Weak"

    return strength, feedback

def main():
    print("=== 🔐 Password Strength Checker ===")
    password = input("Enter a password to check: ")

    strength, suggestions = check_password_strength(password)

    print("\n🔎 Password Strength:", strength)

    if suggestions:
        print("\n💡 Suggestions to improve your password:")
        for tip in suggestions:
            print(tip)
    else:
        print("✅ Your password meets all recommended criteria!")

if __name__ == "__main__":
    main()
