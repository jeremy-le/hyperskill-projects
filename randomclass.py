import random

print("Please give AI some data to learn...")


class GenerateRandom:

    def __init__(self):
        self.data = ''
        self.bank = 1000

    def inputFilter(self, inputs):
        self.data += ''.join(x for x in inputs if x in '01')
        return self.data


game = GenerateRandom()


while len(game.data) < 10:
    print(
        f'Current data length is {len(game.data)}, {10 - len(game.data)} symbols left')
    game.inputFilter(input('Print a random string containing 0 or 1: '))

print(f'Final data string:\n{game.data}\n')

# print(len(game.data))

# game.inputfilter(input('Print a random string containing 0 or 1: '))

# print(game.data)

# game.inputfilter(input('Print a random string containing 0 or 1: '))
# print(game.data)


# print(f'Final data string:\n{final_data}\n')
# print(f'Current data length is {len(self.final_data)}, {10 - len(self.final_data)} symbols left')
# input_data = input('Print a random string containing 0 or 1: ')
