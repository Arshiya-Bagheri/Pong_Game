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
        self.right_line = WIDTH-20
        self.left_line = 10
        self.destination = -1
        self.ball = pygame.Rect(WIDTH/2-15, HEIGHT/2-15, 30, 30)
        self.player = pygame.Rect(self.right_line, HEIGHT/2 - 70, 10, 140)
        self.oppenent = pygame.Rect(self.left_line, HEIGHT/2 - 70, 10, 140)
        self.bg_color = pygame.Color('black')
        self.text_font = pygame.font.SysFont('Arial', 30)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed += 7
                    if event.key == pygame.K_UP:
                        self.player_speed -= 7

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed -= 7
                    if event.key == pygame.K_UP:
                        self.player_speed += 7

            
            

            self.screen.fill(self.bg_color)
            self.ball_animation()
            self.player_animation()
            self.predict_ball_destination()
            self.oppenent_animation()
            self.point = self.text_font.render(f'{self.oppenent_scores}  {self.player_scores}', True, 'white')
            self.screen.blit(self.point, (WIDTH/2 - 20, 30) )
            
            
            pygame.draw.rect(self.screen, 'white', self.player)
            pygame.draw.rect(self.screen, 'white', self.oppenent)
            pygame.draw.ellipse(self.screen,'white', self.ball)
            pygame.draw.aaline(self.screen, 'white', (WIDTH/2, 0), (WIDTH/2, HEIGHT))
            pygame.display.flip()
            self.clock.tick(60)

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y
        
        if self.ball.top <= 0 or self.ball.bottom >= HEIGHT:
            self.ball_speed_y *= -1
        
        if self.ball.left <= self.left_line:
            self.player_scores += 1
            self.ball_restart()
    
        if self.ball.right >= self.right_line + 5:
            self.oppenent_scores += 1
            self.ball_restart()
                    
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.oppenent):
            self.ball_speed_x *= -1
        
        if self.ball.colliderect(self.oppenent):
            self.reset_destination()

    def ball_restart(self):
        self.ball.center = (WIDTH/2, HEIGHT/2)
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))
        self.reset_destination()

    def player_animation(self):
        self.player.y += self.player_speed
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= HEIGHT:
            self.player.bottom = HEIGHT
    
    def predict_ball_destination(self):
        if self.destination != -1:
            return
        
        ball_top = self.ball.top
        ball_bottom = self.ball.bottom
        ball_right = self.ball.right
        ball_left = self.ball.left
        ball_speed_x = self.ball_speed_x
        ball_speed_y = self.ball_speed_y

        while True:
            ball_top += ball_speed_y
            ball_bottom += ball_speed_y

            ball_right += ball_speed_x
            ball_left += ball_speed_x
            
            if ball_top <= 0 or ball_bottom >= HEIGHT:
                ball_speed_y *= -1
            
            if ball_right >= self.player.left:
                ball_speed_x *= -1

            if ball_left <= self.left_line:
                self.destination = (ball_top + ball_bottom) // 2
                return
    
    def oppenent_animation(self):
        if self.destination == -1:
            return
        
        if (self.oppenent.top * 2 + self.oppenent.bottom) // 3 < self.destination:
            self.oppenent.top += self.oppenent_speed
        if (self.oppenent.top + self.oppenent.bottom * 2) // 3 > self.destination:
            self.oppenent.top -= self.oppenent_speed
        
        if self.oppenent.top <= 0:
            self.oppenent.top = 0
        if self.oppenent.bottom >= HEIGHT:
            self.oppenent.bottom = HEIGHT
    
    def reset_destination(self):
        self.destination = -1
        

if __name__ == "__main__":
    game = Game()
    game.run()
