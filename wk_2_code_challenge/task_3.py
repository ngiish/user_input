user_input = {}

while True:
    user_input["name"] = input ("Enter your name:")
    user_input["age"] = input ("Enter your age:")
    user_input["favourite_colour"] = input ("Enter your favourite colour:")
    quit_input = input ("Enter q to quit:")

    if quit_input.lower() == "q":
        break



print(f"Hello {user_input['name']}. You are {user_input['age']} and your favourite colour is {user_input['favourite_colour']}")