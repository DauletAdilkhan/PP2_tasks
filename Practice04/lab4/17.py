import math

def point_in_circle(x, y, R):
    """Проверяет, находится ли точка внутри круга"""
    return x*x + y*y <= R*R

def segment_length_in_circle(R, x1, y1, x2, y2):
    """Возвращает длину отрезка, лежащую внутри круга"""
    
    # Проверяем, находятся ли обе точки внутри
    in1 = point_in_circle(x1, y1, R)
    in2 = point_in_circle(x2, y2, R)
    
    # Если обе точки внутри - весь отрезок
    if in1 and in2:
        return math.hypot(x2 - x1, y2 - y1)
    
    # Если обе снаружи - проверяем пересечение
    if not in1 and not in2:
        # Находим точки пересечения прямой с окружностью
        dx = x2 - x1
        dy = y2 - y1
        
        # Решаем квадратное уравнение
        a = dx*dx + dy*dy
        b = 2*(x1*dx + y1*dy)
        c = x1*x1 + y1*y1 - R*R
        
        disc = b*b - 4*a*c
        
        if disc <= 0:  # Нет пересечений
            return 0.0
        
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2*a)
        t2 = (-b + sqrt_disc) / (2*a)
        
        # Проверяем, попадают ли точки пересечения на отрезок
        t1 = max(0.0, min(1.0, t1))
        t2 = max(0.0, min(1.0, t2))
        
        if t2 <= t1:  # Отрезок не пересекает круг
            return 0.0
        
        # Длина части отрезка внутри круга
        return math.hypot(dx*(t2 - t1), dy*(t2 - t1))
    
    # Одна точка внутри, другая снаружи
    # Находим точку пересечения
    dx = x2 - x1
    dy = y2 - y1
    
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    
    disc = b*b - 4*a*c
    sqrt_disc = math.sqrt(disc)
    
    # Берём t в пределах [0, 1]
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    
    # Выбираем подходящее t
    if 0 <= t1 <= 1:
        t = t1
    else:
        t = t2
    
    # Длина от точки внутри до пересечения
    if in1:
        return math.hypot(dx*t, dy*t)
    else:
        return math.hypot(dx*(1 - t), dy*(1 - t))

# Читаем входные данные
R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

# Вычисляем длину
length = segment_length_in_circle(R, x1, y1, x2, y2)

# Выводим с высокой точностью
print(f"{length:.10f}")