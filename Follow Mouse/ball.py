import pygame, math, random, time

class Ball:
    def __init__(self, x ,y, velX, velY, accX=0, accY=0):
        self.x = x
        self.y = y

        self.velX = velX
        self.velY = velY

        self.accX = accX
        self.accY = accY

        self.angle = 0

        self.colour = [1,1,1]
        self.colourPos = random.randint(0,2)
        self.colourInc = 1

        self.randomXConst = random.randint(-5, 5)
        self.randomYConst = random.randint(-5, 5)

        self.limit = True
        self.lastLimitTime = time.time()

        self.radius = random.randint(1,10)
        self.radiusInc = 0.01
    def update(self, mousePos):

        self.angle = math.atan2(mousePos[1] - self.y, mousePos[0] - self.x)
        self.dist = math.sqrt((mousePos[1] - self.y)**2 + (mousePos[0] - self.x)**2)

        self.accX = self.dist*math.cos(self.angle)
        self.accY = self.dist*math.sin(self.angle)
        self.limitAccel(0.1)

        self.velX += self.accX + random.choice([-0.3,0.3])
        self.velY += self.accY + random.choice([-0.3,0.3])

        if self.limit:
            self.limitVel(5)
        if time.time() - self.lastLimitTime > 1:
            self.limit = True
        self.x += self.velX
        self.y += self.velY

        self.changeColour = random.choice([False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True])
        self.colour[self.colourPos] += self.colourInc
        if self.changeColour:

            self.colourPos = random.randint(0,2)
        if self.colour[self.colourPos] >= 255 or self.colour[self.colourPos] <= 0:
            self.colourPos = random.randint(0,2)
            if self.colour[self.colourPos] >= 255:
                self.colourInc = -1
            elif self.colour[self.colourPos] <= 0:
                self.colourInc = 1

        self.radius += self.radiusInc
        if self.radius >= 20 or self.radius <= 0:
            self.radiusInc = -self.radiusInc
    def draw(self, win):
        pygame.draw.circle(win, self.colour, (int(self.x), int(self.y)), int(self.radius))
        # pygame.draw.line(win, (255,255,0), (self.x, self.y), pygame.mouse.get_pos(), 1)

    def limitVel(self, velLimit):
        if self.velX > velLimit:
            self.velX = velLimit
        if self.velY > velLimit:
            self.velY = velLimit
        if self.velX < -velLimit:
            self.velX = -velLimit
        if self.velY < -velLimit:
            self.velY = -velLimit
    def limitAccel(self, accLimit):
        if self.accX > accLimit:
            self.accX = accLimit
        if self.accY > accLimit:
            self.accY = accLimit
        if self.accX < -accLimit:
            self.accX = -accLimit
        if self.accY < -accLimit:
            self.accY = -accLimit
