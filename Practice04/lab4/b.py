import json

def deep_diff(obj1, obj2, path=""):
    """
    Рекурсивно сравнивает два JSON объекта и возвращает список различий.
    """
    differences = []
    
    # Получаем все ключи из обоих объектов
    keys1 = set(obj1.keys()) if isinstance(obj1, dict) else set()
    keys2 = set(obj2.keys()) if isinstance(obj2, dict) else set()
    
    # Ключи, которые есть только в первом объекте
    for key in keys1 - keys2:
        current_path = f"{path}.{key}" if path else key
        value1 = json.dumps(obj1[key], separators=(',', ':'))
        differences.append((current_path, f"{value1} -> <missing>"))
    
    # Ключи, которые есть только во втором объекте
    for key in keys2 - keys1:
        current_path = f"{path}.{key}" if path else key
        value2 = json.dumps(obj2[key], separators=(',', ':'))
        differences.append((current_path, f"<missing> -> {value2}"))
    
    # Ключи, которые есть в обоих объектах
    for key in keys1 & keys2:
        current_path = f"{path}.{key}" if path else key
        val1 = obj1[key]
        val2 = obj2[key]
        
        # Если оба значения — словари, рекурсивно сравниваем
        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(deep_diff(val1, val2, current_path))
        # Иначе, если значения отличаются
        elif val1 != val2:
            value1 = json.dumps(val1, separators=(',', ':'))
            value2 = json.dumps(val2, separators=(',', ':'))
            differences.append((current_path, f"{value1} -> {value2}"))
    
    return differences

# Читаем входные данные
obj_a = json.loads(input().strip())
obj_b = json.loads(input().strip())

# Находим различия
diffs = deep_diff(obj_a, obj_b)

# Сортируем по пути
diffs.sort(key=lambda x: x[0])

# Выводим результат
if diffs:
    for path, diff in diffs:
        print(f"{path} : {diff}")
else:
    print("No differences")