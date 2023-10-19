with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

letter_counts = {}

for word in words:
    for letter in word:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_counts:
                # update
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")

letter_list = list(letter_counts.items())
letter_list.sort()

for pair in letter_list:
    print(f"The '{pair[0]}' was found {pair[1]} times")
print(f"--- End report ---")