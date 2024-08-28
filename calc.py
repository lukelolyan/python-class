def simple_calculator():
    while True:
        user_input = input("Enter a simple expression (e.g., 3+4 or 7-2) or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            if '+' in user_input:
                num1, num2 = user_input.split('+')
                operator = '+'
            elif '-' in user_input:
                num1, num2 = user_input.split('-')
                operator = '-'
            else:
                raise ValueError("Invalid input. Only '+' and '-' operators are supported.")

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

simple_calculator()
