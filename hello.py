#1.Add
#2.subtract
#3.multiply
#4.divide
print("Select operation to perform:")
print("1. Add")
print("2.  subtract")
print("3. Mulbtiply")
print("4. divide")
print("5. Exit")

operation = input()

if operation in ['1', '2', '3', '4']:
    num1 =float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif operation == '2':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operation == '3':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif operation == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero.")  



            course='python for beginners'
            print(course[5:0])