class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plaint_text, key):
        encrypt_text = ""
        key_index = 0
        for char in plaint_text:
            if char.isalpha():
                if char.isalpha():
                    key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                    if char.isupper():
                        encrypt_text += chr((ord(char) + key_shift - ord('A')) % 26 + ord('A'))
                    else:
                        encrypt_text += chr((ord(char) + key_shift - ord('a')) % 26 + ord('a'))
                    key_index += 1
                else:
                    encrypt_text += char
        return encrypt_text

    def vigenere_decrypt(self, encrypt_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypt_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - key_shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - key_shift - ord('a')) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text