def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    elif operator == '%':
        return a % b
    else:
        return "Nepoznat operator."

a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /, //, %): ")
rezultat = calculator(a, b, operator)
print("Rezultat je:", rezultat)
# Ako želimo zaokružiti na dvije decimale pišemo print("Rezultat je:", round(rezultat, 2))
