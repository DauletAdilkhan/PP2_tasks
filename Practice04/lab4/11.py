import json
def app_pat(s,p):
    result= sou.copy()

    for key,value in p.items():
        if value is None:
            result.pop(key, None)
        elif key in result and type(result[key])is dict and type(value)is dict:
            result[key]= app_pat(result[key],value)
        else:
            result[key]=value
    return result

sou=json.loads(input())
pat= json.loads(input())
a=app_pat(sou,pat)
print(json.dumps(a, separators=(',', ':'), sort_keys=True))
