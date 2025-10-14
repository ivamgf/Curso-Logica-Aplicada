valores_venda = []

while True:
    try:
        valor_input = input("Digite o valor da venda: ")
        valor_venda = float(valor_input)

        if valor_venda == -1:
            break
        elif valor_venda >= 0:
            valores_venda.append(valor_venda)
        else:
            print("Valor inválido. Digite um valor positivo ou -1 para sair.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

total_vendedores = len(valores_venda)

if total_vendedores > 0:
    maior_venda = max(valores_venda)
    menor_venda = min(valores_venda)
    acima_de_5000 = sum(1 for venda in valores_venda if venda > 5000)
    media_vendas = sum(valores_venda) / total_vendedores

    print("\nResultados:")
    print(f"Total de vendedores: {total_vendedores}")
    print(f"Maior venda: R$ {maior_venda:.2f}")
    print(f"Menor venda: R$ {menor_venda:.2f}")
    print(f"Quantidade de vendedores com venda acima de R$ 5000: {acima_de_5000}")
    print(f"Média de vendas: R$ {media_vendas:.2f}")
else:
    print("Nenhuma venda foi inserida.")