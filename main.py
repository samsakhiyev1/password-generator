import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@!@#$%^&*"
number = int(input("Enter the amount of passwords: "))
length = int(input("Enter the length of passwords: "))
for i in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)