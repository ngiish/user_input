# print ("Hello there, traveller.")
# def sum_integers(list):
#     list = []
#     return
# Initialize an empty list to store the integers
numbers = []

# In a loop, ask the user for input and convert the input to an integer
while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input.lower() == 'q':
        break
    
    try:
        integer = int(user_input)
        numbers.append(integer)
    except ValueError:
        print(f"'{user_input}' is not a valid integer. Please try again.")

# Compute the sum of all the integers in the list
total = sum(numbers)

print(f"The sum of all integers is: {total}")