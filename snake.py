import pygame
import random
import tkinter.messagebox as text

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

game_over = False

coordinaty = []
coordinaty.append([300,400])
dlina = 1
x1_change = 0
y1_change = 0

x1_goal = random.randrange(10, 790, 10)
y1_goal = random.randrange(10, 490, 10)

clock =pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if coordinaty[-1][0]>=790 or coordinaty[-1][0]<10 or coordinaty[-1][1]>=490 or coordinaty[-1][1]<10:
        game_over = True
        text.showinfo('Конец игры', f'Вы набрали {dlina - 1} баллов')

    if coordinaty[-1] in coordinaty[0:-2]:
        game_over = True
        text.showinfo('Конец игры', f'Вы набрали {dlina - 1} баллов')
    if coordinaty[-1][0] == x1_goal and coordinaty[-1][1] == y1_goal:
        x1_goal = random.randrange(10, 780, 10)
        y1_goal = random.randrange(10, 480, 10)
        dlina += 1
        coordinaty.append([coordinaty[-1][0],coordinaty[-1][1]])
    for i in range(0, len(coordinaty)-1):
        coordinaty[i][0] = coordinaty[i+1][0]
        coordinaty[i][1] = coordinaty[i + 1][1]
    coordinaty[-1][0] += x1_change
    coordinaty[-1][1] += y1_change
    dis.fill(green)
    pygame.draw.rect(dis, black, (0, 0, 800, 500), 10)
    i = dlina-1
    while i != -1:
        pygame.draw.rect(dis, blue, [coordinaty[i][0], coordinaty[i][1], 10, 10])
        i -= 1
    pygame.draw.rect(dis, red, [x1_goal, y1_goal, 10, 10])
    pygame.display.update()

    clock.tick(15)

pygame = quit()
quit()
