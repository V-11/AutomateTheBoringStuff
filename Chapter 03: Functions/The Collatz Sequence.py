def collatz(number):
    if number % 2 == 0:          #check if it's even
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:        #check if it's odd
        result = 3 * number + 1
        print(result)
        return result

try:
    user_input = int(input("Enter an integer: "))
except ValueError:
    print('You must enter an integer!!')
    exit()

while user_input != 1:
    user_input = collatz(user_input)       #the returned value will be stored in user_input until the condition is satisfied
