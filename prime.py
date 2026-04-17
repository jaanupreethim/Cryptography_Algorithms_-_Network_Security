num = int(input("Enter a number: "))

if num > 1:
    # Check for factors from 2 up to the square root of num
    is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
else:
    is_prime = False

print(f"{num} is {'a Prime' if is_prime else 'not a Prime'} number.")
