import pygame as pg
import random

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
            pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isOver(self, pos):
        # pos to pozycja myszy (pg.mouse.get_pos())
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


class word_base: #klasa do otwierania bazy słów i losowania nowego słowa

    @staticmethod
    def words_reload(mode: str, language: str) -> list:
        if language == 'polish' and mode != "learning":
            return open("word_base/{}_pol.txt".format(mode), "r", encoding='utf8').readline().split(" ")
        elif language == 'english' and mode != "learning":
            return open("word_base/{}_ang.txt".format(mode), "r", encoding='utf8').readline().split(" ")
        elif mode == "learning":
            return open("word_base/learning.txt", "r", encoding='utf8').readline().split(" ")


    @staticmethod
    def get_randWord(word_base: list, previous_word: str) -> str:
        rand = random.randint(0, len(word_base)-1)
        if previous_word is None:
            return word_base[rand]
        else:
            while word_base[rand] == previous_word:
                rand = random.randint(0, len(word_base) - 1)
            return word_base[rand]



