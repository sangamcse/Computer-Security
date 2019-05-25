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
