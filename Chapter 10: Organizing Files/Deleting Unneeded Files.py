#This snippet doesn't delete files as the author asked, it only prints files larger than 100MB.

import os

while True:
    try:
        Directory = input('Enter the directory path you want to search in: \n')
        os.chdir(Directory)
        Directory = os.path.abspath('.')
        break
    except FileNotFoundError:
        print('Path does not exist.. Try again.')

for FolderName, SubFolders, Files in os.walk('.'):
    for File in Files:
        File = os.path.join(FolderName, File)
        size = os.path.getsize(File)
        if size > 100000000:
            print("Size of " + os.path.abspath(File) + " is " + str(size) + " bytes.")
