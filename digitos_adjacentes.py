numero = input("Digite um número inteiro: ")

i = 0
encontrou_digito_igual = False

while i < len(numero) - 1:
    if numero[i] == numero[i + 1]:
        encontrou_digito_igual = True
    i += 1

if encontrou_digito_igual:
    print("sim")
else:
    print("não")

