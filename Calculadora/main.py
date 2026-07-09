print("---Calculadora---")

print("Qual a operação?")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - DIVISÃO")
print("4 - MULTIPLICAÇÃO")

operacao = int(input("Digite: "))

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if operacao == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operacao == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operacao == 3:
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")

elif operacao == 4:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
    