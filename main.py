import random

chars = 'abcdefghijklnopqrstuvwxyz'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars = '1234567890'
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
