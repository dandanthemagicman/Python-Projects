import random

print('Welcome to the Password Generator!')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]{}()<>?/\;:'
num=input('How many passwords would you like to generate?: ')
try: num = int(num)
except ValueError:print('Please type an integer.')

length = input('Input your password length: ')
try: length = int(length)
except ValueError:print('Please type an integer.')

print('Here are your passwords:')
for pwd in range(num):
    password=''
    for c in range(length):
        password += random.choice(chars)
    print(password)
