# Função para calcular a soma dos dígitos
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10  # Adiciona o último dígito do número
        numero //= 10  # Remove o último dígito
    return soma

# Leitura do número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula a soma dos dígitos
resultado = soma_digitos(numero)

# Imprime o resultado
print(resultado)
