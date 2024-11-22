def exercicio1():
    numero = int(input('Digite um numero: ' ))

    if (numero % 2) == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')


def exercicio2():
    idade = int(input('Qual a sua idade? '))

    if 0< idade <= 12:
        print('Você ainda é uma criança.')
    elif 12 < idade < 18:
        print('Você é um adolescente')
    elif idade >= 18:
        print('Você é um adulto')
    else:
        print('Valor inválido!')

def exercicio3():
    login = input('Digite o seu login:')
    senha = input('Digite sua senha: ')

    if login == 'weslei' and senha == 'senha123':
        print('Você está logado!')
    else:
        print('Login ou senha incorreta!')

def exercicio4():
    cordenadas_x = int(input('Digite a cordenada X: '))
    cordenadas_y = int(input('Digite a cordenada Y: '))

    # if 0 < cordenadas_x and 0 < cordenadas_y:
    #     print('Você está no primeiro quadrante')
    # elif cordenadas_x < 0 and 0 < cordenadas_y:
    #     print('Você está no segundo quadrante')
    # elif cordenadas_x < 0 and cordenadas_y < 0:
    #     print('Você está no terceiro quadrante')
    # elif 0 < cordenadas_x and cordenadas_y < 0:
    #     print('Você está no quarto quadrante')
    # else:
    #     print('Você está no ponto de origem')

    if cordenadas_x > 0 and cordenadas_y > 0:
        print("O ponto está no primeiro quadrante.")
    elif cordenadas_x < 0 and cordenadas_y > 0:
        print("O ponto está no segundo quadrante.")
    elif cordenadas_x < 0 and cordenadas_y < 0:
        print("O ponto está no terceiro quadrante.")
    elif cordenadas_x > 0 and cordenadas_y < 0:
        print("O ponto está no quarto quadrante.")
    else:
        print("O ponto está sobre um eixo ou na origem.")

def exercicio5():
    lista_1a10 = [1,2,3,4,5,6,7,8,9,10]
    lista_nomes = ['Weslei', 'João', 'Vinny', 'Monte']
    lista_ano = [1996, 2024]

    print(lista_1a10)
    print(lista_nomes)
    print(lista_ano)


def exercicio6():
    lista = [1,2,3,4,5,6,7,8,9,10]
    for numero in lista:
        print(numero)

def exercicio7():
    lista = [1,2,3,4,5,6,7,8,9,10]
    soma = 0
    for numero in lista:
        if numero % 2 == 1:
            soma = soma + numero

    print(soma)

def exercicio8():
    for i in range(10,0,-1):
        print(i)

def exercicio9():
    numero_tabuada = int(input('Digite um numero para a tabuada '))

    for i in range(1,11):
        print(f'{numero_tabuada} X {i} = {numero_tabuada * i}')


def exercicio10():
    lista = [10,10,8,5,3,5,13,25,None,1]
    soma = 0

    try:
        for i in lista:
            soma = soma + i
        print(soma)
    except:
        print(f'Valor inválido na posição {lista.index(i)}')

def exercicio11():
    lista = [10,10,8,5,3,5,13,25,1]
    soma = 0
    try:
        for i in lista:
            soma = soma + i
        
        print(f'A média dos valores é {soma/len(lista)}')
    except ZeroDivisionError:
        print('A lista está vazia, não é possível calcular a média.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


def exercicio12():
    pessoa = [{'nome': 'Weslei', 'idade': 28, 'cidade': 'Guarulhos'},
              {'nome': 'Gustavo', 'idade': 35, 'cidade': 'Santo André'}
            ]
    
    print(pessoa)

def exercicio13():
    pessoa = {'nome': 'Weslei', 'idade': 28, 'cidade': 'Guarulhos'}
    
    pessoa['idade'] = 30
    pessoa['profissão'] = 'Desenvolvedor'
    pessoa.pop('cidade')

    print(pessoa)

def exercicio14():
    quadrados = {}

    for i in range(1,6):
        quadrados.update({i: i**2})

    print(quadrados)

def exercicio15():
    pessoa = {'nome': 'Weslei', 'idade': 28, 'cidade': 'Guarulhos','profissão': 'Desenvolvedor'}
    chave = input('Digite a chave do dicionario: ')

    if chave in pessoa:
        print('A chave existe no dicionario pessoa')
    else:
        print('A chave não existe')

def exercicio16():
    frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
    contagem_palavras = {}
    palavras = frase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)


def main():
    exercicio16()
    
if __name__ == '__main__':
    main()