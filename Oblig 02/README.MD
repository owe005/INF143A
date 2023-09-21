# INF143A Mandatory Assignment 02
##### Ole Kristian Westby // owe009@uib.no

---

## Task 1: Expand the functionality of cipher.py making it possible to handle arbitrary size inputs using CBC mode of operation.

In /INF143A-Oblig02/p1> you'll find cipher.py and the two files enc.py and dec.py, as well as 4 additional sample files: "moo_in", "moo_iv", "moo_key", "moo_out". In order to encrypt the moo_in file using enc.py you would run the command: 

`python enc.py moo_in moo_key moo_iv moo_out`

which will save the ciphertext in *moo_out*, you can verify that this is done correctly by checking the sample files given with the assignment. In order to decrypt, you'll run the command:

`python dec.py moo_out moo_key moo_iv moo_in`

and it will decrypt the ciphertext and save the plaintext in *moo_in*

---

## Task 2: Implement the Elgamal digital signature scheme in Python.

In /INF143A-Oblig02/p2> you'll find the elgamal.py file with the elgamal scheme implemented. To run it, use:

`python elgamal.py parameters private_key message output`

It'll then save the signature (r,s) in the output file with r on first- and s on the second line. I implemented a function to verify the signature and if it is correct.

---

## Task 3: Implement a program to compute the differential uniformity of a given (n,n)-function.

In /INF143A-Oblig02/p3> you'll find the Python script `du.py` which takes a lookup_table and returns the differential uniformity. Running the command: 

`python du.py sample1.tt` 

will print the differential uniformity "2". while if you run it on sample2.tt, it'll print "8", respectively.

