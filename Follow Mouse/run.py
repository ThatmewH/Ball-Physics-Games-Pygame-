import ball, pygame, random, time
pygame.init()

width = 1920
height = 1080


win = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
balls = []
for x in range(0,100):
    balls.append(ball.Ball(random.randint(0, width),random.randint(0,height),0,0,0,0))
s = pygame.Surface((width,height))
s.set_alpha(50)
s.fill((0,0,0))
while True:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.limit = False
                ball.lastLimitTime = time.time()
                ball.velX += random.randint(-10,10)
                ball.velY += random.randint(-10,10)
    for ball in balls:
        ball.update(pygame.mouse.get_pos())
        ball.draw(win)

    # win.blit(s, (0,0))
    pygame.display.update()
    clock.tick(120)
