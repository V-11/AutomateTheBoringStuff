import re

FileName = str(input('Enter the name of the file you want to edit: (Ex: test.txt)\n'))
if FileName.endswith(".txt"):
    pass
else:
    print("Wrong File Format!")
    exit()

MadFile = open(FileName, 'r')
MadFileContent = MadFile.read()

MadRegex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
MadMatches = MadRegex.findall(MadFileContent)

for Match in MadMatches:
    Edit = input('Enter a word to replace ' + Match + ': ')
    MadFileContent = MadFileContent.replace(Match, Edit, 1)

NewMadFile = open('NewMadFile.txt', 'w')
NewMadFile.write(MadFileContent)
MadFile.close()
NewMadFile.close()
print("Changes wrote to NewMadFile.txt")
