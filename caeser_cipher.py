def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
          start = ord('A') if char.isupper() else ord('a')
          result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
  
message = "Hello World!"
shift_key = 3

encrypted = caesar_cipher(message, shift_key)
print(f"Encrypted: {encrypted}") # Khoor Zruog!

decrypted = caesar_cipher(encrypted, -shift_key)
print(f"Decrypted: {decrypted}") # Hello World!
