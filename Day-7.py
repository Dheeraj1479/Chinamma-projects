#Count the vowels in a given string using a for loop

vowel_count = 0
print("Enter a word to count how many vowels it contains")
word = str(input())

vowels = ['a', 'e', 'i', 'o', 'u']
for letter in word:
    if letter in vowels:
        print(letter)
        vowel_count += 1

print(f"There are {vowel_count} vowels")
