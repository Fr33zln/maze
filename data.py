import pygame
import os



pygame.init()

size_window = (995,500)
size_hero = (60,45)
size_hero = (60,45)
# 


BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 144
#15 15
wall_list = list()
heart_list = list()
abs_path = os.path.abspath(__file__ +"/..")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "noob_move2.png")), size_hero)
]
bot1_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_move2.png")), size_hero),
]
bot2_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_stand.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_move1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "zombie_fast_move2.png")), size_hero)
]
heart_image_list =pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "Images", "health.png")), size_hero)







#66 #33 
maps = {
    "LVL1":{
        "map":[
            "000001000000000001000000100000000000000000001000000000000000000000",
            "000001000000000001000000100000000000000000001000000000000000000000",
            "000001000000000001000000100000000000000000001000000000000000000000",
            "000001000000000001000000100000000000000000001000000000000000000000",
            "000001000000000001000000100000000000001111111111111111111111100000",
            "000001000000000000000000100000010000000000001000000000000000100000",
            "000001000000000000000000100000010000000000001000000000000000100000",
            "000001000000000000000000100000010000000000001000000000000000100000",
            "000001000000000000000000100000010000000000001000000000000000100000",
            "000001000001111111111111111111110000001000001000000111111111100000",
            "000000000000000000000000000000010000001000000000000100000000000000",
            "000000000000000000000000000000010000001000000000000100000000000000",
            "000000000000000000000000000000010000001000000000000100000000000000",
            "000000000000000000000000000000010000001000000000000100000000000000",
            "000000000000000000000000000000010000001000000000000100000000000000",
            "000001111111111111111111100000010000001111111000000111111111100000",
            "000001000000000000000000100000010000000000001000000000000000000000",
            "000001000000000000000000100000010000000000001000000000000000000000",
            "000001000000000000000000100000010000000000001000000000000000000000",
            "000001000000000000000000100000010000000000001000000000000000000000",
            "000001000000000000000000100000010000000000001000000000000000000000",
            "000001000001111111111111100000011111110000001111111111111111111111",
            "000001000000000000000000000000010000000000000000000100000000000000",
            "000001000000000000000000000000010000000000000000000100000000000000",
            "000001000000000000000000000000010000000000000000000100000000000000",
            "000001000000000000000000000000010000000000000000000100000000000000",
            "000001000000000000000000000000010000000000000000000100000000000000",
            "000001000001111111111111111111110000001111110000000100000111111111",
            "000001000000000000000000000000000000000000010000000000000000000000",
            "000001000000000000000000000000000000000000010000000000000000000000",
            "000001000000000000000000000000000000000000010000000000000000000000",
            "000001000000000000000000000000000000000000010000000000000000000000",
            "000001000000000000000000000000000000000000010000000000000000000000"
            ]

    }
}
