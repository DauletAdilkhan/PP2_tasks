import json

def apply_patch(source, patch):
    """
    Применяет patch к source согласно правилам:
    - Если ключ из patch отсутствует в source → добавляем
    - Если значение в patch = null → удаляем ключ из source
    - Если оба значения — объекты → рекурсивно применяем правила
    - Иначе → заменяем значение source на значение patch
    """
    result = source.copy()
    print(result,"\n")
    
    for key, patch_value in patch.items():
        print(key,patch_value,"\n")
        if patch_value is None:
            # Удаляем ключ, если он есть
            result.pop(key, None)
        elif key in result and type(result[key]) is dict and type(patch_value) is dict:
            print(key,"\n")
            # Рекурсивно обрабатываем вложенные объекты
            result[key] = apply_patch(result[key], patch_value)
        else:
            # Добавляем или заменяем значение
            result[key] = patch_value
    
    return result

# Читаем входные данные
source = json.loads('{"user":{"name":"Ann","age":20},"active":true}')
patch = json.loads('{"user":{"age":21},"active":false}')

# Применяем патч
patched = apply_patch(source, patch)

# Выводим результат с сортировкой ключей
print(json.dumps(patched, separators=(',', ':'), sort_keys=True))