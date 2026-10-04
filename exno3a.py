def find_gcd(a, b):
    print("\nSteps of Euclidean Algorithm:")
    while b != 0:
        quotient = a // b
        remainder = a % b
        print(f"{a} ÷ {b} = Quotient {quotient}, Remainder {remainder}")
        a, b = b, remainder
    return a

# Main Program
print("=== Secure Communication Key Validation ===")

# Read encryption parameters
parameter1 = int(input("Enter the first encryption parameter: "))
parameter2 = int(input("Enter the second encryption parameter: "))

# Find GCD
gcd = find_gcd(parameter1, parameter2)

# Display GCD
print("\nGreatest Common Divisor (GCD) =", gcd)

# Validate communication parameters
if gcd == 1:
    print("\n[OK] The encryption parameters are COPRIME.")
    print("[OK] Secure communication can be established.")
else:
    print("\n[NOT OK] The encryption parameters are NOT COPRIME.")
    print("[NOT OK] Communication setup rejected.")
    print("[NOT OK] Choose different encryption parameters.")

