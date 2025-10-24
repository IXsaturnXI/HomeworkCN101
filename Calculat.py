print("1. Modify Calculator")
Continue = "c" or "C"
while Continue == "c" or Continue == "C":
    Digit_value_1 = float(input("Digit value 1 : "))
    Digit_value_2 = float(input("Digit value 2 : "))
    Operation = input("Enter operation (+, -, *, /, //, %, **): ")
    if Operation == "+":
        Result = Digit_value_1 + Digit_value_2
        print(f"{Digit_value_1} + {Digit_value_2} = {Result:,.2f}")
    elif Operation == "-":
        Result = Digit_value_1 - Digit_value_2
        print(f"{Digit_value_1} - {Digit_value_2} = {Result:,.2f}")
    elif Operation == "*":
        Result = Digit_value_1 * Digit_value_2
        print(f"{Digit_value_1} * {Digit_value_2} = {Result:,.2f}")
    elif Operation == "/":
        if Digit_value_2 != 0:
            Result = Digit_value_1 / Digit_value_2
            print(f"{Digit_value_1} / {Digit_value_2} = {Result:,.2f}")
        else:
            print("Error: Division by zero is not allowed.")
    elif Operation == "//":
        if Digit_value_2 != 0:
            Result = Digit_value_1 // Digit_value_2
            print(f"{Digit_value_1} // {Digit_value_2} = {Result:,.2f}")
        else:
            print("Error: Division by zero is not allowed.")
    elif Operation == "%":
        if Digit_value_2 != 0:
            Result = Digit_value_1 % Digit_value_2
            print(f"{Digit_value_1} % {Digit_value_2} = {Result:,.2f}")
        else:
            print("Error: Division by zero is not allowed.")
    elif Operation == "**":
        Result = Digit_value_1 ** Digit_value_2
        print(f"{Digit_value_1} ** {Digit_value_2} = {Result:,.2f}")
    else:
        print("Error: Invalid operation.")
    Continue = input("Do you want to continue another calculation? (c to continue, any key to exit): ")