import string
import random

def PasswordGenerate(length):
    password = ''
    charracter = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += random.choice(charracter)
    return password
length = int(input('Enter length of password = '))
print(PasswordGenerate(length))