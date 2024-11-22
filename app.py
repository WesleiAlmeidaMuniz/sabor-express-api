import os

restaurantes = [
    {'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome':'Pizza Superma', 'categoria': 'Italiana', 'ativo': True},
    {'nome':'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

def exibir_nome_do_programa():
    '''Essa função exibe o nome do aplicativo'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função imprimi as opções do aplicativo na tela'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função exibe a mensagem final do aplicativo'''
    exibir_subtitulo('Finalizando o app...')

def voltar_ao_menu_principal():
    '''Essa função solicita uma tecla para retorna ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa função é invocada quando uma opção é inválida e retorna ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função cria um subtitulo utilizando o parametro
    
    Inputs:
    - texto: str - O texto do subtítulo

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurante

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}


    restaurantes.append(dados_do_restaurante) #append é igual ao push do javascript

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista todos os restaurantes'''
    exibir_subtitulo('Listando os restaurantes')

    print(f"{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função altera o estado do restaurante para ativo ou inativo'''
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    '''Essa função mapeia as opções conforme o input do usuario'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))           

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()