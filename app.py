def is_number(text: str) -> bool:
    return text.replace(".", "").isdigit()


def get_number(text: str) -> float:
    while True:
        num = input("Zadejte " + text + " cislo: ").replace(",", ".")
        if is_number(num):
            return float(num)
        else:
            print("Zadejte prosim cislo")


def calculate(num1: float, num2: float, opr: str)-> tuple[int, float]:
    result: float = None
    match(opr):
        case "+":
            result = num1+num2
        case "-":
            result = num1-num2
        case "*":
            result = num1*num2
        case "/":
            if num2 == 0:
                return tuple([-1, None])
            result = num1/num2
    return tuple([0, result])


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
        if result[0] != 0:
            print("Nastala chyba")
            can_continue = "n"
            continue
        print(type(result))
        print(num1, opr, num2, " = ", result[1])

        can_continue = input("Chcete pokračovat ve výpočtu Y/N (Y): ").lower()
        
        if can_continue != "n":
            continue

        can_close = input("Chcete ukončit aplikaci Y/N (N): ")

        if can_close.lower() == "y":
            break

if __name__ == "__main__":
    main()