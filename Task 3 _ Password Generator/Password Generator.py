import random
import string
length = int(input("Enter the length of the password to be created : "))
values = string.ascii_letters + string.digits + string.punctuation
password = ""
for _ in range(length):
    password += random.choice(values)
print("Password :",password)
