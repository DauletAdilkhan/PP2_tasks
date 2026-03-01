import math

def distance(p1, p2):
    """Расстояние между двумя точками"""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def point_on_circle(angle):
    """Точка на окружности радиуса R под углом angle"""
    return (R * math.cos(angle), R * math.sin(angle))

def tangent_points(P, R):
    """Находит точки касания из точки P к окружности радиуса R"""
    x, y = P
    d2 = x*x + y*y
    if d2 <= R*R:
        return []  # Точка внутри круга
    
    d = math.sqrt(d2)
    # Угол до точки
    alpha = math.atan2(y, x)
    # Угол отклонения касательной
    delta = math.acos(R / d)
    
    t1 = alpha + delta
    t2 = alpha - delta
    
    return [(R * math.cos(t1), R * math.sin(t1)), 
            (R * math.cos(t2), R * math.sin(t2))]

def arc_length(angle1, angle2, R):
    """Длина дуги между двумя углами на окружности (кратчайшая)"""
    diff = abs(angle1 - angle2)
    diff = min(diff, 2*math.pi - diff)
    return R * diff

# Читаем входные данные
R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

A = (x1, y1)
B = (x2, y2)

# Случай 1: отрезок AB не пересекает круг
# Проверяем, пересекает ли отрезок окружность
# Для простоты проверим расстояние от центра до прямой
def point_segment_distance(p, a, b):
    """Расстояние от точки p до отрезка ab"""
    x0, y0 = p
    x1, y1 = a
    x2, y2 = b
    
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0 and dy == 0:
        return math.hypot(x0 - x1, y0 - y1)
    
    t = ((x0 - x1) * dx + (y0 - y1) * dy) / (dx*dx + dy*dy)
    
    if t < 0:
        return math.hypot(x0 - x1, y0 - y1)
    elif t > 1:
        return math.hypot(x0 - x2, y0 - y2)
    else:
        projx = x1 + t * dx
        projy = y1 + t * dy
        return math.hypot(x0 - projx, y0 - projy)

dist_to_line = point_segment_distance((0, 0), A, B)

# Если отрезок не пересекает круг и обе точки вне - идём прямо
if dist_to_line >= R and distance(A, (0, 0)) >= R and distance(B, (0, 0)) >= R:
    # Проверяем, не огибает ли путь вокруг круга
    # Если обе точки видят друг друга без пересечения круга
    print(f"{distance(A, B):.10f}")
    exit()

# Случай 2: нужно огибать круг
# Находим касательные из A и B к окружности
tans_A = tangent_points(A, R)
tans_B = tangent_points(B, R)

min_path = float('inf')

# Пробуем все комбинации касательных
for tA in tans_A:
    for tB in tans_B:
        # Длина пути: A -> tA -> дуга -> tB -> B
        path = distance(A, tA) + distance(B, tB)
        
        # Углы точек на окружности
        angleA = math.atan2(tA[1], tA[0])
        angleB = math.atan2(tB[1], tB[0])
        
        # Добавляем длину дуги
        path += arc_length(angleA, angleB, R)
        
        min_path = min(min_path, path)

print(f"{min_path:.10f}")