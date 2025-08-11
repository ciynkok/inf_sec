# RSA Scheme and Two RSA Hacking Methods Written in Python

## A project written in Python that implements the RSA scheme and two ways to crack RSA. The first method factors the public key. And the second method raises the encrypted message to a power modulo.

The project includes:
* An algorithm for generating public and secret keys
* The Miller-Rabin test for checking whether a number is prime
* Fast exponentiation algorithm
* Extended Euclidean Algorithm
* RSA encryption and decryption algorithm
All of the above modules taken together represent the RSA scheme.

The project also presents two types of RSA hacks:
* The first way is to factorize the number n, which is part of the public and secret key. By finding the factors and using the key generation algorithm, you can calculate the secret key
* The second method is less reliable, but depending on the generated keys it may be more effective than the first method. It outputs an encrypted message at the same degree of the public key modulo, that is, it repeats the message encryption algorithm, then outputs the result again at the same level, and so on, until the result is the original encrypted message. The decrypted message will be the result algorithm obtained in the previous iterations.

Graph of the dependence of time and number of iterations of the first and second hacking methods depending on the key length:
<img width="4200" height="3600" alt="graph" src="https://github.com/user-attachments/assets/1f40a44a-930c-4d3c-8251-b607b47f43a4" />

# How to install this Python Project
1. clone this repository
2. make sure you have Python 3.10 or higher
3. go to the project repository on your device, open a terminal and enter the command 'pip install -r requirements.txt' to install the required libraries
4. run the rsa.py file to see the RSA scheme in action
5. run the file one_crack_rsa.py to see how the first method of cracking RSA works
6. run the file two_crack_rsa.py to see how the second method of cracking RSA works
7. run the graph.py file to see the difference in time and number of iterations between the two RSA cracking methods on a graph

