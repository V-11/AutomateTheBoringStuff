def Joiner(user_list):                                    #Declare function
    if user_list == []:                                   #Check if the list is empty
        print('You must add elements!!')
        exit()                                            #If it's empty it will exit the program so it won't crash
    else:
        for i in range(len(user_list)-1):                 #Iterate over all elements except the last one
            print(user_list[i] + ', ', end='')            #Separate and append elements
        print('and ' + user_list[i+1])                    #Append the last element

user_list = []                                            #Declare the user input list
print ('To exit the program press enter')
while True:
    element = input('Add an element to the list: ')
    if element != '':                                     #Check if it's not empty
        user_list.append(element)                         #Append the new element to the list
    else:
        break                                             #It will exit the loop if the user add an empty element

Joiner(user_list)                                         #Passing the list to the function
