import calculator

def main():

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    try:
        if operation == "add":
            result = calculator.add(a, b)
        elif operation == "subtract":
            result = calculator.subtract(a, b)
        elif operation == "multiply":
            result = calculator.multiply(a, b)
        elif operation == "divide":
            result = calculator.divide(a, b)
        else:
            result = "Unknown operation"
    except Exception as e:
        result = f"Error: {e}"

    print("Result:", result)

if __name__ == "__main__":
    main()