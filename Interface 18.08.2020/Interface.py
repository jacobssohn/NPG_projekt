# -*- coding: utf-8 -*-
import pygame as pg
from classes import word_base as wb
from classes import button
import testy
import time as tm



# w plikach znajdują się niektóre pliki, które nie są używane przez grę, w późniejszych etapach się ich pozbęde

def text_objects(text, color=(0, 128, 0), font='freesansbold.ttf', fontSize=32):
    n_font = pg.font.Font(font, fontSize)
    n_text = n_font.render(text, True, color)
    return n_text, n_text.get_rect()


def messageToScreen(win, text, x_pos, y_pos, color=(255, 255, 255), font='freesansbold.ttf', fontSize=32):
    n_text, n_text_rect = text_objects(text, color, font, fontSize)
    n_text_rect.center = (x_pos, y_pos)
    win.blit(n_text, n_text_rect)


class Game:

    def __init__(self, win):
        self.win = win

        # przyciski w aplikacji
        self.easy_button = button((169, 169, 169), 433, 200, 189, 83)
        self.medium_button = button((169, 169, 169), 433, 300, 189, 83)
        self.hard_button = button((169, 169, 169), 433, 400, 189, 83)
        self.back_button = button((255, 0, 0), 100, 100, 132, 72)
        self.start_button = button((255, 0, 0), 445, 260, 189, 83)
        self.settings_button = button((255, 0, 0), 445, 380, 189, 83)
        self.english_button = button((225, 0, 0), 222, 460, 159, 72)
        self.polish_button = button((255, 0, 0), 699, 460, 158, 72)
        self.learning_button = button((225, 0, 0), 358, 360, 164, 72)
        self.challange_button = button((225, 0, 0), 622, 360, 164, 72)
        self.change_player_button = button((255, 0, 0), 800, 314, 184, 92)
        self.ready_button = button((0, 0, 0), 464, 180, 153, 72)
        self.chs_ex_button = button((0, 0, 0), 359, 300, 362, 62)
        self.create_new_button = button((0, 0, 0), 359, 400, 362, 62)
        self.plr1_button = button((0, 0, 0), 238, 250, 604, 67)
        self.plr2_button = button((0, 0, 0), 238, 350, 604, 67)
        self.plr3_button = button((0, 0, 0), 238, 450, 604, 67)

        self.mode = "chs_plr"
        self.language = "polish"

        self.players_list = open("config/players_list.txt", "r+").readline().split(" ")
        self.act_player = ""

        self.clock = pg.time.Clock()
        self.bg = pg.image.load('backgrounds/bg.jpg')

        # część z mechaniki działania:
        self.previous_word = None
        self.word_base = None
        self.input_text = ''
        self.random_word = None
        self.location_of_the_wanted_text = (540, 240)  # położenie wylosowanego słowa
        self.arrow = 0

        # część odpowiedzialna za pierwsze odpalenie gry
        self.first_launch = testy.str_to_bool(open("config/config.txt", "r+").readline().split(" ")[3])
        self.first_steps = 1

        self.pol_buttons0 = ['buttons/start0.png',
                             'buttons/challange0_pol.png',
                             'buttons/settings0_pol.png',
                             'buttons/english0_pol.png',
                             'buttons/polish0_pol.png',
                             'buttons/back0_pol.png',
                             'buttons/easy0_pol.png',
                             'buttons/medium0_pol.png',
                             'buttons/hard0_pol.png',
                             'buttons/learning0_pol.png',
                             'buttons/ready0_pol.png',
                             'buttons/chs_ex_pl0.png',
                             'buttons/create_new_pl0.png',
                             'buttons/change_plr_pl0.png']

        self.pol_buttons1 = ['buttons/start1.png',
                             'buttons/challange1_pol.png',
                             'buttons/settings1_pol.png',
                             'buttons/english1_pol.png',
                             'buttons/polish1_pol.png',
                             'buttons/back1_pol.png',
                             'buttons/easy1_pol.png',
                             'buttons/medium1_pol.png',
                             'buttons/hard1_pol.png',
                             'buttons/learning1_pol.png',
                             'buttons/ready1_pol.png',
                             'buttons/chs_ex_pl1.png',
                             'buttons/create_new_pl1.png',
                             'buttons/change_plr_pl1.png']

        self.ang_buttons0 = ['buttons/start0.png',
                             'buttons/challange0_ang.png',
                             'buttons/settings0_ang.png',
                             'buttons/english0_ang.png',
                             'buttons/polish0_ang.png',
                             'buttons/back0_ang.png',
                             'buttons/easy0_ang.png',
                             'buttons/medium0_ang.png',
                             'buttons/hard0_ang.png',
                             'buttons/learning0_ang.png',
                             'buttons/ready0_ang.png',
                             'buttons/chs_ex_eng0.png',
                             'buttons/create_new_eng0.png',
                             'buttons/change_plr_eng0.png']

        self.ang_buttons1 = ['buttons/start1.png',
                             'buttons/challange1_ang.png',
                             'buttons/settings1_ang.png',
                             'buttons/english1_ang.png',
                             'buttons/polish1_ang.png',
                             'buttons/back1_ang.png',
                             'buttons/easy1_ang.png',
                             'buttons/medium1_ang.png',
                             'buttons/hard1_ang.png',
                             'buttons/learning1_ang.png',
                             'buttons/ready1_ang.png',
                             'buttons/chs_ex_eng1.png',
                             'buttons/create_new_eng1.png',
                             'buttons/change_plr_eng1.png']

        self.start0, self.challange0, self.settings0, self.english0, self.polish0, self.back0, self.easy0, self.medium0, \
        self.hard0, self.learning0, self.ready0, self.chs_ex0, self.create_new0, self.change_plr0 = self.pol_buttons0

        self.start1, self.challange1, self.settings1, self.english1, self.polish1, self.back1, self.easy1, self.medium1, \
        self.hard1, self.learning1, self.ready1, self.chs_ex1, self.create_new1, self.change_plr1 = self.pol_buttons1

    def change_language(self, language: str) -> None:  # funkcja odpowiedzialna za zmiane języka
        if (language == "polish"):
            self.language = "english"
            self.start0, self.challange0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0, self.ready0, self.chs_ex0, self.create_new0, self.change_plr0 = self.ang_buttons0
            self.start1, self.challange1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1, self.ready1, self.chs_ex1, self.create_new1, self.change_plr1 = self.ang_buttons1



        elif (language == "english"):
            self.language = "polish"
            self.start0, self.challange0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0, self.ready0, self.chs_ex0, self.create_new0, self.change_plr0 = self.pol_buttons0

            self.start1, self.challange1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1, self.ready1, self.chs_ex1, self.create_new1, self.change_plr1 = self.pol_buttons1
        pg.display.update()  # funkcj

    def word_baseReload(self, mode: str, language: str) -> list:
        if language == "polish":
            if mode == "easy":
                return open("word_base/easy_pol.txt", "r+").readline().split(" ")

    def players_listing(self, arrow: int):
        length = len(self.players_list)
        if length == 0:
            return None
        elif length <= 3:
            return self.players_list
        elif length > 3:
            return self.players_list[arrow:arrow+3]




    def mechanics(self):  # funkcja mechaniki rozgrywki
        if self.input_text == self.random_word:
            self.random_word = wb.get_randWord(self.word_base, self.previous_word)  # losuje kolejne słowo
            self.input_text = ''  # kasuje tekst
            self.previous_word = self.random_word

        font = pg.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
        wanted_word_text = font.render(self.random_word, True, (100, 100, 150), (
        255, 255, 255))  # renderowanie wylosowanego słowa, pierwszy tuple to kolor liter, drugi to
        textRect_2 = wanted_word_text.get_rect()  # generowanie prostokąta na którym          # kolor pola tekstowego, teraz się zlewa z tłem i go nie widać
        textRect_2.center = self.location_of_the_wanted_text  # leży szukany tekst
        text = font.render(self.input_text, True, (100, 100, 150), (255, 255, 255))  # renderowanie wpisywanego tekstu
        textRect = text.get_rect()  # pole z wpisywanym tekstem i jego środek
        textRect.center = (540, 360)
        self.win.blit(text, textRect)  # nałożenie zrenderowanego tekstu na jego pole tekstowe
        self.win.blit(wanted_word_text, textRect_2)

    def redrawWindow(self, mode):  # funkcja odpowiedzialna za narysowanie okna zależnie od aktualnego trybu
        pos = pg.mouse.get_pos()

        # część odpowiedzialna za pierwsze uruchomienie gry
        if self.first_launch:
            if self.first_steps == 1:
                self.win.blit(self.bg, (0, 0))
                messageToScreen(self.win, "Witaj w grze Mistrz Klawiatury", 540, 50, (255, 255, 255))
                messageToScreen(self.win, "Wybierz język:", 540, 100, (255, 255, 255))
                self.win.blit(pg.image.load(self.ready0), (464, 180))
                if (self.language == "polish"):
                    self.win.blit(pg.image.load(self.polish1), (699, 460))
                    self.win.blit(pg.image.load(self.english0), (222, 460))
                    if (self.english_button.isOver(pos)):
                        self.win.blit(pg.image.load(self.english1), (222, 460))
                elif (self.language == "english"):
                    self.win.blit(pg.image.load(self.english1), (222, 460))
                    self.win.blit(pg.image.load(self.polish0), (699, 460))
                    if (self.polish_button.isOver(pos)):
                        self.win.blit(pg.image.load(self.polish1), (699, 460))
                if (self.ready_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.ready1), (464, 180))

            elif self.first_steps == 2:
                self.win.blit(self.bg, (0, 0))
                if (self.language == "polish"):
                    messageToScreen(self.win, "Wpisz swój nickname:", 540, 50, (255, 255, 255))
                elif (self.language == "english"):
                    messageToScreen(self.win, "Choose your nickname", 540, 50, (255, 255, 255))
                testy.get_player_nick(self.win, self.input_text)

        else:
            if mode == "chs_plr":
                self.win.blit(pg.image.load('backgrounds/bg_chs_pl_raw.jpg'), (0, 0))
                self.win.blit(pg.image.load(self.chs_ex0), (359, 300))
                self.win.blit(pg.image.load(self.create_new0), (359, 400))
                if (self.chs_ex_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.chs_ex1), (359, 300))
                elif (self.create_new_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.create_new1), (359, 400))

            elif mode == "chs_ex":
                list = Game.players_listing(self,self.arrow)

                self.win.blit(pg.image.load('backgrounds/bg.jpg'), (0, 0))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 250))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 350))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 450))
                messageToScreen(self.win, list[0], 540, 283)
                messageToScreen(self.win, list[1], 540, 383)
                messageToScreen(self.win, list[2], 540, 483)
                if self.plr1_button.isOver(pos):
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 250))
                    messageToScreen(self.win, list[0], 540, 283)
                elif self.plr2_button.isOver(pos):
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 350))
                    messageToScreen(self.win, list[1], 540, 383)
                elif self.plr3_button.isOver(pos):
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 450))
                    messageToScreen(self.win, list[2], 540, 483)



            elif mode == "menu":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.start0), (445, 260))
                self.win.blit(pg.image.load(self.settings0), (445, 380))
                self.win.blit(pg.image.load(self.change_plr0), (800, 314))
                if(self.language == "polish"):
                    messageToScreen(self.win, "Gra: {player}".format(player=self.act_player), 880, 150, (255, 255, 255),
                                    'freesansbold.ttf', 22)
                elif(self.language == "english"):
                    messageToScreen(self.win, "Playing: {player}".format(player=self.act_player), 880, 150, (255, 255, 255),
                                    'freesansbold.ttf', 22)
                if (self.start_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.start1), (445, 260))
                elif (self.settings_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.settings1), (445, 380))
                elif (self.change_player_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.change_plr1), (800, 314))

            elif mode == "settings":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.language == "polish"):
                    self.win.blit(pg.image.load(self.polish1), (699, 460))
                    self.win.blit(pg.image.load(self.english0), (222, 460))
                    if (self.english_button.isOver(pos)):
                        self.win.blit(pg.image.load(self.english1), (222, 460))
                elif (self.language == "english"):
                    self.win.blit(pg.image.load(self.english1), (222, 460))
                    self.win.blit(pg.image.load(self.polish0), (699, 460))
                    if (self.polish_button.isOver(pos)):
                        self.win.blit(pg.image.load(self.polish1), (699, 460))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
            elif mode == "start":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.challange0), (622, 360))
                self.win.blit(pg.image.load(self.learning0), (358, 360))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.language == "polish"):
                    messageToScreen(self.win, "Gra: {player}".format(player=self.act_player), 880, 150, (255, 255, 255),
                                    'freesansbold.ttf', 22)
                elif (self.language == "english"):
                    messageToScreen(self.win, "Playing: {player}".format(player=self.act_player), 880, 150,
                                    (255, 255, 255),
                                    'freesansbold.ttf', 22)
                if (self.learning_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.learning1), (358, 360))
                elif (self.challange_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.challange1), (622, 360))
                elif (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
            elif mode == "challange":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.easy0), (433, 200))
                self.win.blit(pg.image.load(self.medium0), (433, 300))
                self.win.blit(pg.image.load(self.hard0), (433, 400))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.easy_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.easy1), (433, 200))
                elif (self.medium_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.medium1), (433, 300))
                elif (self.hard_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.hard1), (433, 400))
                elif (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
            elif mode == "easy":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
            elif mode == "medium":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
            elif mode == "hard":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
            elif mode == "learning":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))



    def start(self):  # funkcja odpowiedzialna za odpalenie i wyłączenie gry
        pg.init()
        pg.display.set_caption("Mistrz klawiatury")
        pg.time.delay(60)
        run = True

        while run:

            Game.redrawWindow(self, self.mode)
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    run = False
                    self.act_player = ""
                    pg.quit()
                    quit()
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE] and keys[pg.K_DOWN]:
                    self.run = False
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN and self.first_launch:
                    if self.ready_button.isOver(pos):
                        print("next step")
                        self.first_steps += 1
                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "chs_ex":
                    list = Game.players_listing(self, self.arrow)
                    if event.button == 4:
                        if self.arrow == 0:
                            pass
                        else:
                            self.arrow -= 1
                    elif event.button == 5:
                        if self.arrow == len(self.players_list) - 4:
                            pass
                        else:
                            self.arrow += 1
                    elif self.plr1_button.isOver(pos):
                        self.act_player = list[0]
                        self.mode = "menu"

                    elif self.plr2_button.isOver(pos):
                        self.act_player = list[1]
                        self.mode = "menu"

                    elif self.plr3_button.isOver(pos):
                        self.act_player = list[2]
                        self.mode = "menu"





                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "challange":
                    if self.easy_button.isOver(pos):
                        print("Pick easy")
                        self.mode = "easy"
                        self.word_base = wb.words_reload(self.mode, self.language)
                        self.random_word = wb.get_randWord(self.word_base, self.previous_word)
                        print(self.word_base)
                    elif self.medium_button.isOver(pos):
                        print("Pick medium")
                        self.mode = "medium"
                        self.word_base = wb.words_reload(self.mode, self.language)
                        self.random_word = wb.get_randWord(self.word_base, self.previous_word)
                    elif self.hard_button.isOver(pos):
                        print("Pick Hard")
                        self.mode = "hard"
                        self.word_base = wb.words_reload(self.mode, self.language)
                        self.random_word = wb.get_randWord(self.word_base, self.previous_word)
                if event.type == pg.MOUSEBUTTONDOWN and self.mode != "menu":
                    if self.back_button.isOver(pos):
                        print("Returned")
                        if (self.mode == "start" or self.mode == "settings"):
                            self.mode = "menu"
                        elif (self.mode == "challange" or self.mode == "learning"):
                            self.mode = "start"
                        elif (self.mode == "easy" or self.mode == "medium" or self.mode == "hard"):
                            self.mode = "challange"

                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "menu":
                    if self.start_button.isOver(pos):
                        print("Pick difficulty:")
                        self.mode = "start"
                    elif self.settings_button.isOver(pos):
                        print("welcome in settings: ", self.language)
                        self.mode = "settings"
                    elif self.change_player_button.isOver(pos):
                        self.mode = "chs_plr"
                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "start":
                    if self.challange_button.isOver(pos):
                        self.mode = "challange"
                    elif self.learning_button.isOver(pos):
                        self.mode = "learning"
                if event.type == pg.MOUSEBUTTONDOWN and (self.mode == "settings" or self.first_steps == 1):
                    if (self.polish_button.isOver(pos) and self.language == "english"):
                        Game.change_language(self, self.language)
                        print("switch")
                        pg.display.update()
                    elif (self.english_button.isOver(pos) and self.language == "polish"):
                        Game.change_language(self, self.language)
                        print("switch")
                        pg.display.update()
                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "chs_plr":
                    if self.create_new_button.isOver(pos):
                        self.first_launch = True
                        self.first_steps = 2
                    if self.chs_ex_button.isOver(pos):
                        self.mode = "chs_ex"

                # część z mechaniki

                elif (event.type == pg.KEYDOWN and  # wyjątki które nie powodują wpisania nazwy klawisza
                      (
                              pg.key.name(event.key) == 'escape' or
                              pg.key.name(event.key) == 'left ctrl' or
                              pg.key.name(event.key) == 'left alt' or
                              pg.key.name(event.key) == "right alt" or
                              pg.key.name(event.key) == 'alt gr' or
                              pg.key.name(event.key) == 'right ctrl' or
                              pg.key.name(event.key) == 'left shift' or
                              pg.key.name(event.key) == 'right shift' or
                              pg.key.name(event.key) == 'space'
                        ) and (
                                self.mode == "easy" or self.mode == "medium" or self.mode == "hard" or self.first_steps == 2)
                ):
                    pass


                elif keys[pg.K_RALT]:  # obsługa polskich znaków:
                    letter = ""
                    if keys[pg.K_c]:
                        letter = "ć"
                    elif keys[pg.K_z]:
                        letter = "ż"
                    elif keys[pg.K_a]:
                        letter = "ą"
                    elif keys[pg.K_e]:
                        letter = "ę"
                    elif keys[pg.K_l]:
                        letter = "ł"
                    elif keys[pg.K_n]:
                        letter = "ń"
                    elif keys[pg.K_x]:
                        letter = "ź"
                    elif keys[pg.K_o]:
                        letter = "ó"
                    elif keys[pg.K_s]:
                        letter = "ś"
                    self.input_text += letter


                # Zadziała przy pierwszym uruchomieniu gry i przy tworzeniu nowych profili graczy
                elif (event.type == pg.KEYDOWN and pg.key.name(
                        event.key) == 'return' and self.first_steps == 2):
                    open("players/{player_name}_player.txt".format(player_name=self.input_text), "x")
                    cnf = open('config/config.txt', "r")
                    lines = cnf.readlines()
                    cnf.close()

                    del lines[0]

                    cnf2 = open('config/config.txt', "w+")
                    cnf2.write("first launch = False")
                    cnf2.close()

                    base_update = open("config/players_list.txt", "a")
                    base_update.write(self.input_text + " ")
                    base_update.close()

                    self.first_launch = False
                    self.act_player = self.input_text
                    print(self.first_launch)
                    self.first_steps += 1
                    self.input_text = ""
                    self.mode = "menu"


                elif (event.type == pg.KEYDOWN and pg.key.name(event.key) == 'backspace' and
                      (
                              self.mode == "easy" or self.mode == "medium" or self.mode == "hard" or self.first_steps == 2)):  # usuwanie liter
                    self.input_text = self.input_text[: len(self.input_text) - 1]

                elif (event.type == pg.KEYDOWN and ((
                                                                self.mode == "easy" or self.mode == "medium" or self.mode == "hard") or self.first_steps == 2)):  # wpisywanie liter
                    if keys[pg.K_RSHIFT] or keys[pg.K_LSHIFT]:
                        print(pg.key.name(event.key))
                        letter = pg.key.name(event.key)
                        self.input_text += letter.upper()
                    else:
                        print(pg.key.name(event.key))
                        self.input_text += pg.key.name(event.key)

            self.clock.tick(80)
            pg.display.update()
