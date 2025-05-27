import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Ball Through Horizontal Ring")
clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
BALL_COLOR = (30, 144, 255)
RING_COLOR = (0, 0, 0)
BACKGROUND = (240, 248, 255)


ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vel_y = 0
gravity = 0.3
jump_strength = -6


ring_gap_height = 180  
ring_speed = 3
wall_width = 60
rings = []


score = 0
font = pygame.font.SysFont(None, 36)


def spawn_ring():
    gap_y = random.randint(100, HEIGHT - 100)
    rings.append({"y": gap_y, "x": WIDTH, "passed": False})


spawn_ring()
ring_timer = 0


running = True
while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND)

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        ball_vel_y = jump_strength

 
    ball_vel_y += gravity
    ball_y += ball_vel_y

   
    if ball_y - ball_radius < 0:
        ball_y = ball_radius
        ball_vel_y = 0
    if ball_y + ball_radius > HEIGHT:
        running = False

   
    ring_timer += 1
    if ring_timer > 90:
        spawn_ring()
        ring_timer = 0

 
    for ring in rings:
        ring["x"] -= ring_speed

    for ring in rings:
        ring_x = ring["x"]
        gap_y = ring["y"]

     
        if not ring["passed"] and ring_x + wall_width < ball_x:
            score += 1
            ring["passed"] = True

     
        if ring_x < ball_x < ring_x + wall_width:
            if not (gap_y - ring_gap_height // 2 < ball_y < gap_y + ring_gap_height // 2):
                running = False

        if ring_x + wall_width < 0:
            rings.remove(ring)

     
        pygame.draw.rect(screen, RING_COLOR, (ring_x, 0, wall_width, gap_y - ring_gap_height // 2))
        pygame.draw.rect(screen, RING_COLOR, (ring_x, gap_y + ring_gap_height // 2, wall_width, HEIGHT - (gap_y + ring_gap_height // 2)))


    pygame.draw.circle(screen, BALL_COLOR, (ball_x, int(ball_y)), ball_radius)


    score_text = font.render(f"Score: {score}", True, (20, 20, 20))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit() 
sys.exit() 
