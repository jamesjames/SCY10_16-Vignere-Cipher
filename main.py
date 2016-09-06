import sys

standardAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

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
    charList = list(inputText)
    for char in charList:
        if char in standardAlphabet:
            finalText = standardAlphabet[(standardAlphabet.index(char) + len(inputText)) % len(standardAlphabet)]
            sys.stdout.write(str(finalText))
        else:
            sys.stdout.write(str(char))

# -----------------------------------------------------------------------------------------------------------------------

print("Would You like to cipher or decipher text? (c / d)")
methodChoice = input("Enter Choice: ")

if methodChoice == 'c':
    textFileObject = open('encryptedData.txt', 'w')
    userInput = input("Enter text to be ciphered: ")
    cipher(userInput)
    textFileObject.close()

elif methodChoice == 'd':
    textFileObject = open('encryptedData.txt', 'r')
    decipher(textFileObject)
    textFileObject.close()