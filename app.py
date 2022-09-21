def is_number(text):
    return text.replace(".", "").isdigit()


def get_number(text):
    while True:
        num = input("Zadejte " + text + " cislo: ").replace(",", ".")
        if is_number(num):
            return float(num)
        else:
            print("Zadejte prosim cislo")


def calculate(num1, num2, opr):
    match(opr):
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2


def main():
    
    result = None
    can_continue = "n"

    while True:

        if can_continue == "n":
            num1 = get_number("prvni")
        else:
            num1 = result

        num2 = get_number("druhe")

        while True:
            opr = input("Zadejte operaci + - * /: ")
            if opr in "+-*/":
                break
            else:
                print("Zadejte prosim operaci z: + - * /")

        result = calculate(num1, num2, opr)

        print(num1, opr, num2, " = ", result)

        can_continue = input("Chcete pokračovat ve výpočtu Y/N (Y): ").lower()
        
        if can_continue != "n":
            continue

        can_close = input("Chcete ukončit aplikaci Y/N (N): ")

        if can_close.lower() == "y":
            break

if __name__ == "__main__":
    main()