# Initialize a list of words
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

# Use list comprehension to create a new list that contains only the words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list to the console
print("Words with an odd number of characters:")
print(odd_length_words)