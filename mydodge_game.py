# Name: Matthew Decker
# Date: 5/18/26
# Pygame Dodge Game 
"""
Student Skeleton: Pygame Dodge Game
Follow the README steps and fill in or customize each TODO section.
"""

import pygame
import random


pygame.init()


WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")


clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 255)
RED = (255, 60, 60)


player_width = 60
player_height = 60
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 90
player_speed = 7
lives = 3


object_width = 50
object_height = 50
object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height
object_speed = 5


object2_x = random.randint(0, WIDTH - object_width)
object2_y = -200
object2_speed = 6

object3_x = random.randint(0, WIDTH - object_width)
object3_y = -400
object3_speed = 7


score = 0
font = pygame.font.SysFont(None, 36)
running = True
game_over = False


while running:
    clock.tick(FPS)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                game_over = False
                score = 0
                lives = 3
                player_x = WIDTH // 2 - player_width // 2
                
                
                object_y = -object_height
                object_x = random.randint(0, WIDTH - object_width)
                
                
                object2_y = -200
                object2_x = random.randint(0, WIDTH - object_width)
                
                
                object3_y = -400
                object3_x = random.randint(0, WIDTH - object_width)

    
    if not game_over:
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            
        
        if player_x < 0:
            player_x = 0
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width
            
        
        current_obj_speed = object_speed + (score // 5)
        current_obj2_speed = object2_speed + (score // 5)
        current_obj3_speed = object3_speed + (score // 5)

        
        object_y += current_obj_speed
        object2_y += current_obj2_speed
        object3_y += current_obj3_speed
        
        
        if object_y > HEIGHT:
            object_y = -object_height
            object_x = random.randint(0, WIDTH - object_width)
            score += 1
            
        
        if object2_y > HEIGHT:
            object2_y = -object_height
            object2_x = random.randint(0, WIDTH - object_width)
            score += 1
            
        
        if object3_y > HEIGHT:
            object3_y = -object_height
            object3_x = random.randint(0, WIDTH - object_width)
            score += 1

        
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
        object2_rect = pygame.Rect(object2_x, object2_y, object_width, object_height)
        object3_rect = pygame.Rect(object3_x, object3_y, object_width, object_height)

        
        if player_rect.colliderect(object_rect):
            lives -= 1
            object_y = -object_height
            object_x = random.randint(0, WIDTH - object_width)
            
        if player_rect.colliderect(object2_rect):
            lives -= 1
            object2_y = -object_height
            object2_x = random.randint(0, WIDTH - object_width)
            
        if player_rect.colliderect(object3_rect):
            lives -= 1
            object3_y = -object_height
            object3_x = random.randint(0, WIDTH - object_width)
            
        
        if lives <= 0:
            game_over = True

    
    screen.fill(WHITE)
    
    
    if not game_over:
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))
        pygame.draw.rect(screen, RED, (object2_x, object2_y, object_width, object_height))
        pygame.draw.rect(screen, RED, (object3_x, object3_y, object_width, object_height))

    
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 60))

    
    if game_over:
        game_over_text = font.render("GAME OVER", True, BLACK)
        restart_text = font.render("Press R to restart.", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 2 - 110, HEIGHT // 2 + 10))

    pygame.display.update()

pygame.quit()
