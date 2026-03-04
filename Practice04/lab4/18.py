x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

x2_ref = x2
y2_ref = -y2

dx = x2_ref - x1
dy = y2_ref - y1

t = -y1 / dy

x = x1 + t * dx
y = 0.0

print(f"{x:.10f} {y:.10f}")