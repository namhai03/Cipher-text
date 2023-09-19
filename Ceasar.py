
def encrypt(text,k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        elif char == " ":
            result += char
        elif (char.islower()):
            result += chr((ord(char) + k - 97) % 26 + 97)
        else: result += char
    return result

def decrypt(text, k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - k - 65) % 26 + 65)
        elif char == " ":
            result += char
        elif (char.islower()):
            result += chr((ord(char) + k - 97) % 26 + 97)
        else: result += char
    return result
