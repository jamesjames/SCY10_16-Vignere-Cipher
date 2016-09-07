# imports sys to enable writing to stdout as opposed to
import sys

# standard list of characters that the cipher can scramble
standardAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789,."><?!/{}[]-_=+*@#$%^&*()'

# declares the variable that will be the object used as the text file in the cipher() and decipher() functions
textFileObject = ''

# cipher() ciphers the text
def cipher(inputText):
    sys.stdout.write("Ciphered Text: ")

    # begins for loop that iterates through each character in the string passed into the function
    for char in inputText:
        # if statement to check whether the character currently being passed in by the loop is in standardAlphabet
        if char in standardAlphabet:

            # the following line is what actually ciphers the text
            finalText = standardAlphabet[(standardAlphabet.index(char) + len(inputText)) % len(standardAlphabet)]

            # writes ciphered character to encryptedData.txt
            textFileObject.write(str(finalText))

            # prints ciphered text
            sys.stdout.write(str(finalText))
        else:
            # writes non ciphered character to text file
            textFileObject.write(str(char))

            # prints unciphered character
            sys.stdout.write(str(char))

# decipher() deciphers the text found on the first line of encryptedData.txt
def decipher(inputText):
    sys.stdout.write("Deciphered Text: ")

    # begins for loop that iterates through each character in the text file passed into the function
    for char in inputText:

        # if statement to check whether character being passed in by the loop is in standardAlphabet
        if char in standardAlphabet:

            # deciphers the text, prints it out
            sys.stdout.write(str(standardAlphabet[(standardAlphabet.index(char) - len(inputText)) % len(standardAlphabet)]))
        else:
            # prints non ciphered character out, as it is not in standardAlphabet
            sys.stdout.write(str(char))

# ----------------------------------------------------------------------------------------------------------------------

# asks user whether or not they would like to cipher or decipher text
print("Would You like to cipher or decipher text? (c / d)")
methodChoice = input("Enter Choice: ")

# excecuted if user inputs 'c', it allows them to cipher some text
if methodChoice == 'c':
    # initiates text file writing object
    textFileObject = open('encryptedData.txt', 'w')

    # takes user input
    userInput = input("Enter text to be ciphered: ")

    # passes user input into the cipher function
    cipher(userInput)

    # closes text file to avoid errors in reading and writing later on
    textFileObject.close()

# excecuted if user inputs 'd', it allows them to decipher the text in the first line of encryptedData.txt
elif methodChoice == 'd':
    # initiates text file reading object
    textFileObject = open('encryptedData.txt', 'r')

    # passes data from the first line in encryptedData.txt
    decipher(textFileObject.read())

    # closes text file to avoid errors in reading and writing later on
    textFileObject.close()