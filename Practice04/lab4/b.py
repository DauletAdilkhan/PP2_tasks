import json

def deep_diff(obj1, obj2, path=""):
    differences = []
    
    keys1 = set(obj1.keys()) if isinstance(obj1, dict) else set()
    keys2 = set(obj2.keys()) if isinstance(obj2, dict) else set()
    
    for key in keys1 - keys2:
        current_path = f"{path}.{key}" if path else key
        value1 = json.dumps(obj1[key], separators=(',', ':'))
        differences.append((current_path, f"{value1} -> <missing>"))
    
    for key in keys2 - keys1:
        current_path = f"{path}.{key}" if path else key
        value2 = json.dumps(obj2[key], separators=(',', ':'))
        differences.append((current_path, f"<missing> -> {value2}"))
    
    for key in keys1 & keys2:
        current_path = f"{path}.{key}" if path else key
        val1 = obj1[key]
        val2 = obj2[key]
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(deep_diff(val1, val2, current_path))
        elif val1 != val2:
            value1 = json.dumps(val1, separators=(',', ':'))
            value2 = json.dumps(val2, separators=(',', ':'))
            differences.append((current_path, f"{value1} -> {value2}"))
    
    return differences

obj_a = json.loads(input().strip())
obj_b = json.loads(input().strip())

diffs = deep_diff(obj_a, obj_b)

diffs.sort(key=lambda x: x[0])

if diffs:
    for path, diff in diffs:
        print(f"{path} : {diff}")
else:
    print("No differences")