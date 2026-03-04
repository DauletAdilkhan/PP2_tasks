import json

def apply_patch(source, patch):
    
    result = source.copy()
    print(result,"\n")
    
    for key, patch_value in patch.items():
        print(key,patch_value,"\n")
        if patch_value is None:
            result.pop(key, None)
        elif key in result and type(result[key]) is dict and type(patch_value) is dict:
            print(key,"\n")
            result[key] = apply_patch(result[key], patch_value)
        else:
            result[key] = patch_value
    
    return result

source = json.loads('{"user":{"name":"Ann","age":20},"active":true}')
patch = json.loads('{"user":{"age":21},"active":false}')

patched = apply_patch(source, patch)

print(json.dumps(patched, separators=(',', ':'), sort_keys=True))