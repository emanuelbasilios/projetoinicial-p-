carrinho = []
while True:
    print('Bem vindo ao menu')
    print('1 - Adicionar produto')
    print('2 - Editar produto')
    print('3 - Remover produto')
    print('4 - Listar todos os produtos ')
    print('5 - Sair')
    opcao = input('Selecione a opção: ')
    if opcao == '1':
        produto = input('Digite o nome do produto: ')
        carrinho.append(produto)
        print('Produto adicionado com sucesso!')
    elif opcao == '2':
        produto = input('Digite o produto que deseja editar: ')
        if produto in carrinho:
            indice = carrinho.index(produto)
            carrinho[indice] = input('Digite o nome do novo produto:')
            print('Produto editado com sucesso!')
        else:
            print('Produto não encontrado!')
    elif opcao == '3':
        produto = input('Digite o nome do produto que deseja remover!')
        if produto in carrinho:
            carrinho.remove(produto)
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado!')
    elif opcao == '4':
        print(carrinho)
    elif opcao == '5':
        print('Obrigado pela visita!')
        break
