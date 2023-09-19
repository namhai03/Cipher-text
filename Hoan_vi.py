import random 

def take_key(m):
    random.seed(2003)
    key = random.sample([i for i in range(m)], m)
    key = [[i for i in range(m)], key]
    return key

def split_text (text, m):
    text_splited= []
    while len(text) % m !=0 :
        text += " " 
    for i in range(0, len(text), m):
        text_splited.append(text[i:i+m])
    return text_splited

def encrypt(text, key):
    text_splited = split_text(text, len(key[0]))
    result = ""
    for i in text_splited:
        for j in range(len(key[0])):
            result += i[key[1][j]]
    return result

def decrypt(text, key):
    text_splited = split_text(text, len(key[0]))
    key_sorted = sorted(zip(key[1], key[0]))
    key[0], key[1] = zip(*key_sorted)

    key[1] = list(key[1])
    key[0] = list(key[0])
    
    result = ""
    for i in text_splited:
        for j in range(len(key[0])):
            result += i[key[1][j]]
    return result