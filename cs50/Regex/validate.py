import re

email = input("What's your email?").strip()

if re.search(r"^.+@.+\.edu$",email):
    print("vaild")
else:
    print("Invaild")