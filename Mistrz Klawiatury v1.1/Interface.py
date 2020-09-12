# -*- coding: utf-8 -*-
import pygame as pg
import random
from classes import word_base as wb
from classes import button
import functions
import time



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
        self.reset = False
        self.click_check = False
        self.exist_error_check = False

        self.easy_button = button((169, 169, 169), 433, 200, 189, 83)
        self.medium_button = button((169, 169, 169), 433, 300, 189, 83)
        self.hard_button = button((169, 169, 169), 433, 400, 189, 83)
        self.back_button = button((255, 0, 0), 100, 100, 132, 72)
        self.start_button = button((255, 0, 0), 288, 260, 504, 79)
        self.settings_button = button((255, 0, 0), 288, 458, 244, 79)
        self.english_button = button((225, 0, 0), 222, 460, 159, 72)
        self.polish_button = button((255, 0, 0), 699, 460, 158, 72)
        self.learning_button = button((225, 0, 0), 358, 360, 164, 72)
        self.challenge_button = button((225, 0, 0), 622, 360, 164, 72)
        self.change_player_button = button((255, 0, 0), 548, 458, 244, 79)
        self.ready_button = button((0, 0, 0), 464, 180, 153, 72)
        self.chs_ex_button = button((0, 0, 0), 359, 300, 362, 62)
        self.create_new_button = button((0, 0, 0), 359, 400, 362, 62)
        self.plr1_button = button((0, 0, 0), 238, 250, 604, 67)
        self.plr2_button = button((0, 0, 0), 238, 350, 604, 67)
        self.plr3_button = button((0, 0, 0), 238, 450, 604, 67)
        self.topscores_button = button((255, 0, 0), 288, 359, 504, 79)

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
        self.timer = 60
        self.score = 0
        self.random_word = None
        self.location_of_the_wanted_text = (540, 240)  # położenie wylosowanego słowa
        self.save_difficulty = 0
        self.arrow = 0

        # część odpowiedzialna za pierwsze odpalenie gry
        self.first_launch = functions.str_to_bool(open("config/config.txt", "r+").readline().split(" ")[3])
        self.first_steps = 1

        self.pol_buttons0 = ['buttons/start0.png',
                             'buttons/challenge0_pol.png',
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
                             'buttons/change_plr_pl0.png',
                             'buttons/topscores0_pol.png']

        self.pol_buttons1 = ['buttons/start1.png',
                             'buttons/challenge1_pol.png',
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
                             'buttons/change_plr_pl1.png',
                             'buttons/topscores1_pol.png']

        self.ang_buttons0 = ['buttons/start0.png',
                             'buttons/challenge0_ang.png',
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
                             'buttons/change_plr_eng0.png',
                             'buttons/topscores0_ang.png']

        self.ang_buttons1 = ['buttons/start1.png',
                             'buttons/challenge1_ang.png',
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
                             'buttons/change_plr_eng1.png',
                             'buttons/topscores1_ang.png']

        self.start0, self.challenge0, self.settings0, self.english0, self.polish0, self.back0, self.easy0, self.medium0, \
        self.hard0, self.learning0, self.ready0, self.chs_ex0, self.create_new0, self.change_plr0, self.topscores0 = self.pol_buttons0

        self.start1, self.challenge1, self.settings1, self.english1, self.polish1, self.back1, self.easy1, self.medium1, \
        self.hard1, self.learning1, self.ready1, self.chs_ex1, self.create_new1, self.change_plr1, self.topscores1 = self.pol_buttons1

    def change_language(self, language: str) -> None:  # funkcja odpowiedzialna za zmiane języka

        if (language == "polish"):
            self.language = "english"
            self.start0, self.challenge0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0, \
            self.ready0, self.chs_ex0, self.create_new0, self.change_plr0, self.topscores0 = self.ang_buttons0

            self.start1, self.challenge1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1, \
            self.ready1, self.chs_ex1, self.create_new1, self.change_plr1, self.topscores1 = self.ang_buttons1


        elif (language == "english"):
            self.language = "polish"
            self.start0, self.challenge0, self.settings0, self.english0, \
            self.polish0, self.back0, self.easy0, self.medium0, self.hard0, self.learning0, \
            self.ready0, self.chs_ex0, self.create_new0, self.change_plr0, self.topscores0 = self.pol_buttons0

            self.start1, self.challenge1, self.settings1, self.english1, \
            self.polish1, self.back1, self.easy1, self.medium1, self.hard1, self.learning1, \
            self.ready1, self.chs_ex1, self.create_new1, self.change_plr1, self.topscores1 = self.pol_buttons1
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
            return self.players_list[arrow:arrow + 3]

    def mechanics(self):  # funkcja mechaniki rozgrywki
        if self.input_text == self.random_word:
            self.random_word = wb.get_randWord(self.word_base, self.previous_word)  # losuje kolejne słowo
            self.score += 1
            self.input_text = ''  # kasuje tekst
            self.previous_word = self.random_word

        font = pg.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
        wanted_word_text = font.render(self.random_word, True, (150, 100, 200),
                                       pg.SRCALPHA)  # renderowanie wylosowanego słowa, pierwszy tuple to kolor liter, drugi to
        textRect_2 = wanted_word_text.get_rect()  # generowanie prostokąta na którym               # kolor pola tekstowego, teraz się zlewa z tłem i go nie widać
        textRect_2.center = self.location_of_the_wanted_text  # leży szukany tekst
        text = font.render(self.input_text, True, (150, 100, 200), pg.SRCALPHA)  # renderowanie wpisywanego tekstu
        textRect = text.get_rect()  # pole z wpisywanym tekstem i jego środek
        textRect.center = (540, 360)
        self.win.blit(text, textRect)  # nałożenie zrenderowanego tekstu na jego pole tekstowe
        self.win.blit(wanted_word_text, textRect_2)
        if self.mode != "learning":
            if self.language == "polish":
                seconds = font.render("Czas: {}".format(self.timer), True, (150, 0, 200), pg.SRCALPHA)
            else:
                seconds = font.render("Time: {}".format(self.timer), True, (150, 0, 200), pg.SRCALPHA)
            textRect_3 = seconds.get_rect()
            self.win.blit(seconds, textRect_3)

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
                    messageToScreen(self.win, "Wpisz swoją nazwę użytkownika:", 540, 50, (255, 255, 255))
                elif (self.language == "english"):
                    messageToScreen(self.win, "Choose your nickname", 540, 50, (255, 255, 255))
                functions.get_player_nick(self.win, self.input_text)
        else:
            if mode == "chs_plr":
                self.win.blit(self.bg, (0, 0))
                if self.language == 'polish':
                    messageToScreen(self.win,"Witaj ponownie!", 540, 100)
                    messageToScreen(self.win,"Wybierz istniejący profil gracza lub stwórz nowy", 540, 150)
                elif self.language == "english":
                    messageToScreen(self.win, "Welcome again!", 540, 100)
                    messageToScreen(self.win, "Choose existing player profile or create new", 540, 150)
                self.win.blit(pg.image.load(self.chs_ex0), (359, 300))
                self.win.blit(pg.image.load(self.create_new0), (359, 400))
                if (self.chs_ex_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.chs_ex1), (359, 300))
                elif (self.create_new_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.create_new1), (359, 400))

            elif mode == "chs_ex":
                list = Game.players_listing(self, self.arrow)

                self.win.blit(pg.image.load('backgrounds/bg.jpg'), (0, 0))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 250))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 350))
                self.win.blit(pg.image.load("buttons/choose0.png"), (238, 450))
                messageToScreen(self.win, list[0], 540, 283)
                try:
                    messageToScreen(self.win, list[1], 540, 383)
                except IndexError:
                    pass
                try:
                    messageToScreen(self.win, list[2], 540, 483)
                except IndexError:
                    pass
                if self.plr1_button.isOver(pos):
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 250))
                    messageToScreen(self.win, list[0], 540, 283)
                elif self.plr2_button.isOver(pos) and len(self.players_list) > 2:
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 350))
                    messageToScreen(self.win, list[1], 540, 383)
                elif self.plr3_button.isOver(pos) and len(self.players_list) > 3:
                    self.win.blit(pg.image.load("buttons/choose1.png"), (238, 450))
                    messageToScreen(self.win, list[2], 540, 483)




            elif mode == "menu":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.start0), (288, 260))
                self.win.blit(pg.image.load(self.settings0), (288, 458))
                self.win.blit(pg.image.load(self.topscores0), (288, 359))
                self.win.blit(pg.image.load(self.change_plr0), (548, 458))
                self.click_check = False
                if (self.language == "polish"):
                    messageToScreen(self.win, "Gra: {player}".format(player=self.act_player), 880, 150, (255, 255, 255),
                                    'freesansbold.ttf', 22)
                elif (self.language == "english"):
                    messageToScreen(self.win, "Playing: {player}".format(player=self.act_player), 880, 150,
                                    (255, 255, 255),
                                    'freesansbold.ttf', 22)
                if (self.start_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.start1), (288, 260))
                elif (self.topscores_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.topscores1), (288, 359))
                elif (self.settings_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.settings1), (288, 458))
                elif (self.change_player_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.change_plr1), (548, 458))



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
                self.win.blit(pg.image.load(self.challenge0), (622, 360))
                self.win.blit(pg.image.load(self.learning0), (358, 360))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.learning_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.learning1), (358, 360))
                elif (self.challenge_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.challenge1), (622, 360))
                elif (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
            elif mode == "challenge":
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

                if (self.language == "polish"):
                    font = pg.font.Font('freesansbold.ttf', 20)
                    rules1 = font.render("W tym trybie należy wpisać jak najwięcej słów w 60 sekund.", True,
                                         (150, 0, 200), pg.SRCALPHA)
                    rules2 = font.render("Wynik zależy od liczby wpisanych słów.", True, (150, 0, 200), pg.SRCALPHA)
                    textRect1 = rules1.get_rect()
                    textRect2 = rules2.get_rect()
                    textRect1.center = (512, 550)
                    textRect2.center = (512, 580)
                    self.win.blit(rules1, textRect1)
                    self.win.blit(rules2, textRect2)
                else:
                    font = pg.font.Font('freesansbold.ttf', 20)
                    rules1 = font.render("In this mode you need to type as many words as possible within 60 seconds.",
                                         True,
                                         (150, 0, 200), pg.SRCALPHA)
                    rules2 = font.render("The score is the number of words typed in.", True, (150, 0, 200),
                                         pg.SRCALPHA)
                    textRect1 = rules1.get_rect()
                    textRect2 = rules2.get_rect()
                    textRect1.center = (512, 550)
                    textRect2.center = (512, 580)
                    self.win.blit(rules1, textRect1)
                    self.win.blit(rules2, textRect2)
            elif mode == "easy":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
                self.save_difficulty = 1
                if self.language == 'polish':
                    messageToScreen(self.win, "Twój wynik: " + str(self.score), 540, 100)
                elif self.language == 'english':
                    messageToScreen(self.win, "Your score: " + str(self.score), 540, 100)
            elif mode == "medium":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
                self.save_difficulty = 2
                if self.language == 'polish':
                    messageToScreen(self.win, "Twój wynik: " + str(self.score), 540, 100)
                elif self.language == 'english':
                    messageToScreen(self.win, "Your score: " + str(self.score), 540, 100)
            elif mode == "hard":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                Game.mechanics(self)
                self.save_difficulty = 3
                if self.language == 'polish':
                    messageToScreen(self.win, "Twój wynik: " + str(self.score), 540, 100)
                elif self.language == 'english':
                    messageToScreen(self.win, "Your score: " + str(self.score), 540, 100)
            elif mode == "learning":
                self.win.blit(self.bg, (0, 0))
                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))
                if self.language == "polish":
                    messageToScreen(self.win,
                                    "W tym trybie możesz dowolnie wpisywać losowane słowa bez limitu czasowego.",
                                    512, 500, fontSize=18)
                else:
                    messageToScreen(self.win,
                                    "In this mode you can freely type words you see on screen with no time limit. Click on the screen to begin.",
                                    512, 500, fontSize=18)
                Game.mechanics(self)
                self.save_difficulty = random.randint(1, 3)
            elif mode == "save screen":

                font = pg.font.Font('freesansbold.ttf', 20)
                if (self.input_text != "" and not self.reset):
                    self.input_text = ""
                    self.reset = True
                self.win.blit(self.bg, (0, 0))
                if self.language == "polish":
                    messageToScreen(self.win, "Gratulacje! Twój wynik to {}.".format(self.score), 520, 150, fontSize=25)
                    messageToScreen(self.win, "Wciśnij enter aby kontynuować", 520, 650, fontSize=25)
                else:
                    messageToScreen(self.win,"Congratulations! Your score is {}.".format(self.score), 520, 150, fontSize=25)
                    messageToScreen(self.win, "Press enter to continue", 520, 350, fontSize=25)
                # save_text_window = font.render("Gratulacje! Twój wynik to {}. Podaj swój nick i wciśnij ENTER aby zapisać. ".format(self.score), True, (150, 0, 200), pg.SRCALPHA).get_rect()
                # save_text_window.center = (512, 300)
                # self.win.blit(font.render("Gratulacje! Twój wynik {}. Podaj swój nick i wciśnij ENTER aby zapisać. ".format(self.score), True, (150, 0, 200), pg.SRCALPHA), save_text_window)
                functions.get_player_nick(self.win, self.input_text)

            elif mode == "top scores":
                self.win.blit(self.bg, (0, 0))

                self.win.blit(pg.image.load(self.back0), (100, 100))
                if (self.back_button.isOver(pos)):
                    self.win.blit(pg.image.load(self.back1), (100, 100))

                scores_easy = functions.get_results(self.act_player, 'easy')
                scores_medium = functions.get_results(self.act_player, 'medium')
                scores_hard = functions.get_results(self.act_player, 'hard')

                if self.language == "polish":
                    messageToScreen(self.win, "Najlepsze wyniki", 540, 150, (255, 255, 255))
                    messageToScreen(self.win, "Łatwy poziom:", 200, 310)
                    messageToScreen(self.win, "Średni poziom:", 540, 310)
                    messageToScreen(self.win, "Trudny poziom:", 930, 310)
                else:
                    messageToScreen(self.win, "Top scores", 540, 150, (255, 255, 255))
                    messageToScreen(self.win, "Easy:", 200, 310)
                    messageToScreen(self.win, "Medium:", 540, 310)
                    messageToScreen(self.win, "Hard:", 930, 310)
                for i in range(10):
                    try:
                        messageToScreen(self.win, "{}".format(scores_easy[i]), 200,
                                        360 + i * 40)
                    except IndexError:
                        pass
                    try:
                        messageToScreen(self.win, "{}".format(scores_medium[i]), 548,
                                        360 + i * 40)
                    except IndexError:
                        pass
                    try:
                        messageToScreen(self.win, "{}".format(scores_hard[i]), 930,
                                        360 + i * 40)
                    except IndexError:
                        pass

                # dictionary_scores = sorting_scores.sorting(lista)
                # print(dictionary_scores)
                # iterations = 0
                # for key, value in dictionary_scores.items():
                # messageToScreen(self.win, "{} {}".format(key, value), 540, 250 + iterations*40)
                # iterations += 1
                # if iterations == 10:
                # break
                # messageToScreen(self.win, sorting_scores.sorting(scores_easy.split("\n")), 540, 250)
                # sorting_scores.sorting(scores_easy)
                # print(scores_easy)

                # for score in scores_easy:
                # messageToScreen(self.win, score, 540, 250)

    def start(self):  # funkcja odpowiedzialna za odpalenie i wyłączenie gry
        pg.init()
        pg.display.set_caption("Mistrz klawiatury")
        pg.time.delay(60)
        run = True
        counter = 60
        pg.time.set_timer(pg.USEREVENT, 1000)



        while run:

            Game.redrawWindow(self, self.mode)
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    run = False
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
                        self.click_check = True
                        self.mode = "menu"


                    elif self.plr2_button.isOver(pos):
                        if list[1] == '':
                            pass
                        else:
                            self.act_player = list[1]
                            self.click_check = True
                            self.mode = "menu"


                    elif self.plr3_button.isOver(pos):
                        if list[2] == '':
                            pass
                        else:
                            self.act_player = list[2]
                            self.click_check = True
                            self.mode = "menu"

                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "challenge":
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
                        if (self.mode == "start" or self.mode == "settings" or self.mode == "top scores"):
                            self.mode = "menu"
                        elif (self.mode == "challenge" or self.mode == "learning"):
                            self.input_text = ''
                            self.mode = "start"
                        elif (self.mode == "easy" or self.mode == "medium" or self.mode == "hard"):
                            self.mode = "challenge"

                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "menu" and not self.click_check:
                    if self.start_button.isOver(pos):
                        print("Pick difficulty:")
                        self.mode = "start"
                    elif self.settings_button.isOver(pos):
                        print("welcome in settings: ", self.language)
                        self.mode = "settings"
                    elif self.topscores_button.isOver(pos):
                        print("Welcome to top 10 scores. ")
                        self.mode = "top scores"
                    elif self.change_player_button.isOver(pos):
                        self.mode = "chs_plr"
                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "start":
                    if self.challenge_button.isOver(pos):
                        self.mode = "challenge"
                    elif self.learning_button.isOver(pos):
                        self.word_base = wb.words_reload("learning", self.language)
                        self.random_word = wb.get_randWord(self.word_base, self.previous_word)
                        self.mode = "learning"
                if event.type == pg.MOUSEBUTTONDOWN and (self.mode == "settings" or self.first_steps == 1):
                    if (self.polish_button.isOver(pos) and self.language == "english"):
                        Game.change_language(self, self.language)
                        pg.display.update()

                    if (self.english_button.isOver(pos) and self.language == "polish"):
                        Game.change_language(self, self.language)
                        pg.display.update()
                # print("wynik to ", self.score)

                if event.type == pg.MOUSEBUTTONDOWN and self.mode == "chs_plr":
                    if self.create_new_button.isOver(pos):
                        self.first_launch = True
                        self.first_steps = 2
                    if self.chs_ex_button.isOver(pos):
                        self.mode = "chs_ex"

                # część z mechaniki

                keys_names = ['1', '2', '3', '4','5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
                              'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'backspace', 'return'
                              ]

                if (event.type == pg.KEYDOWN and  pg.key.name(event.key) not in keys_names # wyjątki które nie powodują wpisania nazwy klawisza
                    and (
                    self.mode == "easy" or self.mode == "medium" or self.mode == "hard" or self.mode == "learning" or self.first_steps == 2 or self.mode == "save screen")
                ):
                    pass
                elif event.type == pg.KEYDOWN and pg.key.name(
                        event.key) == 'return' and self.first_steps != 2 and self.mode != "save screen":
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
                    if keys[pg.K_RSHIFT] or keys[pg.K_LSHIFT]:
                        self.input_text += letter.upper()
                    else:
                        self.input_text += letter


                elif keys[pg.K_LSHIFT] and event.type == pg.KEYDOWN:
                    ascii_code = ord(pg.key.name(event.key))
                    self.input_text += chr(ascii_code - 32)

                    # Zadziała przy pierwszym uruchomieniu gry i przy tworzeniu nowych profili graczy
                elif (event.type == pg.KEYDOWN and pg.key.name(
                        event.key) == 'return' and self.first_steps == 2):
                    try:
                        open("players/{player_name}_player.txt".format(player_name=self.input_text), "x")
                    except FileExistsError:
                        self.exist_error_check = True
                        open("players/{player_name}_player.txt".format(player_name=self.input_text), "a")
                    cnf = open('config/config.txt', "r")
                    lines = cnf.readlines()
                    cnf.close()

                    del lines[0]

                    cnf2 = open('config/config.txt', "w+")
                    cnf2.write("first launch = False")
                    cnf2.close()

                    if not self.exist_error_check:
                        base_update = open("config/players_list.txt", "a")
                        base_update.write(self.input_text + " ")
                        base_update.close()

                    self.first_launch = False
                    self.act_player = self.input_text
                    self.players_list = open("config/players_list.txt", "r+").readline().split(" ")
                    print(self.first_launch)
                    self.first_steps += 1
                    self.input_text = ""
                    self.mode = "menu"

                elif event.type == pg.KEYDOWN and pg.key.name(event.key) == "return" and self.mode == "save screen":
                    if self.save_difficulty == 1:
                        functions.add_result(self.act_player, self.score, 'easy')
                        self.score = 0
                        self.mode = "menu"
                    elif self.save_difficulty == 2:
                        functions.add_result(self.act_player, self.score, 'medium')
                        self.score = 0
                        self.mode = "menu"
                    else:
                        functions.add_result(self.act_player, self.score, 'hard')
                        self.score = 0
                        self.mode = "menu"


                elif (event.type == pg.KEYDOWN and pg.key.name(event.key) == 'backspace' and
                      (self.mode == "easy" or self.mode == "medium" or self.mode == "hard" or self.mode == "learning" or self.first_steps == 2 or self.mode == "save screen")):  # usuwanie liter
                    self.input_text = self.input_text[: len(self.input_text) - 1]

                elif (event.type == pg.KEYDOWN and ((
                 self.mode == "easy" or self.mode == "medium" or self.mode == "hard" or self.mode == "learning") or self.first_steps == 2 or self.mode == "save screen")):  # wpisywanie liter
                    # print(pg.key.name(event.key))
                    self.input_text += pg.key.name(event.key)

                if event.type == pg.USEREVENT and (
                        self.mode == "easy" or self.mode == "medium" or self.mode == "hard"):
                    counter -= 1
                    self.timer = counter

                if self.mode != "easy" and self.mode != "medium" and self.mode != "hard" and self.mode != "save screen":
                    counter = 60
                    self.timer = 60
                    self.score = 0

                if self.timer == 0:
                    self.mode = "save screen"
            self.clock.tick(80)
            pg.display.update()
