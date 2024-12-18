from rich import print
from playsound import playsound


# Chama o menu do módulo cadastro
def menu_cadastro():
    while True:
        print("\nEscolha uma opção:")
        print("[1] Cadastrar Aluno")
        print("[2] Pesquisar Aluno")
        print("[3] Matricular em turma")
        print("[4] Sair")
        
        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == '1':
            cadastro()  # Chama a função de cadastro
        elif opcao == '2':
            pesquisar_aluno()  # Chama a função de pesquisa
        elif opcao == '3':
            cadastro_turma()
        elif opcao == '4':
            print("Saindo...")
            break  # Encerra o programa
        else:
            print("Opção inválida. Tente novamente.")


# Cadastro de Alunos
def cadastro():
    matricula_inicial = 1001  # Matrícula começa em 1001

    no_input = input('Digite o nome do aluno: ')
    data_nasc_input = input('Digite a data de nascimento: ')
    endereco_input = input('Digite o endereço: ')
    mae_input = input('Digite o nome da mãe: ')
    pai_input = input('Digite o nome do pai: ')

    matricula_gerada = matricula_inicial + len(alunos)  # Gera matrícula sequencial
    matricula.append(matricula_gerada)

    # Cria o registro do aluno como dicionário
    aluno = {
        "matricula": matricula_gerada,
        "nome": no_input,
        "data_nascimento": data_nasc_input,
        "endereco": endereco_input,
        "nome_mae": mae_input,
        "nome_pai": pai_input,
        "turma": None  # Turma inicialmente nula
    }
    alunos[matricula_gerada] = aluno  # Adiciona ao dicionário principal

    print(f"\nAluno cadastrado com matrícula {matricula_gerada}.\n")


# Cadastro na Turma
def cadastro_turma():
    matricula_turma = int(input('Digite a matrícula: '))

    if matricula_turma in alunos:
        aluno = alunos[matricula_turma]
        print(f'Deseja adicionar o aluno(a) {aluno["nome"]} em qual turma? ')
        print('''\n
                [1] 1° ANO
                [2] 2° ANO
                [3] 3° ANO
                [4] 4° ANO
                [5] 5° ANO
                [6] 6° ANO
                [7] 7° ANO
                [8] 8° ANO
                [9] 9° ANO
                ''')

        lancamento_turma = int(input('>>> '))
        if lancamento_turma in turmas:
            turmas[lancamento_turma].append(aluno)  # Adiciona o aluno à turma
            aluno["turma"] = lancamento_turma  # Atualiza a turma no registro do aluno
            print(f'{aluno["nome"]} foi matriculado no {lancamento_turma}° ano com sucesso!')
            playsound('midias/sons/cotificacao_confirmacao.mp3')
        else:
            print("Turma inválida!")
    else:
        print('Matrícula não encontrada.')


# Pesquisa de Aluno
def pesquisar_aluno():
    matricula_pesquisa = int(input('Digite a matrícula: '))
    if matricula_pesquisa in alunos:
        exibir_informacoes(matricula_pesquisa)
    else:
        print('Matrícula não encontrada.')


# Exibir Informações de um Aluno
def exibir_informacoes(matricula):
    aluno = alunos[matricula]
    print(f"\nMatrícula: {aluno['matricula']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Data de Nascimento: {aluno['data_nascimento']}")
    print(f"Endereço: {aluno['endereco']}")
    print(f"Nome da Mãe: {aluno['nome_mae']}")
    print(f"Nome do Pai: {aluno['nome_pai']}")
    if aluno['turma']:
        print(f"Turma: {aluno['turma']}° ano")
    else:
        print("Turma: Não matriculado.")


# Variáveis
alunos = {}  # Estrutura principal para armazenar informações de alunos
turmas = {i: [] for i in range(1, 10)}  # Dicionário para armazenar as turmas
matricula = []


