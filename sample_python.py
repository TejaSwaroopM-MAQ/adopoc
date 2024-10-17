def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == "power":
        return a**b
    else:
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(calculator('add', 5, 3))        # Output: 8
    print(calculator('subtract', 5, 3))   # Output: 2
    print(calculator('multiply', 5, 3))   # Output: 15
    print(calculator('divide', 5, 3))     # Output: 1.666...
    print(calculator('divide', 5, 0))     # Output: Error: Division by zero
    print(calculator('modulus', 5, 3))    # Output: Error: Unsupported operation
