import sys
from cipher import read_file, write_file, bytes_to_bits, bits_to_bytes, decrypt

def cbc_decrypt(ciphertext, key, iv):
    ciphertext_bits = bytes_to_bits(ciphertext)
    key_bits = bytes_to_bits(key)
    iv_bits = bytes_to_bits(iv)
    plaintext_bits = []

    for i in range(0, len(ciphertext_bits), 16):
        block = ciphertext_bits[i:i + 16]
        decrypted_block = decrypt(block, key_bits)
        xor_block = [a ^ b for a, b in zip(decrypted_block, iv_bits)]
        plaintext_bits.extend(xor_block)
        iv_bits = block

    return bits_to_bytes(plaintext_bits)


ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
iv_file = sys.argv[3]
output_file = sys.argv[4]

ciphertext = read_file(ciphertext_file)
key = read_file(key_file)
iv = read_file(iv_file)

plaintext = cbc_decrypt(ciphertext, key, iv)
write_file(output_file, plaintext)
