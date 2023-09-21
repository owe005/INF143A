import sys
import hashlib

def read_binary_file(file):
    with open(file, 'rb') as f:
        return f.read()

def write_binary_file(file, data):
    with open(file, 'wb') as f:
        f.write(data)

# Computing HMAC-SHA256
def hmac_sha256(key, msg):
    block_size = 64
    outpad = bytes([0x5C] * block_size)
    inpad = bytes([0x36] * block_size)

    key_inpad = xor_bytes(key, inpad)
    key_outpad = xor_bytes(key, outpad)

    # Get final hash value
    inner_hash = hashlib.sha256(key_inpad + msg).digest()
    hmac_digest = hashlib.sha256(key_outpad + inner_hash).digest()

    return hmac_digest

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv) != 4:
        print("Usage: python hmac.py hash_in hash_key hash_out")
        sys.exit(1)

    else:
        # Parsing
        input_file = sys.argv[1]
        key_file = sys.argv[2]
        output_file = sys.argv[3]

        input_data = read_binary_file(input_file)
        key_data = read_binary_file(key_file)

        # Compute HMAC-SHA256
        mac = hmac_sha256(key_data, input_data)

        write_binary_file(output_file, mac)

        print("MAC generated successfully.")
