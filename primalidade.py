entrada = int(input("Digite um numero inteiro: "))
contador = 2 
while contador < entrada: 
    if contador < 2: 
        continue
    if entrada % contador == 0: 
        print("Não Primo")
        break
    contador += 1
if contador == entrada: 
    print("Primo")
