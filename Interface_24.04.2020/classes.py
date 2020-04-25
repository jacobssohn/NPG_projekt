import pygame
import random
import pygame_textinput

class button():
    def __init__(self, color, x, y, width, height, text='', font='comicsans', font_size=60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size


    def draw(self, win, outline=None):
        # używam grafiki do wyglądu przycisków, więc z tej metody nie korzystałem
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isOver(self, pos):
        # pos to pozycja myszy (pygame.mouse.get_pos())
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def text_objects(text, color = (0, 128, 0), font='freesansbold.ttf', fontSize=32):
    n_font = pygame.font.Font(font, fontSize)
    n_text = n_font.render(text, True, color)
    return n_text, n_text.get_rect()

def messageToScreen(win,text, x_pos, y_pos, color = (0, 128, 0), font='freesansbold.ttf', fontSize=32):
    n_text,n_text_rect = text_objects(text, color, font, fontSize)
    n_text_rect.center = (x_pos, y_pos)
    win.blit(n_text, n_text_rect)

class interface:

    def __init__(self,win):
        self.win = win

        self.easy_button = button((169, 169, 169), 433, 200, 189, 83)
        self.medium_button = button((169, 169, 169), 433, 300, 189, 83)
        self.hard_button = button((169, 169, 169), 433, 400, 189, 83)
        self.back_button = button((255, 0, 0), 100, 100, 132, 72)
        self.start_button = button((255, 0, 0), 445, 260, 189, 83)
        self.settings_button = button((255, 0, 0),445, 380, 189, 83)
        self.english_button = button((225, 0, 0), 360, 360, 159, 72)
        self.polish_button = button((255, 0, 0), 620, 360, 158, 72)
        self.learning_button = button((225, 0, 0), 358, 360, 164, 72)
        self.challange_button = button((225, 0, 0), 622, 360, 164, 72)

        self.run = True
        self.mode = "menu"
        self.language = "polish"
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('bg2.jpg')

        self.start0, self.challange0, self.settings0, self.english0,\
        self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0 = ['start0.png',
                                                                                                    'challange0_pol.png',
                                                                                                    'settings0_pol.png',
                                                                                                    'english0_pol.png',
                                                                                                    'polish0_pol.png',
                                                                                                    'back0_pol.png',
                                                                                                    'easy0_pol.png',
                                                                                                    'medium0_pol.png',
                                                                                                    'hard0_pol.png',
                                                                                                    'learning0_pol.png']

        self.start1, self.challange1, self.settings1, self.english1,\
        self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1 = ['start1.png',
                                                                                                 'challange1_pol.png',
                                                                                                 'settings1_pol.png',
                                                                                                 'english1_pol.png',
                                                                                                 'polish1_pol.png',
                                                                                                 'back1_pol.png',
                                                                                                 'easy1_pol.png',
                                                                                                 'medium1_pol.png',
                                                                                                 'hard1_pol.png',
                                                                                                 'learning1_pol.png']


    def change_language(self,language):
        if (language == "polish"):
            self.language = "english"
            self.start0, self.challange0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0 = ['start0.png',
                                                                                                 'challange0_ang.png',
                                                                                                 'settings0_ang.png',
                                                                                                 'english0_ang.png',
                                                                                                 'polish0_ang.png',
                                                                                                 'back0_ang.png',
                                                                                                 'easy0_ang.png',
                                                                                                 'medium0_ang.png',
                                                                                                 'hard0_ang.png',
                                                                                                 'learning0_ang.png']
            self.start1, self.challange1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1 = ['start1.png',
                                                                                                 'challange1_ang.png',
                                                                                                 'settings1_ang.png',
                                                                                                 'english1_ang.png',
                                                                                                 'polish1_ang.png',
                                                                                                 'back1_ang.png',
                                                                                                 'easy1_ang.png',
                                                                                                 'medium1_ang.png',
                                                                                                 'hard1_ang.png',
                                                                                                 'learning1_ang.png']



        elif (language == "english"):
            self.language = "polish"
            self.start0, self.challange0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0 = ['start0.png',
                                                                                              'challange0_pol.png',
                                                                                              'settings0_pol.png',
                                                                                              'english0_pol.png',
                                                                                              'polish0_pol.png',
                                                                                              'back0_pol.png',
                                                                                              'easy0_pol.png',
                                                                                              'medium0_pol.png',
                                                                                              'hard0_pol.png',
                                                                                              'learning0_pol.png']

            self.start1, self.challange1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1 = ['start1.png',
                                                                                              'challange1_pol.png',
                                                                                              'settings1_pol.png',
                                                                                              'english1_pol.png',
                                                                                              'polish1_pol.png',
                                                                                              'back1_pol.png',
                                                                                              'easy1_pol.png',
                                                                                              'medium1_pol.png',
                                                                                              'hard1_pol.png',
                                                                                              'learning1_pol.png']
        pygame.display.update()

    def redrawWindow(self,mode):
        pos = pygame.mouse.get_pos()



        if mode == "menu":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.start0), (445, 260))
            self.win.blit(pygame.image.load(self.settings0), (445, 380))
            if(self.start_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.start1), (445, 260))
            elif(self.settings_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.settings1), (445, 380))
        elif mode == "settings":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if (self.language == "polish"):
                self.win.blit(pygame.image.load(self.polish1), (620, 360))
                self.win.blit(pygame.image.load(self.english0), (360, 360))
                if(self.english_button.isOver(pos)):
                    self.win.blit(pygame.image.load(self.english1), (360, 360))
            elif(self.language == "english"):
                self.win.blit(pygame.image.load(self.english1), (360, 360))
                self.win.blit(pygame.image.load(self.polish0), (620, 360))
                if(self.polish_button.isOver(pos)):
                    self.win.blit(pygame.image.load(self.polish1), (620, 360))
            if(self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))

        elif mode == "start":
            self.win.blit(self.bg,(0, 0))
            self.win.blit(pygame.image.load(self.challange0), (622, 360))
            self.win.blit(pygame.image.load(self.learning0), (358, 360))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if(self.learning_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.learning1),(358, 360))
            elif(self.challange_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.challange1), (622, 360))
            elif(self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))
        elif mode == "challange":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.easy0), (433, 200))
            self.win.blit(pygame.image.load(self.medium0), (433, 300))
            self.win.blit(pygame.image.load(self.hard0), (433, 400))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if(self.easy_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.easy1), (433, 200))
            elif(self.medium_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.medium1), (433, 300))
            elif(self.hard_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.hard1), (433,400))
            elif(self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))
        elif mode == "easy":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if (self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))
        elif mode == "medium":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if (self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))
        elif mode == "hard":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if (self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))
        elif mode == "learning":
            self.win.blit(self.bg, (0, 0))
            self.win.blit(pygame.image.load(self.back0), (100, 100))
            if(self.back_button.isOver(pos)):
                self.win.blit(pygame.image.load(self.back1), (100, 100))



    def start(self):
        pygame.init()
        pygame.display.set_caption("Mistrz klawiatury")
        while self.run:
            interface.redrawWindow(self, self.mode)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] and keys[pygame.K_DOWN]:
                    self.run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.mode == "challange":
                    if self.easy_button.isOver(pos):
                        print("Pick easy")
                        self.mode = "easy"
                    elif self.medium_button.isOver(pos):
                        print("Pick medium")
                        self.mode = "medium"
                    elif self.hard_button.isOver(pos):
                        print("Pick Hard")
                        self.mode = "hard"
                if event.type == pygame.MOUSEBUTTONDOWN and self.mode != "menu":
                    if self.back_button.isOver(pos):
                        print("Returned")
                        if(self.mode == "start" or self.mode == "settings"):
                            self.mode = "menu"
                        elif(self.mode == "challange" or self.mode == "learning"):
                            self.mode = "start"
                        elif(self.mode == "easy" or self.mode == "medium" or self.mode == "hard"):
                            self.mode = "challange"

                if event.type == pygame.MOUSEBUTTONDOWN and self.mode == "menu":
                    if self.start_button.isOver(pos):
                        print("Pick difficulty:")
                        self.mode = "start"
                    elif self.settings_button.isOver(pos):
                        print("welcome in settings: ", self.language)
                        self.mode = "settings"
                if event.type == pygame.MOUSEBUTTONDOWN and self.mode == "start":
                    if self.challange_button.isOver(pos):
                        self.mode = "challange"
                    elif self.learning_button.isOver(pos):
                        self.mode = "learning"
                if event.type == pygame.MOUSEBUTTONDOWN and self.mode == "settings":
                    if(self.polish_button.isOver(pos) and self.language == "english"):
                        interface.change_language(self, self.language)
                        pygame.display.update()
                    elif(self.english_button.isOver(pos) and self.language == "polish"):
                        interface.change_language(self, self.language)
                        pygame.display.update()


            self.clock.tick(60)
            pygame.display.update()

