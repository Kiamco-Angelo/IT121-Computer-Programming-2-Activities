while True:
    password = input("Enter a password: ")

    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if has_letter and has_number:
        print("Password accepted.")
        break
    else:
        print("Invalid password. Try again.")
