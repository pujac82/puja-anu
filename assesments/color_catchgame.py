import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Catch Game")


COLORS = {"RED": (220, 20, 60), "GREEN": (0, 200, 0), "BLUE": (30, 144, 255), "YELLOW": (255, 215, 0), "PURPLE": (138, 43, 226)}
BLOCK_SIZE = 40
FALL_SPEED = 5
BUCKET_WIDTH, BUCKET_HEIGHT = 100, 20
font = pygame.font.SysFont(None, 36)

class Block:
    def __init__(self, x, color):
        self.x, self.y, self.color = x, -BLOCK_SIZE, color
    def fall(self):
        self.y += FALL_SPEED
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

def main():
    bucket_x = WIDTH // 2 - BUCKET_WIDTH // 2
    target_color = random.choice(list(COLORS.keys()))
    score = 0
    blocks = []
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))
        if random.randint(0, 30) == 0:
            x = random.randint(0, WIDTH - BLOCK_SIZE)
            color = random.choice(list(COLORS.values()))
            blocks.append(Block(x, color))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bucket_x = max(bucket_x - 8, 0)
        if keys[pygame.K_RIGHT]:
            bucket_x = min(bucket_x + 8, WIDTH - BUCKET_WIDTH)

        for block in blocks[:]:
            block.fall()
            block.draw()
            if (block.y + BLOCK_SIZE >= HEIGHT - BUCKET_HEIGHT and
                bucket_x < block.x + BLOCK_SIZE and
                bucket_x + BUCKET_WIDTH > block.x):
                if block.color == COLORS[target_color]:
                    score += 1
                blocks.remove(block)

        blocks = [b for b in blocks if b.y < HEIGHT]

        pygame.draw.rect(screen, (0, 0, 0), (bucket_x, HEIGHT - BUCKET_HEIGHT - 10, BUCKET_WIDTH, BUCKET_HEIGHT))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        target_text = font.render(f"Catch: {target_color}", True, COLORS[target_color])
        screen.blit(score_text, (10, 10))
        screen.blit(target_text, (WIDTH - 180, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
