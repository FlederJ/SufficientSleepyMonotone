import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)


class Ball:

    def __init__(self):
        self.image = pygame.image.load("small_tennis.png")
        self.speed = [0, 1]
        self.rect = self.image.get_rect()

    def update(self):
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ball = Ball()

    while True:
        screen.fill(BACKGROUND)
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
