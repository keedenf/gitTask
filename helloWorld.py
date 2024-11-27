def input_not_null(prompt):
    '''Checks that user input is not NULL'''
    user_input = input(prompt)
    while user_input == "":
        print("Please input a word.")
        user_input = input(prompt)
        return user_input
    return user_input


user_name = input_not_null('\nWhat is your name: ')
user_colour = input_not_null('What is your favourite colour: ')
print(f'Good day {user_name}, your favourite colour is {user_colour}\n')
