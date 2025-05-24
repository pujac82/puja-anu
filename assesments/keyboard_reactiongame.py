import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Keyboard Reaction Game")
font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)


arrow_keys = {
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN",
    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: "RIGHT"
}


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def game_loop():
    running = True
    score = 0
    round_time = 3 
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

     
        expected_key = random.choice(list(arrow_keys.keys()))
        direction = arrow_keys[expected_key]

        draw_text(f"Press {direction}", font, BLACK, 180, 150)
        pygame.display.flip()

        start_time = time.time()
        pressed = False
        correct = False

      
        while time.time() - start_time < round_time and not pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pressed = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == expected_key:
                        correct = True
                        score += 1
                    else:
                        correct = False
                    pressed = True

            clock.tick(60)

        
        screen.fill(WHITE)
        if pressed and correct:
            draw_text("Correct!", font, (0, 200, 0), 200, 150)
        else:
            draw_text("Wrong or Too Slow!", font, (200, 0, 0), 80, 150)
        draw_text(f"Score: {score}", small_font, BLACK, 250, 300)
        pygame.display.flip()
        pygame.time.delay(1000)

    pygame.quit()


game_loop()
