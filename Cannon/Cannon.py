import pygame, random, time, math
from pygame.locals import *
displayHeight = 500
displayWidth = 1000
DISPLAY = pygame.display.set_mode((displayWidth,displayHeight),0,32)
green = (0, 255, 0)
blue = (0, 0, 128)
class Cannon:
    def __init__(self):
        self.original_image = pygame.image.load("cannon.png").convert()
        self.image_clean = self.original_image.copy()
        self.x = 50
        self.y = displayHeight - 75
        self.rect = self.original_image.get_rect(center=(50, displayHeight - 75))
        self.angle = 0
    def update(self):
        self.original_image = pygame.transform.rotate(self.image_clean, self.angle)
        recta = self.original_image.get_rect(center=self.rect.center)
        DISPLAY.blit(self.original_image, (recta))

        mousePosDifference = (pygame.mouse.get_pos()[0] - self.x, pygame.mouse.get_pos()[1] - self.y)

        try:
            self.angle = int(math.degrees(math.atan(mousePosDifference[1]/mousePosDifference[0]))) * -1
        except:
            self.angle = int(math.degrees(math.atan(mousePosDifference[1]/1))) * -1
class Ball:
    def __init__(self, angle):
        self.radius = 20
        self.angle = angle
        self.angleRad = self.angle * math.pi / 180
        self.x = 50
        self.y = displayHeight - 75
        self.hypVelocity = 30
        self.dy = int(self.hypVelocity * math.sin(self.angleRad))
        self.dx = int(self.hypVelocity * math.cos(self.angleRad))
        self.positions = []
        self.moving = True
        self.trail = True
        self.alive = True
        self.createTime = int(time.time())
        self.currentTime = int(time.time())
        self.colour = [0,0,0]
    def update(self):
        if self.alive:
            self.currentTime = int(time.time())
            if self.trail:
                if self.moving:
                    self.positions.append((self.x, self.y))
            pygame.draw.circle(DISPLAY, self.colour, (self.x,self.y), self.radius)
            self.y -= self.dy
            self.x += self.dx
            self.dy -= 1
            if self.y + self.radius >= displayHeight:
                self.dy = int(self.dy * -0.7)
                self.dx = int(self.dx * 0.99)
                self.dy += -1
                self.y = displayHeight - self.radius

                # self.dy = 0
                # self.dx = 0
                # self.alive = False
                self.y = displayHeight - self.radius
            if self.x + self.radius > displayWidth or self.x - self.radius < 0:
                self.dx *= -1

                # self.dx = 0
                # self.dy = 0
                # self.alive = False
            if abs(self.dx) == 0 and abs(self.dy) == 0:
                self.moving = False

            if self.trail:
                for x in range(0, len(self.positions) - 1, 3):
                    pygame.draw.circle(DISPLAY, (0,0,0), self.positions[x], 3)
                    # pygame.draw.line(DISPLAY, (0,0,0), self.positions[x], self.positions[x+1], 1)
            if self.currentTime - self.createTime > 5:
                self.alive = False
def main():
    balls = []
    pygame.init()
    cannon = Cannon()
    font = pygame.font.Font('freesansbold.ttf', 32)
    while True:
        text = font.render(str(cannon.angle) + "°", True, (0,0,0), (255,255,255))
        DISPLAY.fill((255,255,255))
        keystate = pygame.key.get_pressed()
        if keystate[K_DOWN]:
            cannon.angle -= 1
        if keystate[K_UP]:
            cannon.angle += 1

        # Get Mouse Held Down // Rapid Fire
        # if pygame.mouse.get_pressed()[0]:
        #     balls.append(Ball(cannon.angle))

        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if event.button == 1:
                    balls.append(Ball(cannon.angle))
            if event.type==QUIT:
                pygame.quit()
                exit()

        for ball in balls:
            ball.update()
            if ball.alive == False:
                balls.remove(ball)
        cannon.update()
        DISPLAY.blit(text, (displayWidth-75, 0))
        pygame.display.flip()
        pygame.time.wait(10)
main()
