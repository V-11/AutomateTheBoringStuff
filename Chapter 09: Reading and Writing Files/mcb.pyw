import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    elif sys.argv[1].lower() == 'erase':
        for keyword in list(mcb_shelf.keys()):
            del mcb_shelf[keyword]

mcb_shelf.close()
