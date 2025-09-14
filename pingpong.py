from pygame import *
window= display.set_mode((700,500))
back=(150,50,250)
window.fill(back)
display.set_caption('pingpong')
clock=time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y,player_width,player_high):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(player_width,player_high))
        self.player_speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def R(self):
        keys= key.get_pressed()
        if keys[K_UP] and self.rect.y> 5:
            self.rect.y-=self.player_speed
        if keys[K_DOWN] and self.rect.y<350:
            self.rect.y+=self.player_speed
    def L(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y> 5:
            self.rect.y-=self.player_speed
        if keys[K_s] and self.rect.y<350:
            self.rect.y+=self.player_speed


raketka1=Player('racket.png',2,650,250,30,150)
raketka2=Player('racket.png',2,30,250,30,150)
tmyachik=GameSprite('tenis_ball.png',3,320,250,50,50)

speed_x=3
speed_y=3
finish= False

font.init()
tekst=font.SysFont('Arial', 100)
lose1=tekst.render('player 1 lose',True,(46,35,67))
lose2=tekst.render('player 2 lose',True,(76,247,167))

      
game=True
while game==True:
    if finish!=True:
        window.fill(back)
        tmyachik.rect.x+=speed_x
        tmyachik.rect.y+=speed_y
        if tmyachik.rect.y>450 or tmyachik.rect.y<0:
            speed_y*=-1
        if sprite.collide_rect(raketka1,tmyachik) or sprite.collide_rect(raketka2,tmyachik):
            speed_x*=-1
        if tmyachik.rect.x<0:
            finish=True
            window.blit(lose1,(180,200))
        if tmyachik.rect.x>700:
            finish=True
            window.blit(lose2,(180,200))
        raketka1.reset()
        raketka1.R()
        raketka2.reset()
        raketka2.L()
        tmyachik.reset()
    for i in event.get():
        if i.type==QUIT:
            game=False
    display.update()
    clock.tick(60)
