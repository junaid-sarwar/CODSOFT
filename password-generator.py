import random
import string

length=int(input("Enter Your Password Length: "))

lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
numbers=string.digits
special_characters=string.punctuation

all=lower_case+upper_case+numbers+special_characters

password=random.sample(all,length)
password="".join(password)


print(f"Your Random Generated Password is: {password}")