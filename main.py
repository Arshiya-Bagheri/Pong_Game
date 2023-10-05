import pygame, sys, random
from settings import *


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.title = pygame.display.set_caption('Pong Game')
        self.clock = pygame.time.Clock()

        self.ball_speed_x = 7
        self.ball_speed_y = 7
        self.player_speed = 0
        self.oppenent_speed = 7
        self.player_scores = 0
        self.oppenent_scores = 0
        self.ball = pygame.Rect(WIDTH/2-15 ,HEIGHT/2-15,30,30)
        self.player = pygame.Rect(WIDTH-20,HEIGHT/2 - 70,10,140)
        self.oppenent = pygame.Rect(10,HEIGHT/2 - 70, 10,140)
        self.bg_color = pygame.Color('black')
        self.text_font = pygame.font.SysFont('Arial', 30)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed +=7
                    if event.key ==pygame.K_UP:
                        self.player_speed -=7

                if event.type==pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed -=7
                    if event.key ==pygame.K_UP:
                        self.player_speed +=7

            
            

            self.screen.fill(self.bg_color)
            self.ball_animation()
            self.player_animation()
            self.oppenent_animation()
            self.point = self.text_font.render(f'{self.oppenent_scores}  {self.player_scores}', True, 'white')
            self.screen.blit(self.point, (WIDTH/2 - 20, 30) )
            
            
            pygame.draw.rect(self.screen, 'white', self.player)
            pygame.draw.rect(self.screen, 'white', self.oppenent)
            pygame.draw.ellipse(self.screen,'white', self.ball)
            pygame.draw.aaline(self.screen, 'white', (WIDTH/2,0), (WIDTH/2, HEIGHT))
            pygame.display.flip()
            self.clock.tick(60)

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y +=self.ball_speed_y
        
        if self.ball.top<=0 or self.ball.bottom >= HEIGHT:
            self.ball_speed_y *= -1
        
        if self.ball.left<=0:
            self.player_scores +=1
            self.ball_restart()
    
        if self.ball.right >= WIDTH:
            self.oppenent_scores +=1
            self.ball_restart()
                    
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.oppenent):
            self.ball_speed_x *=-1

    def ball_restart(self):
        self.ball.center = (WIDTH/2, HEIGHT/2)
        self.ball_speed_y *= random.choice((1,-1))
        self.ball_speed_x *= random.choice((1,-1))

    def player_animation(self):
        self.player.y += self.player_speed
        if self.player.top <=0:
            self.player.top = 0
        if self.player.bottom >= HEIGHT:
            self.player.bottom = HEIGHT

    def oppenent_animation(self):
        if self.oppenent.top < self.ball.y:
            self.oppenent.top +=self.oppenent_speed
        if self.oppenent.bottom >self.ball.y:
            self.oppenent.bottom -= self.oppenent_speed
        
        if self.oppenent.top <=0:
            self.oppenent.top = 0
        if self.oppenent.bottom >= HEIGHT:
            self.oppenent.bottom = HEIGHT
        

if __name__ == "__main__":
    game = Game()
    game.run()
