
while True:

    while True:
        num1 = input("Zadejte prvni cislo: ")
        if num1.isdigit():
            num1 = int(num1)
            break
        else:
            print("Zadejte prosim cislo")

    while True:
        num2 = input("Zadejte druhe cislo: ")
        if num2.isdigit():
            num2 = int(num2)
            break
        else:
            print("Zadejte prosim cislo")

    while True:
        opr = input("Zadejte operaci + - * /: ")
        if opr in "+-*/":
            break
        else:
            print("Zadejte prosim operaci z: + - * /")

    if opr == "+":
        print(num1+num2)
    elif opr == "-":
        print(num1-num2)
    elif opr == "*":
        print(num1*num2)
    elif opr == "/":
        print(num1/num2)

    can_close = input("Chcete ukončit Y/N (N): ")

    if can_close.lower() == "y":
        break