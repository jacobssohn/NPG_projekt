import pygame
import classes
import pygame_functions
button = classes.button

pygame.init()

win = pygame.display.set_mode((1080, 720))
interface = classes.Game(win)

interface.start()



