print('Bem-vindo à livraria da Milena Magno.')
lista_livro = []
id_global = 0

def cadastrar_livro(ID):
    #Pergunta os dados do livro desejado (nome, autor e editora) e cadastra o livro
    NOME = input('Qual o nome do livro? ')
    AUTOR = input('Qual o autor do livro? ')
    EDITORA = input('Qual a editora do livro? ')
    livro = {'ID': ID, 'NOME': NOME, 'AUTOR': AUTOR, 'EDITORA': EDITORA}
    lista_livro.append(livro)
    print('O livro foi cadastrado com sucesso!')

def consultar_livro():
    #Consulta o livro de acordo com a escolha do usuário
    while True:
        print('Escolha a opção desejada:')
        print('1. Consultar todos os livros')
        print('2. Consultar livro por ID')
        print('3. Consultar livro por Autor')
        print('4. Retornar')
        opcao = input('>>')
        if opcao == '1':
            for livro in lista_livro:
                print(livro)
        elif opcao == '2':
            id_consulta = int(input('Qual o ID do livro? '))
            ID = next((livro for livro in lista_livro if livro['ID'] == id_consulta), None)
            print(ID if ID else 'Não há livro cadastrado com esse ID.')
        elif opcao == '3':
            autor_consulta = input('Qual o autor? ')
            livros_autor = [livro for livro in lista_livro if livro['AUTOR'] == autor_consulta]
            if livros_autor:
                for livro in livros_autor:
                    print(livro)
            else:
                print('Não há livro cadastrado desse autor.')
        elif opcao == '4':
            break
        else:
            print('Opcão inválida.')


def remover_livro():
    #Pergunta qual ID do livro que o usuário deseja remover e remove o livro correspondente
    while True:
        id_remover = int(input('Qual o ID do livro que deseja remover? '))
        for livro in lista_livro:
            if livro['ID'] == id_remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                return
        print('ID inválido.')

#Programa principal
while True:
    print('-'*34)
    print('--------- MENU PRINCIPAL ---------')
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar livro')
    print('2 - Consultar livro(s)')
    print('3 - Remover livro')
    print('4 - Sair')
    opcao = input('>>')
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print('Saindo do pragrama...')
        break
    else:
        print('Opcão inválida.') 
