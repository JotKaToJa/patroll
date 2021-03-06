import pygame
from Game.Scenes.Scene import Scene


class PlayingGameScene(Scene):
    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        #game.screen.blit()

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
