def calculator(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '//':
            return a // b
        case '%':
            return a % b
        case _:
            return "Nepoznat operator."

a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /, //, %): ")
rezultat = calculator(a, b, operator)
print("Rezultat je:", rezultat)