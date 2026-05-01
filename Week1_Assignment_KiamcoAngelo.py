while True:
    password = input("Enter a password: ")

    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    if has_letter and has_number:
        print("Password Accepted")
        break
    else:
        print("Invalid Password. Try Again.")
        continue