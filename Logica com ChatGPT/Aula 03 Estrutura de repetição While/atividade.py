import os
os.system('cls')

# num_pares = 2

# while num_pares < 11:
#     print(num_pares)

#     num_pares += 2

num_misterioso = 15

tentativa = 0

while tentativa != num_misterioso:
    tentativa = int(input('Adivinhe o numero entre 1 e 20: '))
    if tentativa < 14:
        print('Você esta longe, tente novamente: ')
    elif tentativa == 14:
        print('Você esta por um triz, tente novamente: ')
    elif tentativa == 16:
        print('Você passou :(, mas esta muito perto, tente novamente: ')
    elif tentativa > 16:
        print('Você esta longe, tente novamente: ')
    
print(f'Muito bem, você acertou!!! O numero misterioso é {num_misterioso}')
    
    