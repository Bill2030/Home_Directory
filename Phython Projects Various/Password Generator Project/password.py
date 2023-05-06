import random

passlen = int(input("Enter the length of your password \n"))
s = "abcdgefhgvctryyfdekmjFHJWQCHSJ@#$%^1234567854909"
p = "".join(random.sample(s,passlen))
print(p)






