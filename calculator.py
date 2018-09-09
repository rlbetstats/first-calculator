# first calculator program


while True:
    print("Options: ")
    print("Enter 'add' to add two numbers together")
    print("Enter 'subtract' to take two numbers away from each other")
    print("Enter 'multiply' to multiply two numbers together")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to exit the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        print("To be written (add)")
    elif user_input == "subtract":
        print("To be written (subtract)")
    elif user_input == "multiply":
        print("To be written (multiply)")
    elif user_input == "divide":
        print("To be written (divide)")
    else:
        print("Unknown Input")
