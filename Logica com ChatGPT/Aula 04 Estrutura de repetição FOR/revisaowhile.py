import os
os.system('cls')

# soma = 0

# while True:
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite o outro numero: '))

#     soma = num1 + num2
#     print(f'A soma entre {num1} + {num2} é igual a {soma}')

#     continuar = input('Deseja continuar ?')
#     if continuar == 'Não':
#         break

# soma = 0

# while True:
#     num1 = int(input('Digite um número: '))

#     soma += num1 
#     print(f'A soma total até o momento é {soma}')

#     continuar = input('Deseja continuar ?')
#     if continuar == 'Não':
#         break

# ATIVIDADE 2

numero = 0

while numero < 51:
    if numero %2 != 0:
        print(numero)
    numero += 10