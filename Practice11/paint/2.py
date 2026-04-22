import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

done = False

# Очищаем экран в начале

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            # Запоминаем начальную позицию
            prevX, prevY = event.pos
        
        if event.type == pygame.MOUSEMOTION:
            print(f"Position of the mouse: {event.pos}, LMBpressed: {LMBpressed}")
            # Рисуем при зажатой ЛКМ
            if LMBpressed:
                currX, currY = event.pos
                # Рисуем линию от предыдущей позиции к текущей
                pygame.draw.line(screen, colorRED, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS = max(1, THICKNESS - 1)  # Не даем толщине стать меньше 1

    pygame.display.flip()
    clock.tick(60)