import string
import secrets


print("Escolha o tipo de senha: ")

print("1 - Só números")
print("2 - Só letras")
print("3 - Misturado")

tamanho_senha = 8

caracteres1 = string.ascii_letters

senha1 = "".join(secrets.choice(caracteres1)) for _ in range(tamanho_senha)

tipo = int(input("Escolha: "))

if tipo == 1:
    print(f"{senha1}")

