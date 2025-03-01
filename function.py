from data import *





class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height, image_list, step)
        self.image_list = image_list
        self.image = self.image_list
        self.image_now = self.image
        self.image_count = 0
        self.step = step
    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count %10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count += 1

class Hero(Human):
    def __init__(self, x, y, width, height, image_list, step,hp):
        super().__init__(x, y, width, height, image_list, step)
        self.walk = {"up": False, "down":False,"right": False, "left": False}
        self.side = False
        

    def move(self, window):
        if self.walk["up"] and self.y > 0:
            self.y -=self.step


        self.move_image()
        window.blit(self.image, (self.x, self.y))





class Bot(Human):
    def __init__(self,x,y,width,height,image_list,step,orientation, radius = 0):
        super().__init__(x,y,width,height,image_list,step)
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.radius = radius

    def guardian(self,window):
        if self.orientation == "vertical":
            self.y += self.step
            if self.y  <self.start_y - self.radius or self.y > self.start_y + self.radius:
                self.step *= -1

        elif self.orientation == "horizontal":
            self.x += self.step
            if self.x  <self.start_x - self.radius or self.x > self.start_x + self.radius:
                self.step *= -1
        self.move_image()
        window.blit(self.image,(self.x,self.y))

    #def atacker


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
