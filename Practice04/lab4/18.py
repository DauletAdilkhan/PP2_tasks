x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Отражаем B
x2_ref = x2
y2_ref = -y2

# Параметрическое уравнение прямой через A и B'
# (x, y) = (x1, y1) + t * (dx, dy), где dx = x2_ref - x1, dy = y2_ref - y1
dx = x2_ref - x1
dy = y2_ref - y1

# Ищем t, при котором y = 0
# y1 + t*dy = 0  =>  t = -y1 / dy
t = -y1 / dy

# Координата x пересечения
x = x1 + t * dx
y = 0.0

print(f"{x:.10f} {y:.10f}")