import pygame
from Game import GameConstans
from Game.Scenes import *

class GameController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Patroll - how to pygame")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstans.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            MenuScene(self)
        )
        self.__currentScene = 0

    def start(self):
        while 1:
            self.__clock.tick(100)
            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()


GameController().start()