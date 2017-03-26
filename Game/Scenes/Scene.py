
class Scene:
    def __init__(self, game):
        self.__game = game
        self.__text = []

    def render(self):
        pass

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass