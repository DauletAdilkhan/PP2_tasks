g = 0

def outer():
    n = 0
    
    def inner():
        nonlocal n
        global g
        
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
                local_var = value

        return n
    
    final_n = inner()
    return final_n

final_n = outer()

print(g, final_n)