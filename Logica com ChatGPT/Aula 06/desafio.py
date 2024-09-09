vendas = []
faturamento_total = 0
comprador_mais_gastador = ("", 0)

while True: 
    nome_do_comprador = input('Digite o nome do comprador: ')
    preço_da_compra = float(input('Qual o preço: '))

    faturamento_total += preço_da_compra 

    if preço_da_compra > comprador_mais_gastador[1]:
        comprador_mais_gastador = (nome_do_comprador, preço_da_compra)

    vendas = input('Olá você deseja registrar mais uma venda :').upper()
    if vendas == 'N':
        break
    elif vendas == 'S':
        continue
        
print(f"Faturamento total: {faturamento_total:.2f}")


if comprador_mais_gastador[1] == 0:
    print("Nenhum comprador registrou compras.")
else:
    print("O comprador que gastou mais foi:", comprador_mais_gastador[0], "com um total de", comprador_mais_gastador[1])