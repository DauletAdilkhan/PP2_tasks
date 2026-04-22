# first run the code without activating the base_layer
# then activate the base_layer (uncomment 3 related lines of code) 
# and run the code again

import pygame

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
    hint2 = font.render("1:Draw 2:Rect 3:Circle 4:Eraser | R,G,B,Y,W - Colors | +/- Size | C - Clear", True, colorWHITE)
    screen.blit(hint1, (10, 10))
    screen.blit(hint2, (10, 35))
    
    pygame.display.flip()
    clock.tick(60)