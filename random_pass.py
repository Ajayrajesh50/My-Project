import random
import string

pass_len=int(input("Enter the length of the password : "))
values=(string.digits+string.ascii_letters+string.punctuation)

password=" "
for i in range(pass_len):
    password+=random.choice(values)
print(password)