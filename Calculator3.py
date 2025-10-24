#6810742681 เศรษฐการ มณีสวัสดิ์
Ans_Undo = "u" or "U"
Continue = "c" or "C"

while Continue == "c" or Continue == "C":
    Digit_value_1 = float(input("Digit value 1 : "))
    Operation = input("Enter operation (+, -, *, /, //, %, **): ")
    Digit_value_2 = float(input("Digit value 2 : "))
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
    
    list = [Digit_value_1,Operation,Digit_value_2,Result]
    Ans_Undo = input("Do you want to undo last calculation? (u to undo, any key to skip): ")
    while Ans_Undo == "u" or Ans_Undo == "U":
        Ans_change = (input("Which value/operation do you want to change?(1.Digitvalue 1,2.Operation,3.Digit value 2 ,) : "))
        
        if Ans_change == "1":
            Digit_value_1 = float(input("Digit value 1 : "))
            list[0] = Digit_value_1
            if list[1] == "+":
                list[3] = list[0] + list[2]
            elif list[1] == "-":
                list[3] = list[0] - list[2]
            elif list[1] == "*":
                list[3] = list[0] * list[2]
            elif list[1] == "/":
                if list[2] != 0:
                    list[3] = list[0] / list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "//":
                if list[2] != 0:
                    list[3] = list[0] // list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "%":
                if list[2] != 0:
                    list[3] = list[0] % list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "**":
                list[3] = list[0] ** list[2]
            else:
                print("Error: Invalid operation.")
        
        elif Ans_change == "2":
            Operation = input("Enter operation (+, -, *, /, //, %, **): ")
            list[1] = Operation 
            if list[1] == "+":
                list[3] = list[0] + list[2]
            elif list[1] == "-":
                list[3] = list[0] - list[2]
            elif list[1] == "*":
                list[3] = list[0] * list[2]
            elif list[1] == "/":
                if list[2] != 0:
                    list[3] = list[0] / list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "//":
                if list[2] != 0:
                    list[3] = list[0] // list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "%":
                if list[2] != 0:
                    list[3] = list[0] % list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "**":
                list[3] = list[0] ** list[2]
            else:
                print("Error: Invalid operation.") 
        
        elif Ans_change == "3":
            Digit_value_2 = float(input("Digit value 2 : "))
            list[2] = Digit_value_2
            if list[1] == "+":
                list[3] = list[0] + list[2]
            elif list[1] == "-":
                list[3] = list[0] - list[2]
            elif list[1] == "*":
                list[3] = list[0] * list[2]
            elif list[1] == "/":
                if list[2] != 0:
                    list[3] = list[0] / list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "//":
                if list[2] != 0:
                    list[3] = list[0] // list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "%":
                if list[2] != 0:
                    list[3] = list[0] % list[2]
                else:
                    print("Error: Division by zero is not allowed.")
            elif list[1] == "**":
                list[3] = list[0] ** list[2]
            else:
                print("Error: Invalid operation.")
        else:
            print("Error: Invalid choice.")
       
        print(f"Updated values: {list[0]} {list[1]} {list[2]} = {list[3]:,.2f}")
        Ans_Undo = input("Do you want to undo last calculation? (u to undo, any key to skip): ")    
        
    Continue = input("Do you want to continue another calculation? (c to continue, any key to exit): ")