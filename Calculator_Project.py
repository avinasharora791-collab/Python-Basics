# Function > A block of code used to reuse the code. 

# Ex: See function as a "Saved Task.
# If I have a specific task you do often, like making a sandwich. 
# Instead of explaining every single step for ex:
# (get bread, add cheese, add meat).
# Every time someone asks for one, you just give that whole process a name: "MakeSandwich."

def calculate_add(a, b):
    print("Result", a + b)

def calculate_sub(a, b):
    print("Result", a - b)

def calculate_mul(a, b):
    print("Result", a * b)

def calculate_div(a, b):
    if b != 0:
        print("Result", a / b)

    else:
        print("Cannot divide by zero")

# Keeps program running continuously until stopped manually or with break.
while True:

# Try runs the code. If an error happens, except handles it instead of crashing the program. 
    try:

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Choose operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: 1/2/3/4: ")

# if is used to execute the code in condition for ex:
# if condition is true perform task A
# else perform task b. 

        if choice == "1":
            calculate_add(a, b)

        elif choice == "2":
            calculate_sub(a, b)

        elif choice == "3":
            calculate_mul(a, b)

        elif choice == "4":
            calculate_div(a, b)

        else:
            print("Invalid choice")

# If found error print the error so that the user understand ehat mistake they have done.
    except:
        print("Error: Enter valid numbers only")

# This code will help to  break the loop and closed the program.
    repeat = input("Do you wish to continue? (y, n): ")

    if repeat == "n":
        print("Calculator Closed")
        break