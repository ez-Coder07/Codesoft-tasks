try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    print("""Select operator:
1) +    2) -    3) *    4) /""")

    operator = int(input("Select operator: "))

    actions = {
        1: lambda x, y: print(x + y),
        2: lambda x, y: print(x - y),
        3: lambda x, y: print(x * y),
        4: lambda x, y: print(x / y),
    }

    invalid = lambda x, y: print("Invalid operation")

    actions.get(operator, invalid)(a, b)

except ValueError:
    print("Enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")