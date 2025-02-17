segundos_totais = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos_totais // (24 * 3600)
horas = (segundos_totais % (24 * 3600)) // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")