import pygame
from color_palette import *
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 30
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Настройки
INITIAL_SPEED = 5 #начальная скорость
MAX_SPEED = 15 #максимальная скорость
FOODS_PER_LEVEL = 3 #еды нужно для повышения

def draw_grid(): #сетка для ориентира 
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point: #координаты
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow = False

    def move(self):
        if self.grow:
            new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
            self.body.insert(0, new_head)
            self.grow = False
        else:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            self.body[0].x += self.dx
            self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_wall_collision(self): #проверка колизии (выход из окна)
        head = self.body[0]
        return (head.x < 0 or head.x >= WIDTH // CELL or 
                head.y < 0 or head.y >= HEIGHT // CELL)

    def check_self_collision(self): #проверка колизии(с самим собой)
        head = self.body[0]
        return any(head.x == seg.x and head.y == seg.y for seg in self.body[1:])

    def eat_food(self, food): #проверка еды
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow = True #на след ходу увеличивается
            return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def randomize(self, snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
             # Проверяем, не занята ли эта позиция телом змейки
            # any() вернет True, если хотя бы один сегмент имеет такие координаты
            if not any(seg.x == x and seg.y == y for seg in snake_body):
                self.pos.x = x
                self.pos.y = y
                break

def show_game_over(score, level):
    screen.fill(colorBLACK)
    texts = [
        font.render("GAME OVER!", True, colorRED),
        font.render(f"Score: {score}  Level: {level}", True, colorWHITE),
        font.render("Press SPACE to restart or ESC to quit", True, colorGRAY)
    ]
    for i, text in enumerate(texts):
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 30 + i*40))
        screen.blit(text, rect)
    pygame.display.flip()
    
     # Ожидаем нажатия клавиши
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

# Основная игра
def main():
    snake = Snake()
    food = Food()
    food.randomize(snake.body)
    score = 0
    level = 1
    speed = INITIAL_SPEED
    
    running = True
    while running:
        # Управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx, snake.dy = 1, 0
                elif event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_UP and snake.dy == 0:
                    snake.dx, snake.dy = 0, -1

        # Движение и проверки
        snake.move()
        
        if snake.check_wall_collision() or snake.check_self_collision():
            if show_game_over(score, level):
                # Рестарт
                snake = Snake()
                food.randomize(snake.body)
                score = 0
                level = 1
                speed = INITIAL_SPEED
                continue
            else:
                running = False
                break

        # Еда и уровни
        if snake.eat_food(food):
            score += 1
            food.randomize(snake.body)
            
            # Повышение уровня
            new_level = score // FOODS_PER_LEVEL + 1
            if new_level > level:
                level = new_level
                speed = min(INITIAL_SPEED + (level - 1) * 2, MAX_SPEED)

        # Отрисовка
        screen.fill(colorBLACK)
        draw_grid()
        snake.draw()
        food.draw()
        
        # Отображение счета и уровня
        screen.blit(font.render(f"Score: {score}", True, colorWHITE), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, colorWHITE), (10, 50))
        
        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()