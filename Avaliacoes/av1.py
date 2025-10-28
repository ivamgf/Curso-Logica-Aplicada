# função
def analisar_vendas(vendas):
  total_vendedores = len(vendas)
  if total_vendedores == 0:
    return 0, 0, 0, 0, 0

  maior_venda = max(vendas)
  menor_venda = min(vendas)
  vendas_acima_5000 = sum(1 for venda in vendas if venda > 5000)
  media_vendas = sum(vendas) / total_vendedores

  return total_vendedores, maior_venda, menor_venda, vendas_acima_5000, media_vendas

# programa

vendas = []

while True:
  try:
    valor_venda_str = float(input('Digite o valor da venda: '))
    valor_venda = float(valor_venda_str)

    if valor_venda == -1:
        break
    elif valor_venda < 0:
      print('Valor de venda inválido. Por favor, digite um valor positivo ou -1 para sair')
    else:
      vendas.append(valor_venda)
  except ValueError:
    print('Valor de venda inválido. Por favor, digite um valor numérico')

if vendas:
  total_vendedores, maior_venda, menor_venda, vendas_acima_5000, media_vendas = analisar_vendas(vendas)

  print(f'\Resultados:')
  print(f'Total de vendedores: {total_vendedores}')
  print(f'Maior venda: R$ {maior_venda:.2f}')
  print(f'Menor venda: R$ {menor_venda:.2f}')
  print(f'Quantidade de vendedores com venda acima de R$ 5000: {vendas_acima_5000}')
  print(f'Média de vendas: R$ {media_vendas:.2f}')
else:
  print('Nenhuma venda foi registrada')
