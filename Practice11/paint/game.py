# first run the code without activating the base_layer
# then activate the base_layer (uncomment 3 related lines of code) 
# and run the code again

import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

#палитра
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0
prevX = 0
prevY = 0

# Новые переменные
current_color = colorWHITE
current_tool = "draw"

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# круг
def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    return (x1, y1, radius)

# квадрат (сторона = max(ширина, высота))
def calculate_square(x1, y1, x2, y2):
    side = max(abs(x2 - x1), abs(y2 - y1))
    if x2 >= x1 and y2 >= y1:
        return pygame.Rect(x1, y1, side, side)
    elif x2 < x1 and y2 >= y1:
        return pygame.Rect(x1 - side, y1, side, side)
    elif x2 >= x1 and y2 < y1:
        return pygame.Rect(x1, y1 - side, side, side)
    else:
        return pygame.Rect(x1 - side, y1 - side, side, side)

# прямоугольный треугольник (по двум точкам - катеты)
def calculate_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x1, y2)]

# равносторонний треугольник (первая точка - центр, вторая - радиус и направление)
def calculate_equilateral_triangle(x1, y1, x2, y2):
    side = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    height = side * math.sqrt(3) / 2
    
    # Определяем направление
    dx = x2 - x1
    dy = y2 - y1
    
    if dx != 0 or dy != 0:
        # Нормализуем направление
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        
        # Перпендикулярное направление
        perp_dx = -dy
        perp_dy = dx
        
        # Вершины равностороннего треугольника
        # Основание перпендикулярно направлению от центра
        half_side = side / 2
        p1 = (x1 - half_side * perp_dx, y1 - half_side * perp_dy)
        p2 = (x1 + half_side * perp_dx, y1 + half_side * perp_dy)
        p3 = (x1 + height * dx, y1 + height * dy)
    else:
        # Если точки совпадают, рисуем маленький треугольник
        p1 = (x1 - 20, y1 + 20)
        p2 = (x1 + 20, y1 + 20)
        p3 = (x1, y1 - 20)
    
    return [p1, p2, p3]

# ромб (по диагоналям)
def calculate_rhombus(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    
    return [
        (center_x, center_y - dy),  # верх
        (center_x + dx, center_y),  # право
        (center_x, center_y + dy),  # низ
        (center_x - dx, center_y)   # лево
    ]

running = True

while running:
    # Очищаем экран и показываем base_layer
    screen.blit(base_layer, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
            # Для draw и eraser сразу начинаем рисовать
            if current_tool == "draw":
                pygame.draw.circle(screen, current_color, (prevX, prevY), THICKNESS)
            elif current_tool == "eraser":
                pygame.draw.circle(screen, colorBLACK, (prevX, prevY), THICKNESS)
            
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                
                # Восстанавливаем base_layer перед предпросмотром
                screen.blit(base_layer, (0, 0))
                
                if current_tool == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "circle":
                    pygame.draw.circle(screen, current_color, (prevX, prevY), 
                                     int(((currX - prevX)**2 + (currY - prevY)**2)**0.5), THICKNESS)
                elif current_tool == "draw":
                    # Рисуем линию и сразу сохраняем
                    pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))  # Сохраняем сразу
                    prevX, prevY = currX, currY
                elif current_tool == "eraser":
                    pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))  # Сохраняем сразу
                    prevX, prevY = currX, currY
                    #adding new figures
                elif current_tool == "square":
                    pygame.draw.rect(screen, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "right_triangle":
                    points = calculate_right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)
                elif current_tool == "equilateral_triangle":
                    points = calculate_equilateral_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)
                elif current_tool == "rhombus":
                    points = calculate_rhombus(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            
            # Рисуем финальную фигуру для rectangle и circle
            if current_tool == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif current_tool == "circle":
                radius = int(((currX - prevX)**2 + (currY - prevY)**2)**0.5)
                pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif current_tool == "square":
                pygame.draw.rect(screen, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif current_tool == "right_triangle":
                points = calculate_right_triangle(prevX, prevY, currX, currY)
                pygame.draw.polygon(screen, current_color, points, THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif current_tool == "equilateral_triangle":
                points = calculate_equilateral_triangle(prevX, prevY, currX, currY)
                pygame.draw.polygon(screen, current_color, points, THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif current_tool == "rhombus":
                points = calculate_rhombus(prevX, prevY, currX, currY)
                pygame.draw.polygon(screen, current_color, points, THICKNESS)
                base_layer.blit(screen, (0, 0))
            # Для draw и eraser уже всё сохранено в MOUSEMOTION

        if event.type == pygame.KEYDOWN: 
            # Выбор инструмента (цифры)
            if event.key == pygame.K_1:
                current_tool = "draw"
                print("Режим: Рисование")
            elif event.key == pygame.K_2:
                current_tool = "rectangle"
                print("Режим: Прямоугольник")
            elif event.key == pygame.K_3:
                current_tool = "circle"
                print("Режим: Круг")
            elif event.key == pygame.K_4:
                current_tool = "eraser"
                print("Режим: Ластик")
            elif event.key == pygame.K_5:
                current_tool = "square"
                print("Режим: Квадрат")
            elif event.key == pygame.K_6:
                current_tool = "right_triangle"
                print("Режим: Прямоугольный треугольник")
            elif event.key == pygame.K_7:
                current_tool = "equilateral_triangle"
                print("Режим: Равносторонний треугольник")
            elif event.key == pygame.K_8:
                current_tool = "rhombus"
                print("Режим: Ромб")


            #выбор цвета
            if event.key == pygame.K_r:
                current_color = colorRED
                print("Цвет: Красный")
            elif event.key == pygame.K_g:
                current_color = colorGREEN
                print("Цвет: Зеленый")
            elif event.key == pygame.K_b:
                current_color = colorBLUE
                print("Цвет: Синий")
            elif event.key == pygame.K_y:
                current_color = colorYELLOW
                print("Цвет: Желтый")
            elif event.key == pygame.K_w:
                current_color = colorWHITE
                print("Цвет: Белый")
            
            # Изменение толщины
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                THICKNESS += 1
                print(f"Толщина: {THICKNESS}")
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
                print(f"Толщина: {THICKNESS}")
            
            # Очистка экрана (клавиша C)
            if event.key == pygame.K_c:
                screen.fill(colorBLACK)
                base_layer.fill(colorBLACK)
                print("Экран очищен")
    
    # Показываем подсказки
    font = pygame.font.Font(None, 24)
    hint1 = font.render(f"Tool: {current_tool}  Size: {THICKNESS}", True, colorWHITE)
    hint2 = font.render("1:Draw 2:Rect 3:Circle 4:Eraser 5:Square 6:RightTri 7:EqTri 8:Rhombus", True, colorWHITE)
    hint3 = font.render("R,G,B,Y,W - Colors | +/- Size | C - Clear", True, colorWHITE)
    screen.blit(hint1, (10, 10))
    screen.blit(hint2, (10, 35))
    screen.blit(hint3, (10, 60))
    
    
    pygame.display.flip()
    clock.tick(60)