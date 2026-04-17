str1 = input("Enter first word: ").lower()
str2 = input("Enter second word: ").lower()

is_anagram = sorted(str1.replace(" ", "")) == sorted(str2.replace(" ", ""))

print(f"Result: {'They are anagrams!' if is_anagram else 'Not anagrams.'}")
