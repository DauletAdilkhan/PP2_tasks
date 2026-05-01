# first run the code without activating the base_layer
# then activate the base_layer (uncomment 3 related lines of code) 
# and run the code again

import pygame
import math
from datetime import datetime

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
THICKNESS_LEVELS = {pygame.K_1: 2, pygame.K_2: 5, pygame.K_3: 10}

currX = 0
currY = 0
prevX = 0
prevY = 0

# Новые переменные
current_color = colorWHITE
current_tool = "draw"

# Для line tool
line_start = None
line_end = None
drawing_line = False

# Для текста
text_input = ""
text_position = None
text_active = False
text_font = pygame.font.SysFont('Arial', 24)

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

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

# круг
def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    return (x1, y1, radius)

# прямоугольный треугольник (по двум точкам - катеты)
def calculate_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x1, y2)]

# равносторонний треугольник
def calculate_equilateral_triangle(x1, y1, x2, y2):
    side = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    height = side * math.sqrt(3) / 2
    
    dx = x2 - x1
    dy = y2 - y1
    
    if dx != 0 or dy != 0:
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        
        perp_dx = -dy
        perp_dy = dx
        
        half_side = side / 2
        p1 = (x1 - half_side * perp_dx, y1 - half_side * perp_dy)
        p2 = (x1 + half_side * perp_dx, y1 + half_side * perp_dy)
        p3 = (x1 + height * dx, y1 + height * dy)
    else:
        p1 = (x1 - 20, y1 + 20)
        p2 = (x1 + 20, y1 + 20)
        p3 = (x1, y1 - 20)
    
    return [p1, p2, p3]

# ромб
def calculate_rhombus(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    
    return [
        (center_x, center_y - dy),
        (center_x + dx, center_y),
        (center_x, center_y + dy),
        (center_x - dx, center_y)
    ]

# Flood fill implementation
def flood_fill(surface, x, y, target_color, replacement_color):
    if target_color == replacement_color:
        return
    
    stack = [(x, y)]
    visited = set()
    width, height = surface.get_size()
    
    while stack:
        cx, cy = stack.pop()
        
        if (cx, cy) in visited:
            continue
            
        if cx < 0 or cx >= width or cy < 0 or cy >= height:
            continue
            
        try:
            current_color = surface.get_at((cx, cy))[:3]
        except:
            continue
            
        if current_color != target_color:
            continue
            
        surface.set_at((cx, cy), replacement_color)
        visited.add((cx, cy))
        
        # Add neighbors
        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))

# Save canvas with timestamp
def save_canvas():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"canvas_{timestamp}.png"
    pygame.image.save(base_layer, filename)
    print(f"Canvas saved as {filename}")

running = True

while running:
    screen.blit(base_layer, (0, 0))
    
    # Preview для line tool
    if drawing_line and line_start and line_end:
        pygame.draw.line(screen, current_color, line_start, line_end, THICKNESS)
    
    # Preview для текста
    if text_active and text_position:
        text_surface = text_font.render(text_input + "|", True, current_color)
        screen.blit(text_surface, text_position)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Ctrl+S to save
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()
            
            # Text tool handling
            if text_active and text_position:
                if event.key == pygame.K_RETURN:
                    # Confirm text
                    text_surface = text_font.render(text_input, True, current_color)
                    screen.blit(text_surface, text_position)
                    base_layer.blit(screen, (0, 0))
                    text_input = ""
                    text_active = False
                    text_position = None
                    print("Text added to canvas")
                elif event.key == pygame.K_ESCAPE:
                    # Cancel text
                    text_input = ""
                    text_active = False
                    text_position = None
                    print("Text input cancelled")
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    # Add character
                    text_input += event.unicode
                continue  # Skip other key handling when typing

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check for text tool activation
            if current_tool == "text":
                text_position = event.pos
                text_active = True
                text_input = ""
                print("Text tool activated. Type your text, press Enter to confirm, Escape to cancel")
                continue
            
            print("LMB pressed!")
            LMBpressed = True
            
            # Для line tool
            if current_tool == "line":
                line_start = event.pos
                drawing_line = True
                prevX, prevY = event.pos
            # Для pencil и других инструментов
            elif current_tool == "draw":
                prevX = event.pos[0]
                prevY = event.pos[1]
                pygame.draw.circle(screen, current_color, (prevX, prevY), THICKNESS)
            elif current_tool == "eraser":
                prevX = event.pos[0]
                prevY = event.pos[1]
                pygame.draw.circle(screen, colorBLACK, (prevX, prevY), THICKNESS)
            elif current_tool == "flood_fill":
                try:
                    x, y = event.pos
                    target_color = base_layer.get_at((x, y))[:3]
                    flood_fill(base_layer, x, y, target_color, current_color)
                    print(f"Flood fill at ({x}, {y}) with color {current_color}")
                except Exception as e:
                    print(f"Flood fill error: {e}")
            else:
                prevX = event.pos[0]
                prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                
                screen.blit(base_layer, (0, 0))
                
                # Для line tool - обновляем preview
                if current_tool == "line" and drawing_line:
                    line_end = (currX, currY)
                    pygame.draw.line(screen, current_color, line_start, line_end, THICKNESS)
                elif current_tool == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "square":
                    pygame.draw.rect(screen, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "circle":
                    pygame.draw.circle(screen, current_color, (prevX, prevY), 
                                     int(((currX - prevX)**2 + (currY - prevY)**2)**0.5), THICKNESS)
                elif current_tool == "right_triangle":
                    points = calculate_right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)
                elif current_tool == "equilateral_triangle":
                    points = calculate_equilateral_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)
                elif current_tool == "rhombus":
                    points = calculate_rhombus(prevX, prevY, currX, currY)
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)
                elif current_tool == "draw":
                    pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))
                    prevX, prevY = currX, currY
                elif current_tool == "eraser":
                    pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))
                    prevX, prevY = currX, currY

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            
            if current_tool == "line" and drawing_line:
                currX = event.pos[0]
                currY = event.pos[1]
                # Draw final line
                pygame.draw.line(base_layer, current_color, line_start, (currX, currY), THICKNESS)
                screen.blit(base_layer, (0, 0))
                drawing_line = False
                line_start = None
                line_end = None
            elif current_tool in ["rectangle", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
                currX = event.pos[0]
                currY = event.pos[1]
                
                if current_tool == "rectangle":
                    pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "square":
                    pygame.draw.rect(base_layer, current_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == "circle":
                    radius = int(((currX - prevX)**2 + (currY - prevY)**2)**0.5)
                    pygame.draw.circle(base_layer, current_color, (prevX, prevY), radius, THICKNESS)
                elif current_tool == "right_triangle":
                    points = calculate_right_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
                elif current_tool == "equilateral_triangle":
                    points = calculate_equilateral_triangle(prevX, prevY, currX, currY)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
                elif current_tool == "rhombus":
                    points = calculate_rhombus(prevX, prevY, currX, currY)
                    pygame.draw.polygon(base_layer, current_color, points, THICKNESS)
                
                screen.blit(base_layer, (0, 0))

        if event.type == pygame.KEYDOWN: 
            # Пропускаем если активен ввод текста
            if text_active:
                continue
                
            # Выбор инструмента
            if event.key == pygame.K_1:
                current_tool = "draw"
                print("Режим: Рисование (Pencil)")
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
            elif event.key == pygame.K_9:
                current_tool = "line"
                print("Режим: Линия (Line)")
            elif event.key == pygame.K_0:
                current_tool = "flood_fill"
                print("Режим: Заливка (Flood Fill)")
            elif event.key == pygame.K_t:
                current_tool = "text"
                print("Режим: Текст. Кликните на холст для ввода текста")
            
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
            
            # Изменение толщины (1, 2, 3 клавиши для размера)
            if event.key in THICKNESS_LEVELS:
                THICKNESS = THICKNESS_LEVELS[event.key]
                print(f"Толщина: {THICKNESS} px")
            
            # Очистка экрана (клавиша C)
            if event.key == pygame.K_c:
                screen.fill(colorBLACK)
                base_layer.fill(colorBLACK)
                print("Экран очищен")
    
    # Отображение подсказок
    font = pygame.font.Font(None, 20)
    
    # Row 1: Tools
    tool_texts = [
        "1:Pencil 2:Rect 3:Circle 4:Eraser",
        "5:Square 6:RightTri 7:EqTri 8:Rhombus",
        "9:Line 0:FloodFill T:Text"
    ]
    
    # Row 2: Colors & Brush Sizes
    color_text = "R:Red G:Green B:Blue Y:Yellow W:White"
    brush_text = "1:Small(2px) 2:Medium(5px) 3:Large(10px)"
    
    # Row 3: Actions
    action_text = "C:Clear Canvas Ctrl+S:Save"
    
    y_offset = HEIGHT - 80
    for i, text in enumerate(tool_texts):
        hint = font.render(text, True, colorWHITE)
        screen.blit(hint, (10, y_offset + i * 20))
    
    hint_color = font.render(color_text, True, colorWHITE)
    screen.blit(hint_color, (10, y_offset + 60))
    
    hint_brush = font.render(brush_text, True, colorWHITE)
    screen.blit(hint_brush, (10, y_offset + 80))
    
    hint_action = font.render(action_text, True, colorWHITE)
    screen.blit(hint_action, (10, y_offset + 100))
    
    # Current tool and size
    current_info = font.render(f"Current Tool: {current_tool} | Size: {THICKNESS}px | Color: {current_color}", True, colorYELLOW)
    screen.blit(current_info, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)