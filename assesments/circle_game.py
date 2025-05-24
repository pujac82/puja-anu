import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Circle Game")

WHITE, RED, BLACK = (255, 255, 255), (220, 20, 60), (0, 0, 0)
RADIUS = 30
font = pygame.font.SysFont(None, 36)
score = 0
circle_pos = (random.randint(RADIUS, WIDTH - RADIUS), random.randint(RADIUS, HEIGHT - RADIUS))

def draw_circle(pos): pygame.draw.circle(screen, RED, pos, RADIUS)
def draw_score(score): screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
def is_inside_circle(mouse_pos): return (mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2 <= RADIUS ** 2

def main():
    global score, circle_pos
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        draw_circle(circle_pos)
        draw_score(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and is_inside_circle(event.pos):
                score += 1
                circle_pos = (random.randint(RADIUS, WIDTH - RADIUS), random.randint(RADIUS, HEIGHT - RADIUS))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__": main()
