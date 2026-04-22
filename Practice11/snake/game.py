import pygame
from color_palette import *
import random
import sys

# Initialize Pygame
pygame.init()

# Game constants
WIDTH = 600
HEIGHT = 600
CELL = 30  # Size of each grid cell

# Game settings
INITIAL_SPEED = 5  # Starting FPS
MAX_SPEED = 15     # Maximum speed cap
FOODS_PER_LEVEL = 3  # Number of foods needed to advance a level

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Level Up!")

# Font for displaying score and level
font = pygame.font.Font(None, 36)

def draw_grid():
    """Draw grid lines on the screen"""
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    """Draw chess pattern background (commented out to use solid background)"""
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    """Represents a point/cell position on the grid"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __eq__(self, other):
        """Allow direct comparison of Point objects"""
        return self.x == other.x and self.y == other.y

class Snake:
    """Snake class handling movement, drawing, and collision detection"""
    
    def __init__(self):
        # Initialize snake with 3 segments in the middle of the screen
        center_x = WIDTH // CELL // 2
        center_y = HEIGHT // CELL // 2
        self.body = [
            Point(center_x, center_y),      # Head
            Point(center_x, center_y + 1),  # Body segment
            Point(center_x, center_y + 2)   # Tail
        ]
        self.dx = 0  # Horizontal direction (0 = not moving)
        self.dy = -1 # Vertical direction (-1 = moving up)
        self.grow_flag = False  # Flag to indicate if snake should grow

    def move(self):
        """Move the snake in the current direction"""
        # If snake needs to grow, add a new head without removing tail
        if self.grow_flag:
            # Create new head at current head position + direction
            new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
            self.body.insert(0, new_head)  # Add new head
            self.grow_flag = False  # Reset growth flag
        else:
            # Normal movement: shift all segments
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            
            # Move the head in the current direction
            self.body[0].x += self.dx
            self.body[0].y += self.dy

    def draw(self):
        """Draw the snake on the screen"""
        # Draw head in red
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        
        # Draw body segments in yellow
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_with_food(self, food):
        """Check if snake's head collides with food"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.grow_flag = True  # Snake will grow on next move
            return True
        return False

    def check_collision_with_walls(self):
        """Check if snake hits the wall (border collision)"""
        head = self.body[0]
        # Check if head is outside the grid boundaries
        if (head.x < 0 or head.x >= WIDTH // CELL or
            head.y < 0 or head.y >= HEIGHT // CELL):
            return True
        return False

    def check_collision_with_self(self):
        """Check if snake collides with itself"""
        head = self.body[0]
        # Check if head position matches any body segment
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def change_direction(self, dx, dy):
        """Change snake direction preventing 180-degree turns"""
        # Prevent snake from going back into itself
        if (self.dx == 0 and self.dy == 0) or (self.dx != -dx or self.dy != -dy):
            self.dx = dx
            self.dy = dy

class Food:
    """Food class handling placement and drawing"""
    
    def __init__(self):
        self.pos = Point(0, 0)
        
    def draw(self):
        """Draw food as a green square"""
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        """Generate random position for food that doesn't collide with snake"""
        while True:
            # Generate random coordinates within grid bounds
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            
            # Check if position is occupied by snake
            collision = False
            for segment in snake_body:
                if segment.x == x and segment.y == y:
                    collision = True
                    break
            
            # If position is free, place food here
            if not collision:
                self.pos.x = x
                self.pos.y = y
                break

def show_game_over_screen(score, level):
    """Display game over screen with final stats"""
    screen.fill(colorBLACK)
    
    # Game over text
    game_over_text = font.render("GAME OVER!", True, colorRED)
    score_text = font.render(f"Final Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level Reached: {level}", True, colorWHITE)
    restart_text = font.render("Press SPACE to play again or ESC to quit", True, colorGRAY)
    
    # Center the text
    text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60))
    screen.blit(game_over_text, text_rect)
    
    text_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
    screen.blit(score_text, text_rect)
    
    text_rect = level_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    screen.blit(level_text, text_rect)
    
    text_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 80))
    screen.blit(restart_text, text_rect)
    
    pygame.display.flip()
    
    # Wait for player input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Restart game
                elif event.key == pygame.K_ESCAPE:
                    return False  # Quit game
    return False

def reset_game():
    """Reset all game variables for a new game"""
    snake = Snake()
    food = Food()
    food.generate_random_pos(snake.body)
    score = 0
    level = 1
    current_speed = INITIAL_SPEED
    return snake, food, score, level, current_speed

def main():
    """Main game loop"""
    # Game variables
    snake, food, score, level, current_speed = reset_game()
    
    # Timer for level up animation
    level_up_timer = 0
    level_up_message = ""
    
    # Create clock for FPS control
    clock = pygame.time.Clock()
    
    # Game state
    running = True
    paused = False
    
    # Main game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause game
                    paused = not paused
                
                if not paused:  # Only handle movement if not paused
                    # Arrow key controls
                    if event.key == pygame.K_RIGHT:
                        snake.change_direction(1, 0)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(0, 1)
                    elif event.key == pygame.K_UP:
                        snake.change_direction(0, -1)
        
        if paused:
            # Display pause message
            pause_text = font.render("PAUSED - Press P to continue", True, colorWHITE)
            text_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(pause_text, text_rect)
            pygame.display.flip()
            clock.tick(10)
            continue
        
        # Game logic update
        snake.move()
        
        # Check for collisions
        if snake.check_collision_with_walls() or snake.check_collision_with_self():
            # Game over
            if show_game_over_screen(score, level):
                # Restart game
                snake, food, score, level, current_speed = reset_game()
                level_up_timer = 0
                continue
            else:
                running = False
                break
        
        # Check for food collision
        if snake.check_collision_with_food(food):
            score += 1
            food.generate_random_pos(snake.body)
            
            # Level up logic
            new_level = score // FOODS_PER_LEVEL + 1
            if new_level > level:
                level = new_level
                # Increase speed but cap at maximum
                current_speed = min(INITIAL_SPEED + (level - 1) * 2, MAX_SPEED)
                level_up_message = f"LEVEL {level}! Speed: {current_speed} FPS"
                level_up_timer = 60  # Show message for 60 frames (about 2 seconds)
        
        # Drawing section
        screen.fill(colorBLACK)  # Clear screen with black background
        draw_grid()  # Draw grid lines
        
        snake.draw()  # Draw snake
        food.draw()   # Draw food
        
        # Display score and level
        score_text = font.render(f"Score: {score}", True, colorWHITE)
        level_text = font.render(f"Level: {level}", True, colorWHITE)
        speed_text = font.render(f"Speed: {current_speed}", True, colorGRAY)
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
        screen.blit(speed_text, (10, 90))
        
        # Display level up message if active
        if level_up_timer > 0:
            level_up_surface = font.render(level_up_message, True, colorYELLOW)
            text_rect = level_up_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(level_up_surface, text_rect)
            level_up_timer -= 1
        
        # Instructions text
        controls_text = font.render("Arrow Keys: Move | P: Pause", True, colorGRAY)
        screen.blit(controls_text, (10, HEIGHT - 30))
        
        # Update display and control game speed
        pygame.display.flip()
        clock.tick(current_speed)
    
    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()