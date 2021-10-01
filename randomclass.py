import random

print("Please give AI some data to learn...")


class GenerateRandom():
    def __init__(self):
        self.test = ''
        self.data = ''
        self.split = self.counts = self.probs = None
        self.bank = 1000
        self.prediction = ''

    def inputData(self, inputs):
        """inputFilter('user input', data or test)\n
        Filters only 0 and 1 from user input into a string"""
        self.data += ''.join(x for x in inputs if x in '01')
        return self.data

    def inputTest(self, inputs):
        self.test += ''.join(x for x in inputs if x in '01')
        return self.test

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

    def Predictor(self):
        """Makes a prediction based on probability dictionary"""
        for i in range(3):
            self.prediction += random.choice('10')
        if len(self.test) > 3:
            for i in range(len(self.test) - 3):
                triadkey = self.probs[self.test[i: i + 3]]
                if triadkey > 0.5:
                    self.prediction += '0'
                elif triadkey < 0.5:
                    self.prediction += '1'
                else:
                    self.prediction += random.choice('01')

    def isMatch(self):
        self.correct = 0
        for i in range(len(self.test)):
            if self.test[i] == self.prediction[i]:
                self.correct += 1


# Calculates percentage of correct guesses
# percentage = round(correct / len(final_test) * 100, 2)
# print(f'Computer guessed right {correct} out of {len(final_test)} symbols ({percentage} %)')


game = GenerateRandom()
game.inputData(
    '010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011')
game.triadProb()
game.inputTest('001010101010100110110100101')
game.Predictor()

# game.data
# game.test
# game.probs
# game.prediction

# def Predict(self):
#     for i in range(3):
#         self.prediction += random.choice('01')
#     if len()

# game = GenerateRandom()

# while len(game.data) < 10:
#     print(
#         f'Current data length is {len(game.data)}, {10 - len(game.data)} symbols left')
#     game.inputData(input('Print a random string containing 0 or 1: '))
# print(f'Final data string:\n{game.data}')
