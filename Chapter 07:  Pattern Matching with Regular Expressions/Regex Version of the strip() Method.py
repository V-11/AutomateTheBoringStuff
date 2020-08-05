import re

String = input('Enter a string you want to edit: ')
Character = input('Enter a character you want to remove: (blank to strip)')

def RegStrip(String, Character):
    if Character == '':
        SearchRegex = re.compile(' +')
        EditedString = SearchRegex.sub('', String)
        print(EditedString)
    else:
        SearchRegex = re.compile(Character)
        EditedString = SearchRegex.sub('', String)
        print(EditedString)

EditedString = RegStrip(String, Character)
