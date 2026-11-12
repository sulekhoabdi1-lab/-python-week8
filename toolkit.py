
import random

# Tool 1: A calculator that performs four basic operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        elif operation == "4":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from 1 to 4.")
            return

        print(f"The answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: A to-do list that lets users add, view and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added!")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' has been removed!")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose from 1 to 4.")


# Tool 3: A number guessing game where players guess a secret number.
def guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please choose a number between 1 and 20.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a whole number.")


# Main menu: Keeps the toolkit running until the user chooses Quit.
def main():
    print("===================================")
    print("Welcome to My Personal Mini-Toolkit!")
    print("===================================")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using my Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


# Start the program.
if __name__ == "__main__":
    main()
