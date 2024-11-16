from rich import print

#chama o menu do módulo cadastro
def menu_cadastro():
    while True:
        print("\nEscolha uma opção:")
        print("[1] Cadastrar Aluno")
        print("[2] Pesquisar Aluno")
        print("[3] Sair")
        
        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == '1':
            cadastro()  # Chama a função de cadastro
        elif opcao == '2':
            pesquisar_aluno()  # Chama a função de pesquisa
        elif opcao == '3':
            print("Saindo...")
            break  # Encerra o programa
        else:
            print("Opção inválida. Tente novamente.")

# cadastro na turma
def cadastro_turma():
    while True:
        matricula_turma = int(input('Digite a matrícula: '))

        if matricula_turma == int:
             if matricula_turma in matricula:
                  index = matricula.index(matricula_turma)
                  print(f'Deseja adicionar o aluno(a) {index} em qual turma? ')
                  print('''\n
                    [1] ANO
                    [2] ANO
                    [3] ANO
                    [4] ANO
                    [5] ANO
                    [6] ANO
                    [7] ANO
                    [8] ANO
                    [9] ANO                 
                        ''')
                  lancamento_turma =  int(input('>>>'))
                  if lancamento_turma == 1:
                       ano_1.append(lancamento_turma)
                  
        else:
             print('Algo de errado aconteceu. Você pode ter digitado a matrícula errada')


# cadastro de alunos
def cadastro():
    matricula_inicial = 1001  # Matrícula começa em 1001
    
    no_input = input('Digite o nome do aluno: ')
    data_nasc_input = input('Digite a data de nascimento: ')
    endereco_input = input('Digite o endereço: ')
    mae_input = input('Digite o nome da mãe: ')
    pai_input = input('Digite o nome do pai: ')
    
    matricula_gerada = matricula_inicial + len(matricula)
    
    nome.append(no_input)
    data_nascimento.append(data_nasc_input)
    endereco.append(endereco_input)
    nome_mae.append(mae_input)
    nome_pai.append(pai_input)
    matricula.append(matricula_gerada)

    print(f"\nAluno cadastrado com matrícula {matricula_gerada}.\n")

# pesqusia de aluno simples
def pesquisar_aluno():
    matricula_pesquisa = int(input('Digite a matrícula: '))
    if matricula_pesquisa in matricula:
            index = matricula.index(matricula_pesquisa)
            exibir_informacoes(index)
    else:
            print('Matrícula não encontrada.')
   

# exibir informações
def exibir_informacoes(index):
    print(f"\nMatrícula: {matricula[index]}")
    print(f"Nome: {nome[index]}")
    print(f"Data de Nascimento: {data_nascimento[index]}")
    print(f"Endereço: {endereco[index]}")
    print(f"Nome da Mãe: {nome_mae[index]}")
    print(f"Nome do Pai: {nome_pai[index]}")


# variáveis
nome = []
data_nascimento = []
endereco = []
nome_mae = []
nome_pai = []
idade = []
matricula = []
ano_1 = []
ano_2 = []
ano_3 = []
ano_4 = []
ano_5 = []
ano_6 = []
ano_7 = []
ano_8 = []
ano_9 = []