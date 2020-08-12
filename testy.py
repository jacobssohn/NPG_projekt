import pygame


def str_to_bool(s : str) -> bool:
    if s == 'True':
         return True
    elif s == 'False':
         return False

def get_player_nick(win, input_text):
    font = pygame.font.Font('freesansbold.ttf', 32)  # jakaś domyślna czcionka i rozmiar
    text = font.render(input_text, True, (100, 100, 150), (255, 255, 255))  # renderowanie wpisywanego tekstu
    textRect = text.get_rect()  # pole z wpisywanym tekstem i jego środek
    textRect.center = (540, 360)
    win.blit(text, textRect)  # nałożenie zrenderowanego tekstu na jego pole tekstowe
