## Assignment Computer Security

### 1. One Time Pad
---

```py
import string


abc = string.ascii_lowercase
one_time_pad = list(abc)


def encrypt(msg, key):
    '''
    Method to encrypt message using OTP.

    :param msg: Plain message to encrypt
    :param key: Key of encryption
    :return:    Encrypted cypher text
    '''

    ciphertext = ''
    for idx, char in enumerate(msg):
        charIdx = abc.index(char)
        keyIdx = one_time_pad.index(key[idx])

        cipher = (keyIdx + charIdx) % len(one_time_pad)
        ciphertext += abc[cipher]

    return ciphertext


def decrypt(ciphertext, key):
    '''
    Method to decrypt message using OTP.

    :param ciphertext: Cypher text to decrypt
    :param key: Key of decryption
    :return:    Decrypted plain text
    '''

    if ciphertext == '' or key == '':
        return ''

    charIdx = abc.index(ciphertext[0])
    keyIdx = one_time_pad.index(key[0])

    cipher = (charIdx - keyIdx) % len(one_time_pad)
    char = abc[cipher]

    return char + decrypt(ciphertext[1:], key[1:])
```

### 2. Stream Cipher
---

```py
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
```

### 3. RC4
---

```py
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
```

### 4. RSA
---

```py
def rsa_algo(p: int, q: int, msg: str):
    n = p * q
    z = (p-1)*(q-1)

    e = find_e(z)
    d = find_d(e, z)

    cypher_text = ''
    for ch in msg:
        cypher_text += chr((ord(ch) ** e) % n)

    plain_text = ''
    for ch in cypher_text:
        plain_text += chr((ord(ch) ** d) % n)

    return cypher_text, plain_text


def find_e(z: int):
    e = 2
    while e < z:
        if gcd(e, z) is 1:
            return e
        e += 1


def find_d(e: int, z: int):
    d = 2
    while d < z:
        if ((d*e) % z) is 1:
            return d
        d += 1


def gcd(x: int, y: int):
    small, large = (x, y) if x<y else (y,x)

    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large
```

### 5. ECC
---

```py
class Point:
    b = 7
    def __init__(self, x=float('inf'), y=float('inf')):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def is_zero(self):
        return self.x > 1e20 or self.x < -1e20

    def neg(self):
        return Point(self.x, -self.y)

    def dbl(self):
        if self.is_zero():
            return self.copy()
        try:
            L = (3 * self.x * self.x) / (2 * self.y)
        except ZeroDivisionError:
            return Point()
        x = L * L - 2 * self.x
        return Point(x, L * (self.x - x) - self.y)

    def add(self, q):
        if self.x == q.x and self.y == q.y:
            return self.dbl()
        if self.is_zero():
            return q.copy()
        if q.is_zero():
            return self.copy()
        try:
            L = (q.y - self.y) / (q.x - self.x)
        except ZeroDivisionError:
            return Point()
        x = L * L - self.x - q.x
        return Point(x, L * (self.x - x) - self.y)

    def mul(self, n):
        p = self.copy()
        r = Point()
        i = 1
        while i <= n:
            if i&n:
                r = r.add(p)
            p = p.dbl()
            i <<= 1
        return r
 
    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)

def show(s, p):
    print(s, "Zero" if p.is_zero() else p)
 
def from_y(y):
    n = y * y - Point.b
    x = n**(1./3) if n>=0 else -((-n)**(1./3))
    return Point(x, y)

a = from_y(1)
b = from_y(2)
show("a =", a)
show("b =", b)
c = a.add(b)
show("c = a + b =", c)
d = c.neg()
show("d = -c =", d)
show("c + d =", c.add(d))
show("a + b + d =", a.add(b.add(d)))
show("a * 12345 =", a.mul(12345))
```
### 6. Diffie-Hellman Key Exchange Algorithm

```c
/* Diffie-Hellman Key exchange algorithm */
#include<stdio.h>
#include<math.h>

long long int power(long long int a, long long int b, long long int P) {
    if (b == 1)
        return a;

    else return (((long long int)pow(a, b)) % P);
}

int main() {
    long long int P, G, x, a, y, b, ka, kb;

    // Both the persons will be agreed upon the
    // public keys G and P
    P = 23; // A prime number P is taken
    printf("The value of P : %lld\n", P);

    G = 9; // A primitve root for P, G is taken
    printf("The value of G : %lld\n\n", G);

    // Alice will choose the private key a
    a = 4; // a is the chosen private key
    printf("The private key a for Alice : %lld\n", a);
    x = power(G, a, P); // gets the generated key

    // Bob will choose the private key b
    b = 3; // b is the chosen private key
    printf("The private key b for Bob : %lld\n\n", b);
    y = power(G, b, P); // gets the generated key
    // Generating the secret key after the exchange
    // of keys
    ka = power(y, a, P); // Secret key for Alice
    kb = power(x, b, P); // Secret key for Bob

    printf("Secret key for the Alice is : %lld\n", ka);
    printf("Secret Key for the Bob is : %lld\n", kb);

    return 0;
}
```
