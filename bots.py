# BOTH PLAYERS ARE BOTS
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
        self.oppenent1_speed = 7
        self.oppenent2_speed = 7
        self.oppenent2_scores = 0
        self.oppenent1_scores = 0
        self.right_line = WIDTH-20
        self.left_line = 10
        self.ball = pygame.Rect(WIDTH/2-15 ,HEIGHT/2-15,30,30)
        self.oppenent2 = pygame.Rect(self.right_line, HEIGHT/2 - 70, 10, 140)
        self.oppenent1 = pygame.Rect(self.left_line, HEIGHT/2 - 70, 10, 140)
        self.bg_color = pygame.Color('black')
        self.text_font = pygame.font.SysFont('Arial', 30)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill(self.bg_color)
            self.ball_animation()
            self.oppenent2_animation()
            self.oppenent1_animation()
            self.point = self.text_font.render(f'{self.oppenent1_scores}  {self.oppenent2_scores}', True, 'white')
            self.screen.blit(self.point, (WIDTH/2 - 20, 30) )
            pygame.draw.rect(self.screen, 'white', self.oppenent1)
            pygame.draw.rect(self.screen, 'white', self.oppenent2)
            pygame.draw.ellipse(self.screen,'white', self.ball)
            pygame.draw.aaline(self.screen, 'white', (WIDTH/2,0), (WIDTH/2, HEIGHT))
            pygame.display.update()
            self.clock.tick(60)

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y +=self.ball_speed_y
        
        if self.ball.top<=0 or self.ball.bottom >= HEIGHT:
            self.ball_speed_y *= -1
        
        if self.ball.left <= self.left_line:
            self.oppenent2_scores +=1
            self.ball_restart()
    
        if self.ball.right >= self.right_line + 5:
            self.oppenent1_scores +=1
            self.ball_restart()

        if self.ball.colliderect(self.oppenent2) or self.ball.colliderect(self.oppenent1):
            self.ball_speed_x *=-1

    def ball_restart(self):
        self.ball.center = (WIDTH/2, HEIGHT/2)
        self.ball_speed_y *= random.choice((1,-1))
        self.ball_speed_x *= random.choice((1,-1))

    def oppenent2_animation(self):
        if self.oppenent2.top < self.ball.y:
            self.oppenent2.top +=self.oppenent2_speed
        if self.oppenent2.bottom >self.ball.y:
            self.oppenent2.bottom -= self.oppenent2_speed

        if self.oppenent2.top <=0:
            self.oppenent2.top = 0
        if self.oppenent2.bottom >= HEIGHT:
            self.oppenent2.bottom = HEIGHT

    def oppenent1_animation(self):
        if self.oppenent1.top < self.ball.y:
            self.oppenent1.top +=self.oppenent1_speed
        if self.oppenent1.bottom >self.ball.y:
            self.oppenent1.bottom -= self.oppenent1_speed
        
        if self.oppenent1.top <=0:
            self.oppenent1.top = 0
        if self.oppenent1.bottom >= HEIGHT:
            self.oppenent1.bottom = HEIGHT

if __name__ == "__main__":
    game = Game()
    game.run()
