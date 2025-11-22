def check_password_strength_easy(password):
    
    print("--- Password Strength Report ---")
    is_strong = True  # Start by assuming it's strong

    # 1. Check Length
    if len(password) < 8:
        print(" FAILED: Password must be at least 8 characters long.")
        is_strong = False
    else:
        print("PASS: Length requirement met (8+ characters).")

    # 2. Check for Uppercase
    found_upper = False

    for char in password:
      if char.isupper():
        found_upper = True
        break
    if not found_upper:
        print("FAILED: Password must contain at least one uppercase letter.")
        is_strong = False
    else:
        print("PASS: Uppercase requirement met.")

    # 3. Check for Lowercase
    found_lower = False
    for char in password:
        if char.islower():
            found_lower = True
            break
    if not found_lower:
        print("FAILED: Password must contain at least one lowercase letter.")
        is_strong = False
    else:
        print("PASS: Lowercase requirement met.")

    # 4. Check for Digits
    digits=[1,2,3,4,5,6,7,8,9]
    found_digit=False
    for char in password:
         if '0' <= char <= '9':
            found_digit=True
            break
    if not found_digit:
        print("FAILED: Password must contain at least one digit.")
        is_strong = False
    else:
        print("PASS: Digit requirement met.")
    # 5. Check for special character
    special_character=['!','@','#','$','%','^','&','*',]
    found_special=False
    for char in password:
        if char in special_character:
            found_special=True
            break
    if not found_special:
        print("FAILED: Password must contain at least one special character.")
        is_strong = False
    else:
        print("PASS: Special character requirement met.")
    print("--------------------------------")

    if is_strong:
        print("Overall Status: STRONG Password!")
    else:
        print("Overall Status: WEAK Password. Please improve it.")
password = input("Enter your password to check its strength: ")
check_password_strength_easy(password)

