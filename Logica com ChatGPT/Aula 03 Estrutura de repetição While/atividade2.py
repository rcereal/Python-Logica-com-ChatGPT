import os
os.system('cls')

# num_misterioso = 87
# limite_tentativas = 6
# tentativa = 0

# while tentativa != num_misterioso and limite_tentativas > 0:
#     tentativa = int(input('Adivinhe o numero entre 1 e 100: '))
#     limite_tentativas -= 1

#     if tentativa < 20:
#         print(f'Você esta muito frio, te restam {limite_tentativas} tentativas: ')
#     elif tentativa < 50:
#         print(f'Você esta ainda esta frio, te restam {limite_tentativas} tentativas: ')
#     elif tentativa < 70:
#         print(f'Ta começando a esquentar, te restam {limite_tentativas} tentativas: ')
#     elif tentativa < 87 or tentativa > 87:
#         print(f'Ta esquentando muito, te restam {limite_tentativas} tentativas: ')
    
# if tentativa == num_misterioso: 
#     print(f'Muito bem, você acertou!!! O numero misterioso é {num_misterioso}')
# else:
#     print(f'Você excedeu o limite de tentativas. O número secreto era {num_misterioso}')


# ATIVIDADES NUMEROS INTEIROS

num_inteiros = 0
soma_pares = 0

while True:
    num_inteiros = int(input('Digite um numero inteiro: '))

    if num_inteiros % 2 == 0:
        soma_pares += num_inteiros
    
    if soma_pares >= 50:
        print(f'A soma dos numeros pares está acima ou igual a 50 e o total é {soma_pares} ') 
        break
    
