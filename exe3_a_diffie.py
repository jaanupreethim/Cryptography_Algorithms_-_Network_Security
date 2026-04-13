def run_diffie_hellman():
    print("--- Diffie-Hellman Key Exchange ---")
    p = int(input("Enter Prime (p): "))
    g = int(input("Enter Primitive Root (g): "))
    a = int(input("Alice's Private Key: "))
    b = int(input("Bob's Private Key: "))

    # Generate Public Keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Compute Shared Secrets
    alice_shared = pow(B, a, p)
    bob_shared = pow(A, b, p)

    print(f"\nAlice's Public Key: {A}")
    print(f"Bob's Public Key: {B}")
    print(f"Resulting Shared Secret: {alice_shared}")

run_diffie_hellman()
