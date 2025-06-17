print("Enter 'exit' to stop.")
result = ()

while True:
    # Ввод первого числа
    first_number = input("Enter first number: ")
    if first_number == "exit":
        break

    try:
        first_number = float(first_number)
    except ValueError:
        print("That's not a valid number!")
        print("---")
        continue

    # Ввод операции с защитой
    valid_operations = ["+", "-", "*", "/"]
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "exit":
        break
    if operation not in valid_operations:
        print("Invalid operation! Please enter one of +, -, *, /")
        print("---")
        continue

    # Ввод второго числа
    second_number = input("Enter second number: ")
    if second_number == "exit":
        break

    try:
        second_number = float(second_number)
    except ValueError:
        print("That's not a valid number!")
        print("---")
        continue

    # Выполнение операции
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You can't divide by zero!")
            print("---")
            continue
        else:
            result = first_number / second_number

    print(f"Result: {result}")
    print("---")
