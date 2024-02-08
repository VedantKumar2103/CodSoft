# Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

operations = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide)
}

print("Select operation:")
for key, value in operations.items():
    print(key + ". " + value[0])

choice = input("Enter choice (1/2/3/4): ")

if choice in operations:
    operation_name, operation_func = operations[choice]
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = operation_func(num1, num2)
    print(f"{operation_name} result: {result}")
else:
    print("Invalid input")
