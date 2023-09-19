import streamlit as st

def inverse(a, m):
    for x in range(1, m):
        if a * x % m == 1:
            return x


def encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                encrypted_char = (a * x + b) % 26
                result += chr(encrypted_char + ord('a'))
            elif char.isupper():
                x = ord(char) - ord('A')
                encrypted_char = (a * x + b) % 26
                result += chr(encrypted_char + ord('A'))
        else:
            result += char
    return result

def decrypt(text, a, b):
    result = ""
    a = inverse(a, 26)
    if a is not None:
        for char in text:
            if char.isalpha():
                if char.islower():
                    y = ord(char) - ord('a')
                    decrypted_char = (a * (y - b)) % 26
                    result += chr(decrypted_char + ord('a'))
                elif char.isupper():
                    y = ord(char) - ord('A')
                    decrypted_char = (a * (y - b)) % 26
                    result += chr(decrypted_char + ord('A'))
            else:
                result += char
    else: 
        st.error("Không tìm được giá trị")
    return result
