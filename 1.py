import re
import json
A=input()
a = json.loads(A)
b = r'^@[a-z_]+$'
for i in a:
    hd= i['handle']
    if re.match(b,hd):
        print(i['user_id'])