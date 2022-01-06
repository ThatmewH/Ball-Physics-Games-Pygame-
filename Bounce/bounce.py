import pygame
pygame.init()
width = 1000
height = 600
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def circleOverlap(pos1, radius, mousePos):
    if abs(pos1[0] - mousePos[0]) < radius and abs(pos1[1] - mousePos[1] < radius):
        return True
def rectOverlap(circlePos, radius, rectangle):
    if circlePos[0] + radius > rectangle[0] and circlePos[0] - radius < rectangle[0] + rectangle[2] and circlePos[1] + radius > rectangle[1] and circlePos[1] - radius < rectangle[1] + rectangle[3]:
        if ball.y + abs(ball.dy) + ball.radius > rectangle[1] + rectangle[3]:
            print((rectangle[1] + rectangle[3]) - (ball.y + abs(ball.dy) + ball.radius))
            ball.dy *= -1 # Bottom
            ball.y = rectangle[1] + rectangle[3] + ball.radius
            print("Bottom")
        elif ball.x - abs(ball.dx) - ball.radius < rectangle[0]:
            ball.dx *= -1 # Left
            ball.x = rectangle[0] - ball.radius
            print("Left")
        elif ball.x + abs(ball.dx) + ball.radius > rectangle[0] + rectangle[2]:
            ball.dx *= -1 # Right
            ball.x = rectangle[0] + rectangle[2] + ball.radius
            print("RIGHT")
        elif ball.y - abs(ball.dy) - radius < rectangle[1]:
            # ball.isFalling = False
            # ball.dx = 0
            ball.dy *= -1
            ball.y = rectangle[1] - radius
class Rectangle:
    def __init__(self, x, y, width, height):
        self.pos = (x,y)
        self.width = width
        self.height = height
    def update(self):
        pygame.draw.rect(win, (0,0,100), (self.pos[0],self.pos[1],self.width,self.height))
class Ball:
    def __init__(self):
        self.radius = 10
        self.gravity = -1
        self.x = int(width/2)
        self.y = int(height*0.1)
        self.dy = 0
        self.dx = 0
        self.isFalling = True
        self.clickMode = False
        self.friction = -0.25
        self.rightClickMode = False
    def update(self):
        if self.clickMode:
            pygame.draw.line(win, (255,0,0), (self.x,self.y), pygame.mouse.get_pos())
        elif self.rightClickMode:
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]
        else:
            # If ball is touching ground
            if self.y + self.radius > height:
                self.isFalling = False
                self.y = height - self.radius
                self.dx = 0
            # If ball is touching roof
            elif self.y - self.radius < 0:
                self.y = 0 + self.radius
                self.dy = int(self.dy * self.friction)
            # If ball is touching right side
            elif self.x + self.radius > width:
                self.x = width - self.radius
                self.dx = int(self.dx * self.friction)
            # If ball is touching left side
            elif self.x - self.radius < 0:
                self.x = 0 + self.radius
                self.dx = int(self.dx * self.friction)
            # If ball is falling
            if self.isFalling:
                self.dy -= self.gravity
                self.y += self.dy
            self.x += self.dx
            # If ball is touching rectangle
            for rectangle in rectangles:
                rectOverlap((ball.x + ball.dx, ball.y + ball.dy), ball.radius, (rectangle.pos[0], rectangle.pos[1], rectangle.width, rectangle.height))
        pygame.draw.circle(win, (200,200,200), (self.x,self.y), self.radius)
    def launch(self, mousePos):
        self.dy = int((mousePos[1] - self.y) * 0.1)
        self.dx = int((mousePos[0] - self.x) * 0.1)
        ball.isFalling = True
ball = Ball()
rectangles = [Rectangle(100, 100, 400, 50), Rectangle(450, 400, 400, 100)]
while True:
    clock.tick(60)
    win.fill((50,50,50))
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if circleOverlap((ball.x, ball.y), ball.radius, pygame.mouse.get_pos()):
                ball.clickMode = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if circleOverlap((ball.x, ball.y), ball.radius, pygame.mouse.get_pos()):
                ball.clickMode = False
                ball.rightClickMode = True
        if event.type == pygame.MOUSEBUTTONUP:
            if ball.clickMode == True:
                ball.clickMode = False
                ball.launch(pygame.mouse.get_pos())
            elif ball.rightClickMode == True:
                ball.rightClickMode = False
                ball.isFalling = True
    # Draw rectangles
    for rectangle in rectangles:
        rectangle.update()
    # Draw ball
    ball.update()
    pygame.display.update()
