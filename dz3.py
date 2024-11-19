def euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    gcd, x1, y1 = euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (gcd, x, y)

def encrypt_character(char, e, n):
    m = ord(char)  
    c = pow(m, e, n)  
    return c

def decrypt_character(c, d, n):
    m = pow(c, d, n) 
    return chr(m)  


p = 101
q = 103 
n = p * q  # n = 10403
phi_n = (p - 1) * (q - 1)
e = 65537 
print(f"Открытый ключ: ({n}, {e})")


gcd, d, _ = euclid(e, phi_n)
d = d % phi_n
print(f"Закрытый ключ: ({n}, {d})")


message = "Ура, я студент ИТИСа!"
print(f"Расшифрованное сообщение: {message}")
text = []

for char in message:
    encrychar = encrypt_character(char, e, n)
    text.append(encrychar)

print(f"Зашифрованное сообщение: {text}")


decrypted_message = ""

for encrypted_char in text:
    decrypted_char = decrypt_character(encrypted_char, d, n)
    decrypted_message += decrypted_char

print(f"Расшифрованное сообщение: {decrypted_message}")

