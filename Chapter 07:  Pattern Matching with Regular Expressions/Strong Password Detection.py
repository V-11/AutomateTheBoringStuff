import re

Password = input("Enter your password: ")

PasswordRegex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

CheckPassword = PasswordRegex.search(Password)

print("Strong Password") if CheckPassword != None else print("Weak Password")
