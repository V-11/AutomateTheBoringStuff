from pyinputplus import *

TotalCost = 0

Bread = inputMenu(['wheat', 'white', 'sourdough'])
if Bread == 'wheat':
    TotalCost += 1
elif Bread == 'white':
    TotalCost += 1.25
else:
    TotalCost += 1.5

Protein = inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if Protein == 'chicken':
    TotalCost += 1
elif Protein == 'turkey':
    TotalCost += 1.25
elif Protein == 'ham':
    TotalCost += 1.5
else:
    TotalCost += 1.75

Cheese = inputYesNo('Would you like some cheese? yes/no\n')
if Cheese == 'yes':
    CheeseType = inputMenu(['cheddar', 'swiss', 'mozzarella'])
    if CheeseType == 'cheddar':
        TotalCost += 1
    elif CheeseType == 'swiss':
        TotalCost += 1.25
    else:
        TotalCost += 1.5

Mayo = inputYesNo('Would you like some mayo? yes/no\n')
if Mayo == 'yes':
    TotalCost += 0.5

Mustard = inputYesNo('Would you like some mustard? yes/no\n')
if Mustard == 'yes':
    TotalCost += 0.5

Lettuce = inputYesNo('Would you like some lettuce? yes/no\n')
if Lettuce == 'yes':
    TotalCost += 0.5

Tomato = inputYesNo('Would you like some tomato? yes/no\n')
if Tomato == 'yes':
    TotalCost += 0.5

HowMany = inputInt('How many sandwiches would you like?\n', min=1)
TotalCost *= HowMany

print('Thank you for your visit, We hope to see you again :)')
print('Total Cost = $' + str(TotalCost))
