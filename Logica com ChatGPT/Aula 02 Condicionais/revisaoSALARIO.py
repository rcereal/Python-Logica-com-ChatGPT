import os
os.system('cls')

salariohora = float(input('Quanto você recebe por horas trabalhadas ? '))
horastrabalhadas = int(input('Quantas horas você trabalha por mês ? '))
salariobruto = float(salariohora * horastrabalhadas)

print(f'Seu salario bruto é de {salariobruto}')

imposto_renda = salariobruto * 0.11 # PORCENTAGEM DE 11% FICARIA 0.11 SEGUIR ESSA LINHA DE RACIOCINIO
inss = salariobruto * 0.08 # PORCENTAGEM DE 8% FICARIA 0.08 SEGUIR ESSA LINHA DE RACIOCINIO
sindicato = salariobruto * 0.05 # PORCENTAGEM DE 5% FICARIA 0.05 SEGUIR ESSA LINHA DE RACIOCINIO

print(f'IR (11%) R$ {imposto_renda}')
print(f'INSS (8%) R$ {inss}')
print(f'Sindicato (5%) R$ {sindicato}')

print(f'Seu salario liquido fica no valor de R${salariobruto-(imposto_renda+inss+sindicato)}')