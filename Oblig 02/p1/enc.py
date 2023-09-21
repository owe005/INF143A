import sys
from cipher import read_file, write_file, bytes_to_bits, bits_to_bytes, encrypt

def cbc_encrypt(plaintext, key, iv):
    plaintext_bits = bytes_to_bits(plaintext)
    key_bits = bytes_to_bits(key)
    iv_bits = bytes_to_bits(iv)
    ciphertext_bits = []

    for i in range(0, len(plaintext_bits), 16):
        block = plaintext_bits[i:i + 16]
        xor_block = [a ^ b for a, b in zip(block, iv_bits)]
        encrypted_block = encrypt(xor_block, key_bits)
        ciphertext_bits.extend(encrypted_block)
        iv_bits = encrypted_block

    return bits_to_bytes(ciphertext_bits)


plaintext_file = sys.argv[1]
key_file = sys.argv[2]
iv_file = sys.argv[3]
output_file = sys.argv[4]

plaintext = read_file(plaintext_file)
key = read_file(key_file)
iv = read_file(iv_file)

ciphertext = cbc_encrypt(plaintext, key, iv)
write_file(output_file, ciphertext)
