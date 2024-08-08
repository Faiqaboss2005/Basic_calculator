from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /): ")

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator!")
                continue

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        choice = input("Do you want to quit the calculator? (Y/N): ").strip().lower()
        if choice == 'y':
            break

if __name__ == "__main__":
    main()
