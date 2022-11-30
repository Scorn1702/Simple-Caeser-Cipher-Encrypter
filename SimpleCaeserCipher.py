# Simple Caeser Cipher encryption tool by Scorn1702
# Created Nov 28 2022

# variables
filename = input('enter filename: ')
shift = int(input('enter shift pattern: '))
result = ""

# open contents in file and read it
with open(filename) as f:
    contents = f.read()

    # logic to take the letter in the file and shift them according the users input
    numOfChars = len(contents)
    for i in range(numOfChars):
        char = contents[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    print(result)
