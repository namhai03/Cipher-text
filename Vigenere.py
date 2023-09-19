def take_key(text):
    result= []
    for i in range(len(text)):
        if(text[i].isupper()): 
            result.append(ord(text[i])-65)
        else:
            result.append(ord(text[i])-97)
    return result

def encrypt(text, m, k):
    result = ""
    index = 0
    while index < len(text):
        for i in range(m):
            if index >= len(text):
                break
            char = text[index]
            if char.isupper():
                result += chr((ord(char) + k[i] - 65) % 26 + 65)
            if char.islower():
                result += chr((ord(char) + k[i] - 97) % 26 + 97)
            index += 1
    return result

def decrypt(text, m, k):
    result = ""
    index = 0
    while index < len(text):
        for i in range(m):
            if index >= len(text):
                break
            char = text[index]
            if char.isupper():
                result += chr((ord(char) - k[i] - 65) % 26 + 65)
            if char.islower():
                result += chr((ord(char) - k[i] - 97) % 26 + 97)
            index += 1
    return result

