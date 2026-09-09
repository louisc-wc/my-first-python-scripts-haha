def check_password():
    print("Welcome to the Password Validator")
    password = input("Enter a password to test:")

    if len(password) >=8:
        print("Success: This password meets the minimum length requirement.")
    else:
        print("Weak: Passwords must be at least 8 characters long.")

check_password()