vendedores = 0
vendas = []
def analisar_vendas():
    global media, vendedores
    while True:
        venda = float(input("Digite o valor da venda, ou digite -1 para encerrar: "))
        vendas.append(venda)
        if venda == -1:
            print("Encerrando programa")
            break
        elif venda >= 5000:
            vendedores += 1

    media = sum(vendas) / len(vendas)
    print("\n Resultados na Universidade Federal de Santa Catarina")
    print(f"Média de vendas: {media}. ")
    print(f"A maior venda foi de {max(vendas)}!")
    print(f"A menor venda foi de {min(vendas)}!")
    print(f"Quantidade de vendedores com venda acimda de R$ 5000: {vendedores}")






if __name__ == "__main__":
    analisar_vendas()