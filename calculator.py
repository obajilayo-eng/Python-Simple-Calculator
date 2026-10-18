def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        # Get user input
        user_input = input("Enter calculation (e.g., 5 + 3): ").strip()

        # Exit condition
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            # Split input into parts: number, operator, number
            parts = user_input.split()

            if len(parts) != 3:
                print("Error: Please use format 'number operator number' (e.g., 5 + 3)\n")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            # Perform calculation
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero\n")
                    continue
                result = num1 / num2
            else:
                print(f"Error: Unknown operator '{operator}'. Use +, -, *, or /\n")
                continue

            # Display result (remove .0 for whole numbers)
            if result == int(result):
                print(f"Result: {int(result)}\n")
            else:
                print(f"Result: {result}\n")

        except ValueError:
            print("Error: Invalid numbers. Please try again.\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    calculator()