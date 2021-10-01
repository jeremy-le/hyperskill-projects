import random
from randomclass import GenerateRandom

game = GenerateRandom()

print("Please give AI some data to learn...")

while len(game.data) < 100:
    print(
        f'Current data length is {len(game.data)}, {100 - len(game.data)} symbols left')
    game.inputData(input('Print a random string containing 0 or 1: '))
print(f'Final data string:\n{game.data}')

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

game.triadProb()

play = ''
while play != 'enough':
    play = input('Print a random string containing 0 or 1: ')
    game.inputTest(play)
    if len(game.test) > 3:
        game.Predictor()
        print(f'Prediction:\n{game.prediction}')
        game.isMatch()
        print(
            f'Computer guessed right {game.correct} out of {len(game.test)} symbols ({round(game.correct / len(game.test), 2)}%)')
        print(f'Your balance is now ${game.bank}')
        game.data += game.test

print('Game Over')
