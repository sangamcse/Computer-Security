msg = map(int, input("Enter the message: ").split(" "))
key = map(int, input("Enter key: ").split(" "))


encrypted = []
decrypted = []
for i in range(len(msg)):
    encrypted.append(msg[i] ^ key[i%len(key)])

e = ' '.join(map(str,encrypted))

print("Encrypted message: " + e)

for j in range(len(encrypted)):
    decrypted.append(encrypted[j] ^ key[j%len(key)])

d = ' '.join(map(str,decrypted))

print("Decrypted message: " + d)
