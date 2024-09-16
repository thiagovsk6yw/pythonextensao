# Imprime o menu do restaurante
print('================================= \n| COD |     PRODUTO     | VALOR | \n| 100 | Parmegiana      |19,00R$| \n'
      '| 101 | Estrogonoff de frango|19,00R$|\n| 102 | Panqueca de carne|16,50R$|\n| 103 | Bife acebolado  |18,00R$| \n'
      '| 104 | Picadinho|16,00R$|\n| 105 | Suco            |5,00R$| \n| 106 | Refrigerante    |5,00R$|\n'
      '=================================\n Para sair digite 0')

# Define o menu como um dicionário
menu = {

    '101': ['Estrogonoff de frango', 19.00],
    '102': ['Panqueca de carne', 16.50],
    '103': ['Bife acebolado', 18.00],
    '104': ['Picadinho', 16.00],
    '100': ['Parmegiana', 19.00],
    '105': ['Suco', 5.00],
    '106': ['Refrigerante', 5.00]
}

# Inicializa o pedido como um dicionário vazio
pedido = {}

# Loop infinito para coletar os pedidos
while True:
    # Solicita o código do produto
    codigo = input('Informe o codigo: ')
    
    # Verifica se o usuário deseja sair
    if (codigo == '0'):
        break
    
    # Verifica se o código é válido
    if codigo in menu:
        # Solicita a quantidade do produto
        quantidade = int(input('Informe a quantidade: '))
        
        # Verifica se a quantidade é válida
        if quantidade > 0:
            # Obtém o valor do produto
            valorItem = menu.get(codigo)
            
            # Adiciona o produto ao pedido
            pedido.update({codigo: (valorItem, quantidade)})

# Inicializa o valor total do pedido
valorDoPedido = 0

# Calcula o valor total do pedido
for linha in pedido.items():
    valorDoPedido += linha[1][0][1] * linha[1][1]  # Preço * Quantidade

# Imprime o pedido
print('\nSEU PEDIDO: ')

# Imprime cada item do pedido
for linha in pedido.items():
    print(f"{linha[1][1]} x {linha[1][0][0]} - R$ {round(linha[1][0][1] * linha[1][1], 2)}")

# Imprime o valor total do pedido
print(f"\nTOTAL DO PEDIDO: R$ {round(valorDoPedido, 2)}")

# Pergunta se o usuário deseja calcular o troco
calcular_troco = input("\nDeseja calcular o troco? (S/N): ")

if calcular_troco.upper() == "S":
    # Solicita o valor pago pelo cliente
    valor_pago = float(input("Informe o valor pago: "))
    
    # Calcula o troco
    troco = valor_pago - valorDoPedido
    
    # Imprime o troco
    print(f"\nTROCO: R$ {round(troco, 2)}")

# Pergunta se o usuário deseja imprimir o pedido em um arquivo
imprimir_arquivo = input("\nDeseja imprimir o pedido em um arquivo? (S/N): ")

if imprimir_arquivo.upper() == "S":
    # Solicita o nome do arquivo
    nome_arquivo = input("Informe o nome do arquivo: ")
    
    # Abre o arquivo em modo de escrita
    with open(nome_arquivo + ".txt", "w") as arquivo:
        # Escreve o pedido no arquivo
        arquivo.write("SEU PEDIDO:\n")
        for linha in pedido.items():
            arquivo.write(f"{linha[1][1]} x {linha[1][0][0]} - R$ {round(linha[1][0][1] * linha[1][1], 2)}\n")
        arquivo.write(f"\nTOTAL DO PEDIDO: R$ {round(valorDoPedido, 2)}")
    
    # Imprime uma mensagem de confirmação
    print(f"\nPedido impresso no arquivo {nome_arquivo}.txt")