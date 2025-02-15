from data import *











class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color

def create_wall(new_map):
    x,y = 0,0
    width,height = 15,15
    for line in new_map:
        for elem in line:
            if elem == "1":
                wall_list.append(Wall(x,y,width,height,WHITE))
            x += width
        x = 0
        y += height

create_wall(maps["LVL1"]["map"])
#print(len(wall_list))
