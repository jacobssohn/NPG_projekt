import pygame
import random

class mechanics:
    def __init__(self,win,bg):
        self.win = win
        self.bg = bg
        self.input_text = ''
        self.location_of_the_wanted_text = (random.randint(80, 700), random.randint(10, 580))  # położenie wylosowanego słowa
        self.words = ['mistrz', 'proton', 'alfabet'] # miejsce na prawidłowy słownik


    def checking_events(self, event):
            if ( event.type == pygame.KEYDOWN and # wyjątki które nie powodują wpisania nazwy klawisza
                 (
                pygame.key.name(event.key) == 'return' or
                pygame.key.name(event.key) == 'left ctrl' or
                pygame.key.name(event.key) == 'left alt' or
                pygame.key.name(event.key) == 'alt gr' or
                pygame.key.name(event.key) == 'right ctrl' or
                pygame.key.name(event.key) == 'left shift' or
                pygame.key.name(event.key) == 'right shift' or
                pygame.key.name(event.key) == 'space'
                 )
            ):
                pass
            elif (event.type == pygame.KEYDOWN and pygame.key.name(event.key) == 'backspace'): # usuwanie liter
                self.input_text = self.input_text[ : len(self.input_text) -1]
                self.win.fill((255, 255, 255))
            elif(event.type == pygame.KEYDOWN): # wpisywanie liter
                print(pygame.key.name(event.key))
                self.input_text += pygame.key.name(event.key)






    def draw_textinput(self):

        random_word = self.words[random.randint(0, 2)]
        if self.input_text == random_word:
            self.location_of_the_wanted_text = (random.randint(80, 700), random.randint(10, 580)) # losuje położenie tekstu na ekranie
            self.win.fill((255, 255, 255)) # wypełnia kolorem całe okno i zakrywa poprzednio napisany tekst
            self.win.blit(self.bg, (0, 0))

            random_word = self.words[random.randint(0, len(self.words)-1)] # losuje kolejne słowo
            self.input_text = '' # kasuje tekst


        font = pygame.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
        wanted_word_text = font.render(random_word, True, (100, 100, 150), (255, 255, 255))  # renderowanie wylosowanego słowa, pierwszy tuple to kolor liter, drugi to
        textRect_2 = wanted_word_text.get_rect()  # generowanie prostokąta na którym          # kolor pola tekstowego, teraz się zlewa z tłem i go nie widać
        textRect_2.center = self.location_of_the_wanted_text  # leży szukany tekst
        text = font.render(self.input_text, True, (100, 100, 150), (255, 255, 255))  # renderowanie wpisywanego tekstu
        textRect = text.get_rect()  # pole z wpisywanym tekstem i jego środek
        textRect.center = (720, 400)
        self.win.blit(text, textRect)  # nałożenie zrenderowanego tekstu na jego pole tekstowe
        self.win.blit(wanted_word_text, textRect_2)
        pygame.display.update()  # odświeżenie okna