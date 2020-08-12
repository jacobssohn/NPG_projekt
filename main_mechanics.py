# -*- coding: utf-8 -*-
import pygame
import random


def main():
    pygame.init()

    slowa = ['mistrz', 'proton', 'alfabet'] # miejsce na prawidłowy słownik

    win = pygame.display.set_mode((800, 600)) # główne okno programu wraz z rozdzielczością
    pygame.display.set_caption("Gra na NPG") # nazwa okna

    win.fill((255, 255, 255)) # początkowy kolor całego okna

    correct = False
    random_word = slowa[random.randint(0,2)] # losowanie losowego słowa, które gracz ma wpisać
    input_text = ''
    location_of_the_wanted_text = (random.randint(80, 700), random.randint(10, 580)) # położenie wylosowanego słowa

    run = True
    while run: # główna pętla programu
        pygame.time.delay(60) # czas zajmujący programowi wykonanie akcji

        for event in pygame.event.get(): # wyjście z programu
            if event.type == pygame.QUIT:
                run = False

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
                input_text = input_text[ : len(input_text) -1]
                win.fill((255, 255, 255))
            elif(event.type == pygame.KEYDOWN): # wpisywanie liter
                print(pygame.key.name(event.key))
                input_text += pygame.key.name(event.key)

        if input_text == random_word:
            location_of_the_wanted_text = (random.randint(80, 700), random.randint(10, 580)) # losuje położenie tekstu na ekranie
            win.fill((255, 255, 255)) # wypełnia kolorem całe okno i zakrywa poprzednio napisany tekst
            random_word = slowa[random.randint(0, len(slowa)-1)] # losuje kolejne słowo
            input_text = '' # kasuje tekst

        while True:
            if abs(location_of_the_wanted_text[0] - 400) < 50 or abs(location_of_the_wanted_text[1] - 300) < 30: # pętla sprawdza czy słowo do wpisania
                location_of_the_wanted_text = (random.randint(80, 700), random.randint(10, 580))                 # nie pojawia się za blisko wpisywanego tekstu
            else:
                break

        font = pygame.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
        wanted_word_text = font.render(random_word, True, (100, 100, 150), (255, 255, 255))  # renderowanie wylosowanego słowa, pierwszy tuple to kolor liter, drugi to
        textRect_2 = wanted_word_text.get_rect() # generowanie prostokąta na którym          # kolor pola tekstowego, teraz się zlewa z tłem i go nie widać
        textRect_2.center = location_of_the_wanted_text # leży szukany tekst
        text = font.render(input_text, True, (100, 100, 150), (255, 255, 255)) # renderowanie wpisywanego tekstu
        textRect = text.get_rect()    # pole z wpisywanym tekstem i jego środek
        textRect.center = (400, 300)
        win.blit(text, textRect) # nałożenie zrenderowanego tekstu na jego pole tekstowe
        win.blit(wanted_word_text, textRect_2)
        pygame.display.update() # odświeżenie okna

    pygame.display.quit()
    pygame.quit()

main()