import math

def point_in_circle(x, y, R):
    return x*x + y*y <= R*R

def segment_length_in_circle(R, x1, y1, x2, y2):
    
    in1 = point_in_circle(x1, y1, R)
    in2 = point_in_circle(x2, y2, R)
    
    if in1 and in2:
        return math.hypot(x2 - x1, y2 - y1)
    
    if not in1 and not in2:
        dx = x2 - x1
        dy = y2 - y1
        
        a = dx*dx + dy*dy
        b = 2*(x1*dx + y1*dy)
        c = x1*x1 + y1*y1 - R*R
        
        disc = b*b - 4*a*c
        
        if disc <= 0:  
            return 0.0
        
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2*a)
        t2 = (-b + sqrt_disc) / (2*a)
        
        t1 = max(0.0, min(1.0, t1))
        t2 = max(0.0, min(1.0, t2))
        
        if t2 <= t1: 
            return 0.0
        
        return math.hypot(dx*(t2 - t1), dy*(t2 - t1))
    
    dx = x2 - x1
    dy = y2 - y1
    
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    
    disc = b*b - 4*a*c
    sqrt_disc = math.sqrt(disc)
    
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    
    if 0 <= t1 <= 1:
        t = t1
    else:
        t = t2
    
    if in1:
        return math.hypot(dx*t, dy*t)
    else:
        return math.hypot(dx*(1 - t), dy*(1 - t))

R = float(input().strip())
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

length = segment_length_in_circle(R, x1, y1, x2, y2)

print(f"{length:.10f}")