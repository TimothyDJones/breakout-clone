from game import Game


if __name__ == "__main__":
    game = Game()
    while True:
        game.handle_events()
        game.update()
        game.draw()