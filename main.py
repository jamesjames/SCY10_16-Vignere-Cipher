import sys

standardAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789,."><?!/{}[]-_=+*@#$%^&*()'
textFileObject = ''

def cipher(inputText):
    charList = list(inputText)
    sys.stdout.write("Ciphered Text: ")
    for char in charList:
        if char in standardAlphabet:
            finalText = standardAlphabet[(standardAlphabet.index(char) + len(inputText)) % len(standardAlphabet)]
            textFileObject.write(str(finalText))
            sys.stdout.write(str(finalText))
        else:
            textFileObject.write(str(char))
            sys.stdout.write(str(char))

def decipher(inputText):
    sys.stdout.write("Deciphered Text: ")
    for char in inputText:
        if char in standardAlphabet:
            sys.stdout.write(str(standardAlphabet[(standardAlphabet.index(char) - len(inputText)) % len(standardAlphabet)]))
        else:
            sys.stdout.write(str(char))

# ----------------------------------------------------------------------------------------------------------------------

print("Would You like to cipher or decipher text? (c / d)")
methodChoice = input("Enter Choice: ")

if methodChoice == 'c':
    textFileObject = open('encryptedData.txt', 'w')
    userInput = input("Enter text to be ciphered: ")
    cipher(userInput)
    textFileObject.close()

elif methodChoice == 'd':
    textFileObject = open('encryptedData.txt', 'r')
    decipher(textFileObject.read())
    textFileObject.close()