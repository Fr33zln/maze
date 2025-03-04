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
    #5,
    5
)

bot1 = Bot(
    300,
    200,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    #-3,
    "vertical",
    radius = 200,
)





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
        if event.walk == pygame.K_s:
            hero.walk["down"] = True
        if event.walk == pygame.K_d:
            hero.walk["right"] = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            hero.walk["up"] = False
        if event.key == pygame.K_a:
            hero.walk["left"] = False
        if event.walk == pygame.K_s:
            hero.walk["down"] = False
        if event.walk == pygame.K_d:
            hero.walk["right"] = False

    clock.tick(FPS)
    pygame.display.flip()
