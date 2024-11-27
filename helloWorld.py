def input_not_null(prompt):
    '''Checks that user input is not NULL or is a number'''
    user_input = input(prompt)
    while user_input == "" or user_input.isdigit():
        print("Please input a word.")
        user_input = input(prompt)
    return user_input


# Prompt user for name and favourite colour, then print them.
user_name = input_not_null('\nWhat is your name: ')
user_colour = input_not_null('What is your favourite colour: ')
print(f'Good day {user_name}, your favourite colour is {user_colour}\n')
