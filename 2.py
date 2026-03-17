import re

users = eval(input())

pattern = r"^@[a-z]*_[a-z_]*$"

for user in users:
    if re.match(pattern, user['handle']):
        print(user['user_id'])