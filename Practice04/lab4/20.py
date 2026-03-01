# Глобальная переменная
g = 0

def outer():
    # Переменная в функции outer
    n = 0
    
    def inner():
        nonlocal n
        global g
        
        # Читаем количество команд
        m = int(input())
        
        for _ in range(m):
            cmd = input().strip().split()
            scope = cmd[0]
            value = int(cmd[1])
            
            if scope == "global":
                g += value
            elif scope == "nonlocal":
                n += value
            elif scope == "local":
                # Локальная переменная, которая не влияет на g и n
                local_var = value
        
        return n
    
    # Вызываем inner и получаем финальное n
    final_n = inner()
    return final_n

# Запускаем outer и получаем финальное n
final_n = outer()

# Выводим результаты
print(g, final_n)