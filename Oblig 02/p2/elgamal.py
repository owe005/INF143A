import sys
import random
import hashlib
from math import gcd

def inverse_mod(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def generate_k(p):
    k = random.randint(1, p - 1)
    while gcd(k, p - 1) != 1:
        k = random.randint(1, p - 1)
    return k

def hash_message(message):
    hash_obj = hashlib.sha256()
    hash_obj.update(str(message).encode())
    hash_int = int(hash_obj.hexdigest(), 16)
    return hash_int

def sign_message(p, g, beta, d, message):
    k = generate_k(p)
    r = pow(g, k, p)
    k_inv = inverse_mod(k, p - 1)
    message_hash = hash_message(message)
    s = (k_inv * (message_hash - d * r)) % (p - 1)
    return r, s

def verify_signature(p, g, beta, r, s, message):
    if r < 1 or r > p - 1:
        return False
    message_hash = hash_message(message)
    v1 = pow(beta, r, p) * pow(r, s, p) % p
    v2 = pow(g, message_hash, p)
    return v1 == v2

def main():
    if len(sys.argv) != 5:
        print('Usage: python elgamal.py parameters private_key message output')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        p = int(f.readline())
        g = int(f.readline())
        beta = int(f.readline())

    with open(sys.argv[2], 'r') as f:
        d = int(f.readline())

    with open(sys.argv[3], 'r') as f:
        message = int(f.readline())

    r, s = sign_message(p, g, beta, d, message)

    with open(sys.argv[4], 'w') as f:
        f.write(f'{r}\n{s}\n')

    if verify_signature(p, g, beta, r, s, message):
        print('Signature is valid')
    else:
        print('Signature is invalid')

if __name__ == '__main__':
    main()
