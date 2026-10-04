import hashlib

# DSA parameters
p = 23
q = 11
g = 4

# Private key
x = 3

# Public key
y = pow(g, x, p)

# Secret number
k = 7

# Read message
message = input("Enter message: ")

# Hash message
h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q

# Signature generation
r = pow(g, k, p) % q
k_inv = pow(k, -1, q)
s = (k_inv * (h + x * r)) % q

print("\n--- DSA Signature ---")
print("Hash =", h)
print("Private Key =", x)
print("Public Key =", y)
print("r =", r)
print("s =", s)

# Signature verification
w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q

v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

print("\n--- Verification ---")
print("u1 =", u1)
print("u2 =", u2)
print("v =", v)

if v == r:
    print("Signature is VALID")
else:
    print("Signature is INVALID")
