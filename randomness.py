"""
Generating randomness
"""
import random
# current = len(final_data)
# remain = 100 - len(final_data)

print("Please give AI some data to learn...")


def datastring():
    final_data = ''
    while len(final_data) < 10:
        print(
            f'Current data length is {len(final_data)}, {10 - len(final_data)} symbols left')
        input_data = input('Print a random string containing 0 or 1: ')
        final_data += ''.join(x for x in input_data if x in '01')
    return final_data


final_data = datastring()

print(f'Final data string:\n{final_data}\n')

#########################################################################

# Creates a list of four character slices for each character
split_data = [final_data[i: i + 4]
              for i in range(0, len(final_data) - 3)]  # - 3 removes lagging slices
# Creates a list of triads for use in the next two dictionaries.
triads = ['000', '001', '010', '011', '100', '101', '110', '111']
# Count slices that end with 0 or 1 for each triad.
triad_counts = {key: [split_data.count(
    key + '0'), split_data.count(key + '1')] for key in triads}
# Creates a dictionary mapping the probability of 0 for each triad.
# Add 0.0001 to each value to avoid DivisionByZero.
triad_prob = {key: (value[0] + 0.0001) / (value[0] + value[1] + 0.0001)
              for key, value in triad_counts.items()}
# This is another solution to DivisionByZero using if/else statement.
# triad_prob = {key: value[0] / (value[0] + value[1]) if value[0] +
#               value[1] != 0 else 0.5 for key, value in triad_counts.items()}

#########################################################################

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

final_test = ''
while True:
    game_over = False
    input_test = input('Please enter a test string containing 0 or 1: ')
    final_test = final_test.join(x for x in input_test if x in '01')
    if input_test.lower() == 'enough':
        game_over = True
        print('Game over!')
        break
    elif len(final_test) < 3:  # Must be at least three characters long or prediction doesn't work
        print('Must enter at least three valid characters (0 or 1).')
    else:
        print(final_test)
        break

while not game_over:
    # Chooses first three characters in prediction string with random module
    prediction = ''
    for i in range(3):
        prediction += random.choice('01')
    if len(final_test) > 3:
        # Adds 0 or 1 to prediction based on the mapping of user input and probability dictionary
        # - 3 ensures length of prediction matches user string
        for i in range(len(final_test) - 3):
            if triad_prob[final_test[i: i + 3]] > 0.5:
                prediction += '0'
            elif triad_prob[final_test[i: i + 3]] < 0.5:
                prediction += '1'
            else:  # if 50/50, uses random to select
                prediction += random.choice('01')
    else:
        print(f'Prediction:\n{prediction}')
    break
