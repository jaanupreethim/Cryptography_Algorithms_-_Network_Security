def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        if m == 0: return None # Avoid division by zero
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

try:
    num = int(input("Enter number (a): "))
    mod = int(input("Enter modulus (m): "))

    inverse = mod_inverse(num, mod)
    if inverse and (num * inverse) % mod == 1:
        print(f"The multiplicative inverse is: {inverse}")
    else:
        print("Inverse does not exist (numbers must be coprime).")
except ValueError:
    print("Please enter valid integers.")
