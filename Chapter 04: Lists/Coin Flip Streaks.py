import random

NumberOfStreaks = 0
flips = []

for ExperimentNumber in range(10000):
    for i in range(100):
        if random.randint(0,1) == 0:
            flips.append('H')
        else:
            flips.append('T')

    for j in range(100):
        if flips[j:j+6] == ['H','H','H','H','H','H']:
            NumberOfStreaks += 1
        elif flips[j:j+6] == ['T','T','T','T','T','T']:
            NumberOfStreaks += 1

print('Chance of streak: %s%%' % (NumberOfStreaks / (100*10000)))
