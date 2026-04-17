def find_primitive_root(p):
    if p == 2: return 1
    phi = p - 1
    
    # Find unique prime factors of p - 1
    factors = []
    d, temp = 2, phi
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0: temp //= d
        d += 1
    if temp > 1: factors.append(temp)

    # Test each number from 2 upwards
    for res in range(2, p):
        if all(pow(res, phi // f, p) != 1 for f in factors):
            return res
    return None

# --- Dynamic Input Section ---
try:
    num = int(input("Enter a prime number: "))
    root = find_primitive_root(num)
    
    if root:
        print(f"The smallest primitive root of {num} is: {root}")
    else:
        print(f"No primitive root found for {num}.")
except ValueError:
    print("Please enter a valid integer.")
