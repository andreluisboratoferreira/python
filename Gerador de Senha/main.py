import random
import secrets


print("Escolha o tipo de senha: ")

print("1 - Só números")
print("2 - Só letras")
print("3 - Misturado")

senha1 = secrets.choice

tipo = int(input("Escolha: "))

if tipo == 1:
    print(f"{senha1}")

