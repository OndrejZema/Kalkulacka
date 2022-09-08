
while True:

    num1 = int(input("Zadejte prvni cislo: "))
    num2 = int(input("Zadejte druhe cislo: "))
    opr = input("Zadejte operaci + - * /: ")

    if opr == "+":
        print(num1+num2)
    elif opr == "-":
        print(num1-num2)
    elif opr == "*":
        print(num1*num2)
    elif opr == "/":
        print(num1/num2)
    can_close = input("Chcete dále pokačovat Y/N: ")

    if can_close.lower() == "n":
        break