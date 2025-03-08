from function import *


window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()


hero = Hero(
    10,
    10,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    1,
    2
)

bot1 = Bot(
    300,
    210,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    -3,
    "vertical-down",
    radius = 200,
)



#bot2 = Bot(
    #300,
    #200,
    #size_hero[0],
    #size_hero[1],
    #bot2_image_list.copy,
    #-3,
    #"vertical-down",
    #radius = 200,
#)
#bot7 = Bot(
#    300,
#    200,
#    size_hero[0],
#    size_hero[1],
#    bot1_image_list,
#    -3,
#    "horizontal"
#)

#bullet7 = Bullet(bot7.x,
#                 bot7.y,
#                 20, 20,
#                 #RED,
#                 bot7.orientation,
#                 5)


heart_list.append(Heart(150,150,50, 50, heart_image_list))





game = True
while game:
    events = pygame.event.get()
    window.fill(BLACK)

#    x,y = 0,0
#    for i in range(100):
#        pygame.draw.line(window, WHITE, (0, y), (size_window[0],y))
#        pygame.draw.line(window, WHITE, (x, 0), (x, size_window[1]))
#        x += 10
#        y += 10

    hero.move(window)
    bot1.guardian(window)
    for heart in heart_list:
        heart.blit(window)



    for wall in wall_list:
        pygame.draw.rect(window, wall.color, wall)
        #print(wall.x,wall.y)


    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
            if event.key == pygame.K_a:
                hero.walk["left"] = True
            if event.key == pygame.K_s:
                hero.walk["down"] = True
            if event.key == pygame.K_d:
                hero.walk["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False
            if event.key == pygame.K_a:
                hero.walk["left"] = False
            if event.key == pygame.K_s:
                hero.walk["down"] = False
            if event.key== pygame.K_d:
                hero.walk["right"] = False

    clock.tick(FPS)
    pygame.display.flip()
