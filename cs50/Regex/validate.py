import re

email = input("What's your email?").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|in|us|aus|org|net)$",email):    # \w = [a-zA-Z0-9_]
    print("vaild")
else:
    print("Invaild")