# Este código implementa a Cifra de Vigenère, um método de criptografia que utiliza uma palavra-chave para variar o deslocamento das letras no texto. 
# A cifra é uma técnica de substituição polialfabética, onde cada letra do texto é deslocada por uma quantidade determinada pela letra correspondente da palavra-chave. 
# O código abaixo permite criptografar e descriptografar uma mensagem usando uma palavra-chave fornecida.

def vigenere_encrypt(plaintext, keyword):
    encrypted = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():  # Verifica se é uma letra
            shift = ord(k.lower()) - ord('a')
            base = ord('a') if p.islower() else ord('A')
            encrypted_char = chr((ord(p) - base + shift) % 26 + base)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(p)  # Mantém caracteres não alfabéticos inalterados

    return ''.join(encrypted)

def vigenere_decrypt(ciphertext, keyword):
    decrypted = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():  # Verifica se é uma letra
            shift = ord(k.lower()) - ord('a')
            base = ord('a') if c.islower() else ord('A')
            decrypted_char = chr((ord(c) - base - shift) % 26 + base)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(c)  # Mantém caracteres não alfabéticos inalterados

    return ''.join(decrypted)

# Exemplo de uso
mensagem = "Ola Mundo!"
palavra_chave = "chave"
cifrada = vigenere_encrypt(mensagem, palavra_chave)
decifrada = vigenere_decrypt(cifrada, palavra_chave)

print("Mensagem Original:", mensagem)
print("Mensagem Cifrada:", cifrada)
print("Mensagem Decifrada:", decifrada)