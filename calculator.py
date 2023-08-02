def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero is not allowed"
    return x / y

print("Choose operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Divisiom")

choice = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Wrong operation choice")
