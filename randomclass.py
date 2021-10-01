import random

print("Please give AI some data to learn...")


class GenerateRandom:
    def __init__(self):
        self.data = ''
        self.split = self.counts = self.probs = None
        self.bank = 1000
        self.test = ''
        self.prediction = ''

    def inputFilter(self, inputs):
        """inputFilter('user input', data or test)\n
        Filters only 0 and 1 from user input into a string"""
        self.data += ''.join(x for x in inputs if x in '01')
        return self.data

    def triadProb(self):
        """Splits input from user into four character slices, counts the number of 1 or 0
        for each triad, then calculate probability of 0 following a triad into a dict"""
        triads = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.split = [self.data[i: i + 4]
                      for i in range(0, len(self.data) - 3)]
        self.counts = {key: [self.data.count(
            key + '0'), self.data.count(key + '1')] for key in triads}
        self.probs = {key: (value[0] + 0.0001) / (value[0] + value[1] + 0.0001)
                      for key, value in self.counts.items()}

    def Predict(self):
        for i in range(3):
            self.prediction += random.choice('01')
        if len()

        # game = GenerateRandom()

        # while len(game.data) < 10:
        #     print(
        #         f'Current data length is {len(game.data)}, {10 - len(game.data)} symbols left')
        #     game.inputFilter(input('Print a random string containing 0 or 1: '))
        # print(f'Final data string:\n{game.data}')
