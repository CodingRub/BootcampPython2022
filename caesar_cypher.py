import string

def encrypt(alpha: list, text: str, shift: int) -> str:
    res = ""
    for letter in text:
        if letter == " ":
            res += " "
        else:
            s = int(alpha.index(letter))+shift
            if s > len(alpha):
                s = s - len(alpha)
            res += alpha[s]
    return res

def decrypt(alpha: list, text: str, shift: int) -> str:
    res = ""
    for letter in text:
        if letter == " ":
            res += " "
        else:
            s = int(alpha.index(letter))-shift
            if s < 0:
                s = s + len(alpha)
            res += alpha[s]
    return res

def main():
    again = True
    alphabet = list(string.ascii_lowercase)
    while again:
        choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower())
        while not(choice == "encode" or choice == "decode"):
            choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower())

        text = input("Type your message:\n")
        print(type(text))
        while not(type(text) == str):
            print("Please enter your message, not numbers")
            text = input("Type your message:\n").lower()

        shift = int(input("Type the shift number:\n"))
        while not(type(shift) == int):
            print("Please enter a shift number")
            text = str(input("Type the shift number:\n").lower())
        if choice == "encode":
            encode = encrypt(alphabet, text, shift)
            print("Here's the encoded message: " + encode)
        else:
            decode = decrypt(alphabet, text, shift)
            print("Here's the decoded message: " + decode)
        close = str(input("Type 'y' to start again, type 'n' to stop:\n").lower())
        while not(close == "y" or close == "n"):
            close = str(input("Type 'y' to start again, type 'n' to stop:\n").lower())
        if close == "n":
            again = False
            print("Goodbye !")

if __name__ == "__main__":
    main()