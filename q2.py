password = input("Enter your password: ")

if len(password) < 6 or password.isalpha():
    print("Password Strength: Weak")
elif len(password) >= 6 and password.isalnum():
    print("Password Strength: Moderate")
elif len(password) >= 8 and any(char in "@#$%&" for char in password):
    print("Password Strength: Strong")
else:
    print("Password Strength: Moderate")
