import random
password_length = 15
characters = "abcdefghijklmnopqrstuvwxyz1234567890"
password = ""
for index in range(password_length):
    password = password + random.choice(characters)
print("Password generated:{}".format(password))
