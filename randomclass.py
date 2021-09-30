import random

print("Please give AI some data to learn...")


class GenerateRandom:

    def __init__(self):
        self.data = ''
        self.split = None
        self.counts = None
        self.probs = None
        self.bank = 1000

    def inputFilter(self, inputs):
        self.data += ''.join(x for x in inputs if x in '01')
        return self.data

    def triadProb(self):
        """Takes input from user, split into four character slices, counts them
        and then calculate probability for 0 or 1 following a triad into a dictionary."""
        triads = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.split = [self.data[i: i + 4]
                      for i in range(0, len(self.data) - 3)]
        self.counts = {key: [self.data.count(
            key + '0'), self.data.count(key + '1')] for key in triads}
        self.probs = {key: (value[0] + 0.0001) / (value[0] + value[1] + 0.0001)
                      for key, value in self.counts.items()}

        print(self.split)


game = GenerateRandom()


while len(game.data) < 10:
    print(
        f'Current data length is {len(game.data)}, {10 - len(game.data)} symbols left')
    game.inputFilter(input('Print a random string containing 0 or 1: '))

print(f'Final data string:\n{game.data}')

game.triadProb()

# print(f'Final data string:\n{final_data}\n')
# print(f'Current data length is {len(self.final_data)}, {10 - len(self.final_data)} symbols left')
# input_data = input('Print a random string containing 0 or 1: ')
