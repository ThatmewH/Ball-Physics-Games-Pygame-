import pygame, math
pygame.init()
win = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
class Spinner:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.radius = 5
        self.angle = 0
        self.angleDelay = a
        self.speed = 100
        self.size = 200
    def update(self):
        self.dx = int(math.cos((self.angle + self.angleDelay)/self.speed)*self.size) + self.x
        self.dy = int(math.sin((self.angle + self.angleDelay)/self.speed)*self.size) + self.y

        pygame.draw.circle(win, (255,255,255), (self.x+self.dx,self.y+self.dy), self.radius)
        self.angle += 1
spinners = []
for x in range(-20,125):
    spinners.append(Spinner(x*5, 100, x*0.6))

while True:
    pos = []
    win.fill((0,0,0))
    clock.tick(60)
    # for event in pygame.event.get():
    #     if event == pygame.QUIT():
    #         exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:

    # Draw Spinners

    # Draw lines
    for x in range(0,len(pos)):
        if x == (len(pos) - 1):
            break
        else:
            # redColour = 255 - abs(pos[x+1][0]-pos[x][0])*10
            # if redColour > 255:
            #     redColour = 255
            # if redColour < 0:
            #     redColour = 0
            pygame.draw.line(win, (255,255,255), pos[x], pos[x+1], 4)
    for x in range(0, len(spinners)):
        spinners[x].angleDelay += x/15
    for spinner in spinners:
        spinner.update()
        pos.append((spinner.x + spinner.dx, spinner.y + spinner.dy))

    pygame.display.update()
