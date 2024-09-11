import os

#váriaveis
restaurantes= [{'nome':'Dona Italiana', 'categoria':'Italiana', 'ativo':True},
               {'nome':'Pollo Hermanos', 'categoria':'Mexicana', 'ativo':False},
               {'nome':'Sushibar', 'categoria':'Japonesa', 'ativo':True}
               ]

def exibir_nome_prog():
    print('+==========================+')
    print('+      Sabor Express       +')

def exibir_opcoes():    
    print('+  1.Cadastrar Restaurante +')
    print('+  2.Listar Restaurantes   +')
    print('+  3.Alterar status        +')
    print('+  4.Sair                  +')
    print('+--------------------------+')

def opcao_invalida():
    print('+   Opção invalída!                  +')
    voltar_menu_principal()

def voltar_menu_principal():
    print('+=============================================+')
    input('+ Aperte Enter para voltar as opções +')
    main()

def exibir_subtitulo(texto):
    ''' Função de padronização do subtitulo    '''
    os.system('cls')
    print('+===============================================+')
    print(f'+        {texto}             +')

def cadastrar_restaurante():
    '''Função para cadastrar novo restaurante
       Inputs
         Nome do restaurante
         categoria
       Outputs
         adiciona restaurante e categoria na lista
    '''
       
    exibir_subtitulo('Cadastrar Restaurante')
    nome_restaurante = input ('+ Insira o nome do restaurante:')
    categoria = input('Digite o nome da categoria: ')
    print(f'+ O restaurante {nome_restaurante} foi cadastrado\n na categoria {categoria} com sucesso! +')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulo(' Lista de restaurantes')
    print(f'{'+ Restaurante'.ljust(22)} | {'Categoria'.ljust(17)} | Ativo +')
    print('+----------------------------------------------------+')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao ='ativo' if restaurante['ativo'] else 'desativado'
        print(f'+ {nome_restaurante.ljust(20)} | {categoria.ljust(15)} | {situacao}')
    voltar_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Ativar Restaurante')
    restarante_encontrado=False
    nome_restaurante = input('+ Digite o nome do restaurante: ')
    for restaurante in restaurantes:
         if  nome_restaurante == restaurante['nome']:
             restarante_encontrado=True
             restaurante['ativo'] = not restaurante['ativo']
             if restaurante['ativo']== True:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso')  
             else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso')

    if not restarante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_menu_principal()

def finalizar_app():
    os.system('cls')
    print('+ Obrigado volte sempre!  +')

def escolher_opcoes():   
    try:
        opcao = int(input('+  Escolha uma opção: '))
        print(f'+ Você escolheu opção de Nº: {opcao}\n')
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurante()
        elif opcao == 3:
            ativar_restaurante()
        elif opcao == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    os.system('cls')
    exibir_nome_prog()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()