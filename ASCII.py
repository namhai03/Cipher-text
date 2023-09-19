def encrypt(text,k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char)+k)%256)
    return result

def decrypt(text, k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char)-k+256)%256)
    return result 