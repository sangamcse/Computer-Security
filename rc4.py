msg = map(int, input("Enter the message: ").split(" "))
key = map(int, input("Enter key: ").split(" "))

s = [0]*8
t = []
for i in range(8):
    s[i] = i
    t.append(key[i % len(key)])

j = 0


for i in range(8):
  j = (j+s[i]+t[i]) % 8
  temp = s[i]
  s[i] = s[j]
  s[j] = temp


i = j = 0
c = []
x = []
for _ in range(len(msg)):
    i = (i+1)%8
    j = (j+s[i])%8
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    k = (s[i] + s[j])%8
    x.append(s[k])
    c.append(msg[i] ^ s[k])
cipher = ' '.join(map(str,c))
print(cipher)

for i in range(len(c)):
    print(c[i] ^ x[i],)
