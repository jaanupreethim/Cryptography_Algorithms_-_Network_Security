text = input("Enter text: ")

# Convert each character to its 8-bit binary equivalent
binary_output = ' '.join(format(ord(char), '08b') for char in text)

print(f"Binary: {binary_output}")
