import os
import re

Files = []
for File in os.listdir('.'):
    if File.endswith('.txt'):
        Files.append(File)

InputExpression = input('What expression are you looking for?\n')
FindRegex = re.compile(InputExpression, re.I)

RegexFilesList = []

for FileName in Files:
    OpenFile = open(FileName)
    ReadFile = OpenFile.read()
    if FindRegex.search(ReadFile):
        RegexFilesList.append(FileName)

if RegexFilesList != []:
    print(RegexFilesList)
else:
    print('No Matches!')
