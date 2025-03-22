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
    100,
    335,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    1,
    "vertical",
    radius = 105,
)

bot2 = Bot(
    775,
    435,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    1,
    "horizontal",
    radius = 140,
)

bot3 = Bot(
    495,
    12,
    size_hero[0],
    size_hero[1],
    bot2_image_list,
    2,
    "horizontal",
    radius = 120,
)

bot4 = Bot(
    100,
    10,
    size_hero[0],
    size_hero[1],
    bot3_image_list,
    2,
    "vertical",
    radius = 120,
)
bullet4= Bullet(bot4.x+17,
                 bot4.y,
                 20, 20,
                 WHITE,
                 bot4.orientation,
                 1)


bot5 = Bot(
    780,
    170,
    size_hero[0],
    size_hero[1],
    bot3_image_list,
    2,
    "horizontal",
    radius = 120,
)
bullet5= Bullet(bot5.x+20,
                 bot5.y+7,
                 20, 20,
                 WHITE,
                 bot5.orientation,
                 1)

bot6 = Bot(
    590,
    350,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    1,
    "horizontal",
    radius = 130,
)

bot7 = Bot(
    690,
    170,
    size_hero[0],
    size_hero[1],
    bot2_image_list,
    2,
    "vertical",
    radius = 100,
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


heart_list.append(Heart(290,255,50, 50, heart_image_list))
heart_list.append(Heart(390,80,50, 50, heart_image_list))
well_list.append(Well(700,10,50, 50, well_image_list))

font = pygame.font.Font(None, 40)

game = True
while game:
    events = pygame.event.get()
    window.fill(BLACK)
    window.blit(heart_image_list, (3,3))
    render_hp = font.render(f"x{hero.hp}", True, BLACK)
    window.blit(render_hp, (22,3))
#    x,y = 0,0
#    for i in range(100):
#        pygame.draw.line(window, WHITE, (0, y), (size_window[0],y))
#        pygame.draw.line(window, WHITE, (x, 0), (x, size_window[1]))
#        x += 10
#        y += 10

    hero.move(window)
    bot1.guardian(window)
    bot2.guardian(window)
    bot3.guardian(window)
    bot4.striker(window, bullet4)
    bot5.striker(window, bullet5)
    bot6.guardian(window)
    bot7.guardian(window)


    hero.collide_enemy([bot1, bot2, bot3, bot4, bot5, bot6, bot7, bullet4, bullet5])
    hero.collide_heart(heart_list)


    for heart in heart_list:
        heart.blit(window)
        
    for well in well_list:
        well.blit(window)

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
