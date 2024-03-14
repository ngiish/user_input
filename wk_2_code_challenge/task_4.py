# Initialize two empty sets to store integers
set1 = set()
set2 = set()

# In a loop, ask the user for input and convert the input to an integer, then add it to the first set
print("Enter integers for the first set (type 'done' when finished):")
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    try:
        integer = int(user_input)
        set1.add(integer)
    except ValueError:
        print(f"'{user_input}' is not a valid integer. Please try again.")

# In a loop, ask the user for input and convert the input to an integer, then add it to the second set
print("Enter integers for the second set (type 'done' when finished):")
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    try:
        integer = int(user_input)
        set2.add(integer)
    except ValueError:
        print(f"'{user_input}' is not a valid integer. Please try again.")

# Create a new set that contains only the elements that are common to both sets
common_set = set1.intersection(set2)

# Print the common set to the console
print("The common set is:")
for element in common_set:
    print(element)