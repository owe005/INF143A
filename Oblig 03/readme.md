# INF143A Mandatory Assignment 03
#### Ole Kristian Westby | owe009@uib.no
---
## Problem 1
I implemented this HMAC construction with the SHA256 hash function. You can test it by running:

`python hmac.py input_file key_file output_file`

The HMAC SHA256 implementation is seen in the hmac_sha256 function. There's also a helper functions in xor_bytes to xor, read and write functions to read and write.

---
## Problem 2

I have decided to expand the existing cbc.py implementation provided in the attachment files. I added the two functions `pad` and `unpad` to implement the padding scheme described in the task. It takes a sequence of bytes and adds padding, then the unpad function will remove the padding from the sequence of bytes. I then updated the main function to expect an additional parameter either penc or pdec. I integrated padding in the main function to pad the input data before encryption and to remove padding after decryption. You can verify it by comparing the pad_out file after encryption to the provided pad_out file.

To run it:

`python cbc.py penc plaintext_file key_file iv_file ciphertext_file` to encrypt..

and,

`python cbc.py pdec ciphertext_file key_file iv_file plaintext_file` to decrypt..

---
## Problem 3
I have attached three screenshots in the /p3/ folder showing the hierarchy in the chain of trust of uib.no and highlighted in the pictures which signature algorithm was used. I have also highlighted the RSA public key algorithm used and the keysize for each certificate.

A little explanation of what it is because I assume it is needed. The website certificate which the server issued certificate issued to the website uib.no is signed by the intermediate CA below it in the hierarchy. 

Next is the Sectigo RSA Org. CA which is the intermediate CA mentioned earlier. This is a security measure to reduce risk associated with a CA compromise. This certificate is signed by the root CA below it in the hierarchy. 

The root CA which is USERTrust RSA CA is the self-signed certificate trusted by the browser and operating system. This is the highest level of trust in the chain.

`w3.uib.no -> Sectigo RSA CA -> USERTrust Root CA`