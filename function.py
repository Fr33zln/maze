from data import *





class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height)
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
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"up": False, "down": False, "left":False,"right":False}
        self.side = False
        self.hp = hp
        

    def move(self, window):
        if self.walk["up"] and self.y > 0:
            self.y -= self.step
            if self.collidelist(wall_list) != -1:
                self.y += self.step
        if self.walk["down"] and self.y < size_window[1]:
            self.y += self.step
            if self.collidelist(wall_list) != -1:
                self.y -= self.step
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
            if self.collidelist(wall_list) != -1:
                self.x += self.step
            self.side = True
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step
            if self.collidelist(wall_list) != -1:
                self.x -= self.step
            self.side = False

        for value in list(self.walk.values()):
            if value:
                self.move_image()
                break
        else:
            self.image = self.image_list[0]
        if self.side:
            self.image_now = pygame.transform.flip(self.image, True , False)
        else:
            self.image_now = self.image

        self.move_image()
        window.blit(self.image_now, (self.x,self.y))






class Bot(Human):
    def __init__(self,x,y,width,height,image_list,step,orientation, radius = 0):
        super().__init__(x,y,width,height,image_list,step)
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.radius = radius
        if self.orientation.find("left") != 1:
            index = 0
            while index <len(self.image_list):
                self.image_list[index] = pygame.transform.flip(self.image_list[index],True, False)
                index +=1         
     

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

    



    def striker(self,window,bullet):
        self.move_image()
        window.blit(self.image, (self.x, self.y))
        bullet.move(window)



    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =- 1
            hero.x = hero.start_x
            hero.y = hero.start_y

class Bullet(pygame.Rect):
    def __init__(self,x,y,width,height,color,orientation,step,image = None):
        super().__init__(x,y,width,height)
        self.color = color
        self.image = image
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.step = step


    def move(self, window):
        if self.orientation.find('vertical') != -1:
            self.y += self.step
            if self.y < 0 or self.y > size_window[1] or self.collidelist(wall_list) != -1:
                self.y = self.start_y
        elif self.orientation.find('horizontal') != -1:
            self.x += self.step
            if self.x < 0 or self.x > size_window[1] or self.collidelist(wall_list) != -1:
                self.x = self.start_x
        pygame.draw.rect(window,self.color,self)


    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =- 1
            bullet_image_list.remove(self)


class Heart(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        
    def blit(self,window):
        window.blit(self.image, (self.x,self.y))

    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =+ 1
            heart_list.remove(self)



class Well(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        
    def blit(self,window):
        window.blit(self.image, (self.x,self.y))




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
