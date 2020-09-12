import pygame
import Interface


pygame.init()

win = pygame.display.set_mode((1080, 720))
interface = Interface.Game(win)

interface.start()





