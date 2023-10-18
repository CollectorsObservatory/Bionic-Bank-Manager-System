import pygame, sys, time, random

class SnakeGame:
    def __init__(self):
        self.difficulty = 25
        self.frame_size_x = 720
        self.frame_size_y = 480
        pygame.init()
        pygame.display.set_caption('Snake Eater')
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))
        self.fps_controller = pygame.time.Clock()
        self.score = 0
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.frame_size_x/2, self.frame_size_y/4)
        self.game_window.fill(self.black)
        self.game_window.blit(game_over_surface, game_over_rect)
        self.show_score(0, self.red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        self.main_window.deiconify()

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.frame_size_x/10, 15)
        else:
            score_rect.midtop = (self.frame_size_x/2, self.frame_size_y/1.25)
        self.game_window.blit(score_surface, score_rect)

    def run(self):
        snake_pos = [100, 50]
        snake_body = [[100, 50],
                      [100-10, 50],
                      [100-(2*10), 50]]
        food_pos = [random.randrange(1, self.frame_size_x//10) * 10,
                    random.randrange(1, self.frame_size_y//10) * 10]
        food_spawn = True
        direction = 'RIGHT'
        change_to = direction
        


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_UP, ord('w')}:
                        change_to = 'UP'
                    if event.key in {pygame.K_DOWN, ord('s')}:
                        change_to = 'DOWN'
                    if event.key in {pygame.K_LEFT, ord('a')}:
                        change_to = 'LEFT'
                    if event.key in {pygame.K_RIGHT, ord('d')}:
                        change_to = 'RIGHT'
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            if change_to == 'UP' and not direction == 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and not direction == 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and not direction == 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and not direction == 'LEFT':
                direction = 'RIGHT'

            if direction == 'UP':
                snake_pos[1] -= 10
            if direction == 'DOWN':
                snake_pos[1] += 10
            if direction == 'LEFT':
                snake_pos[0] -= 10
            if direction == 'RIGHT':
                snake_pos[0] += 10

            snake_body.insert(0, list(snake_pos))
            if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                self.score += 1
                food_spawn = False
            else:
                snake_body.pop()

            if not food_spawn:
                food_pos = [random.randrange(1, self.frame_size_x//10) * 10,
                            random.randrange(1, self.frame_size_y//10) * 10]
            food_spawn = True

            self.game_window.fill(self.black)
            for pos in snake_body:
                pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))

            pygame.draw.rect(self.game_window, self.white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

            if (snake_pos[0] < 0 or 
                snake_pos[0] > self.frame_size_x-10 or 
                snake_pos[1] < 0 or 
                snake_pos[1] > self.frame_size_y-10):
                self.game_over()

            for block in snake_body[1:]:
                if block[0] == snake_pos[0] and block[1] == snake_pos[1]:
                    self.game_over()

            self.show_score(1, self.white, 'consolas', 20)
            pygame.display.flip()
            self.fps_controller.tick(self.difficulty)
