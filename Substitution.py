import random
random.seed(2003)
key = []
key.extend(random.sample('abcdefghijklmnopqrstuvwxyz',26))
key_pi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, key, key_pi):
    result = ""
    for char in text:
        if char.islower():
            char_in_key_pi = key_pi[key.index(char)]
            result += char_in_key_pi
        if char.isupper():
            index_in_key = key.index(char.lower())
            char_in_key_pi = key_pi[index_in_key].upper()
            result += char_in_key_pi
    return result


def decrypt(text, key_pi, key):
    result = ""
    for char in text:
        if char.islower():
            char_in_key = key[key_pi.index(char)]
            result += char_in_key
        if char.isupper():
            index_in_key_pi = key_pi.index(char.lower())
            char_in_key = key[index_in_key_pi].upper()
            result += char_in_key
    return result