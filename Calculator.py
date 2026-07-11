print("This is simple calculator!!!")
print("Choose option among(1-4)")
print("1-Addition(+)\n2-Subtraction(-)\n3-Multiplication(*)\n4-Division(/)")
try:

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            while True:
                try:

                    num1 = float(input("Enter first number: "))
                    break
                except ValueError:
                    print("Error!!! You need to enter a valid number")
            while True:
                try:     
                    num2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Error!!! You need to enter a valid number i.e. 3,4,5 etc")
        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            while num2==0:
                    try:
                        print("Kindly enter non-zero no.i.e. 3,4,5 etc")
                        num2=float(input("Enter 2nd no. again:"))
                    except ValueError:
                        print("Error!!! You need to enter a valid number i.e. 3,4,5 etc")
            print(f"{num1} / {num2} = {num1 / num2}")
        elif choice not in ['1','2','3','4']:
            print("Kindly enter number among(1-4)")
            continue
        again=input("Do you want to quit:\n1-Yes\n2-No")
        if again.lower().startswith("y") or again == "1":
                break
        else:
            continue
except KeyboardInterrupt:
    print("Exiting!!!!")

       
        
        