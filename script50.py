while True:
    password = input("enter your password")
    if len(password)<5:
        print("password must be greater than five characters")
    elif not any(char.islower() for char in password):
        print("password must have a lower case letter characters")
    elif not any(char.isupper() for char in password):
        print("password must have a lower case letter characters")
    elif not any(char.isdigit() for char in password):
        print("password must have atleast one digit ")
    elif not any(char in"!@#$%^&*+()+=><,.?/;:{}[]"for char in password):
        print("password must have at least one special character")
    else:
        print("PASSWORD IS STRONG :)")
        break
