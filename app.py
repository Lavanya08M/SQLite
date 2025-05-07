# import the database module to handle data storage and retrieval
import database

# Menu prompt for user interaction
MENU_PROMPT = """ -- Coffee Bean App --

Choose an option:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your Choice:"""

# Main menu loop
def menu():
    connection = database.connect() # Connect to the SQLite database
    database.create_tables(connection) # Ensure the beans table exists

    # Keep prompting the user until the user choose to exit
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
           prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        else:
            print("Invalid input, please try again!")


# Add a new bean entry from user input
def prompt_add_new_bean(connection):
    name = input("Enter bean name: ").strip().title()
    method = input("Enter how you've prepared it: ").strip().title()
    while True:
        try:
            rating = int(input("Enter your rating score (0-100): "))
            if 0 <= rating <= 100:
                break
            else:
                print("Rating must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer")

    database.add_bean(connection, name, method, rating)

# Display all bean entries
def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} {bean[2]} - {bean[3]/100:.2f}")

# Search and display all records of a specific bean name
def prompt_find_bean(connection):
    name = input("Enter bean name to find: ").strip().title()
    beans = database.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} {bean[2]} - {bean[3]/100:.2f}")

# Show the highest rated preparation method for a given bean
def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = database.get_best_preparation_for_bean(connection, name)

    print(f"The best preparation method for {name} is: {best_method[2]}")


# start the app
menu()