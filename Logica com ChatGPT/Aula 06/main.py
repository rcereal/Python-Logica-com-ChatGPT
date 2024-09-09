# def registrar_venda():
#     nome_comprador = input("Digite o nome do comprador: ")
#     preco_produto = float(input("Digite o preço do produto: "))
#     return nome_comprador, preco_produto

# vendas = []

# while True:



#     continuar = input('Deseja continuar ?')
#     if continuar == 'N':
#          break


while True:
    nome_comprador = input('Digite seu nome: ')
    preço_produto = float(input('Digite o preço do produto: '))
        
    continuar = input('Deseja registrar mais uma venda?: ')
    
    if continuar == 'N':
        print(f'{nome_comprador}, sua compra foi finalizada com sucesso. Volte sempre!' )
        break


