# p = 5
# q = 7
# N = p*q
# phi = (p-1)*(q-1)
# e = 5

# P = [N, e]

# d = 8
# while e*d % phi != 1:
#     d = d+1

# S = [N, d]

# # print(d)
# # print((e*d)%24)

# m = 19
# c = (m**e) % N
# print(c) #зашифрованное сообщение

# m = (c**d) % N
# print(m) #расшифрованное сообщение



# text = "привет"
# byte_data = text.encode('utf-8')
# number = int.from_bytes(byte_data, byteorder='big')
# print(number)
# p = 61
# q = 53
# N = p*q
# phi = (p-1)*(q-1)
# e = 17

# d = pow(e, -1, phi)

# c = (number**e) % N 
# print("зашифрованное сообщение: ", c)

# m = (c**d) % N
# print("расшифрованное сообщение в числовом виде: ", m)








