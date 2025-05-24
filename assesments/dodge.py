import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBJECT_WIDTH, OBJECT_HEIGHT = 50, 50
INITIAL_FALL_SPEED = 5
FALL_SPEED_INCREASE = 0.5
LIVES = 3


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 8
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 8


class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - OBJECT_WIDTH), 0))

    def update(self, fall_speed):
        self.rect.y += fall_speed
        if self.rect.top > HEIGHT:
            self.kill() 

def main():
    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    falling_objects = pygame.sprite.Group()
    clock = pygame.time.Clock()
    fall_speed = INITIAL_FALL_SPEED
    score = 0
    lives = LIVES

    while lives > 0:
        screen.fill(WHITE)

   
        if random.randint(1, 30) == 1:
            falling_objects.add(FallingObject())

   
        player_group.update()
        falling_objects.update(fall_speed)


        if pygame.sprite.spritecollideany(player, falling_objects):
            lives -= 1
            falling_objects.empty() 

        
        player_group.draw(screen)
        falling_objects.draw(screen)

       
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        lives_text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))

 
        fall_speed += FALL_SPEED_INCREASE * (score // 10) 
        score += 1 

        pygame.display.flip()
        clock.tick(60)

    
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2 - 20))
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
