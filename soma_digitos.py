
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10  
        numero //= 10  
    return soma


numero = int(input("Digite um número inteiro: "))


resultado = soma_digitos(numero)


print(resultado)
