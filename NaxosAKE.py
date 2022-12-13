import hashlib, binascii, os, sympy


#Formation of a cyclic group
# p and q
flag = True
while flag == True:
    q = sympy.randprime(100000,200000)  #random large prime q
    p = 2*q + 1
    for i in range(2, p):     #checking if p is prime number
        if(p % i == 0):
            flag = True
        else:
            flag = False

# initialization g as g^q mod p = 1, 1 < g < p-1
g = 2

# creating a group G with q-elements g^i mod p
G = []
for i in range(1, q):
    G.append(pow(g, i, p))


#Generating secretKeyA and secretKeyB belonging to Zq

secretKeyA = 29722055333381 % q
secretKeyB = 75981582189181 % q

#Generating publicKeyA and publicKeyB publicKeyX=g^(secretKeyX) belonging to group G

publicKeyA = pow(g, secretKeyA, p)
publicKeyB = pow(g, secretKeyB, p)

#Generating ephemeralSecretKeyA and ephemeralSecretKeyB as hashed bytes string

ephemeralSecretKeyA = hashlib.sha512(os.urandom(10)).digest()
ephemeralSecretKeyB = hashlib.sha512(os.urandom(10)).digest()

# Create H1 with output belonging to Zq
def H1(esk, sk):
    temp = str(esk)+str(sk)

    H1 = hashlib.sha512(temp.encode()).digest()
    return (int(binascii.hexlify(H1), 16) % q)


# Initiating values X and Y belonging to group G
X = pow(g, H1(ephemeralSecretKeyA, secretKeyA), p)
Y = pow(g, H1(ephemeralSecretKeyB, secretKeyB), p)

# A should send X to B and B should send Y to A
if(X in G and Y in G):
    print("X and Y both are in group G")
else:
    print("Error")

# Create id_A id_B

A = "Side A"
B = "Side B"

# Session Key A

hash_mod_A = H1(ephemeralSecretKeyA,secretKeyA) % p
temp_session_key_A = str(pow(Y, secretKeyA, p)) + str(pow(publicKeyB, hash_mod_A, p)) + str(pow(Y, hash_mod_A, p)) + A + B
h2_A = hashlib.new('sha512')
h2_A.update(temp_session_key_A.encode())
session_key_A = h2_A.digest()

# Session Key B

hash_mod_B = H1(ephemeralSecretKeyB, secretKeyB) % p
temp_session_key_B = str(pow(publicKeyA, hash_mod_B, p)) + str(pow(X, secretKeyB, p)) + str(pow(X, hash_mod_B, p)) + A + B
h2_B = hashlib.new('sha512')
h2_B.update(temp_session_key_B.encode())
session_key_B = h2_B.digest()


# Results
print("Public Key A = ", publicKeyA)
print("Public Key B = ", publicKeyB)
print("Secret Key A = ", secretKeyA)
print("Secret Key B = ", secretKeyB)
print("Session Key A = ", session_key_A)
print("Session Key B = ", session_key_B)

# Checking if the keys are the same
if(session_key_A == session_key_B):
    print("Session Keys are the same!")
else:
    print("Session keys are different - error")

