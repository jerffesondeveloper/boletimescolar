from rich import print
# Listas para armazenar os dados dos 
nome = []
data_nascimento = []
endereco = []
nome_mae = []
nome_pai = []
idade = []
matricula = []
nota = []
nota2 = []
nota3 = []

def menu():
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

# Função para cadastrar alu
def cadastro():
    matricula_inicial = 1001  # Matrícula começa em 1001
    
    no_input = input('Digite o nome do aluno: ')
    idade_input = input('Digite a idade: ')
    data_nasc_input = input('Digite a data de nascimento: ')
    endereco_input = input('Digite o endereço: ')
    mae_input = input('Digite o nome da mãe: ')
    pai_input = input('Digite o nome do pai: ')
    
    matricula_gerada = matricula_inicial + len(matricula)
    
    nome.append(no_input)
    idade.append(idade_input)
    data_nascimento.append(data_nasc_input)
    endereco.append(endereco_input)
    nome_mae.append(mae_input)
    nome_pai.append(pai_input)
    matricula.append(matricula_gerada)

    nota.append(None)
    nota2.append(None)
    nota3.append(None)

    print(f"\nAluno cadastrado com matrícula {matricula_gerada}.\n")

# Função para pesquisar alunos por nome ou matrícula
def pesquisar_aluno():
    opcao = input("Deseja pesquisar por [1] Nome ou [2] Matrícula? ")
    
    if opcao == '1':
        nome_pesquisa = input('Digite o nome do aluno: ')
        if nome_pesquisa in nome:
            index = nome.index(nome_pesquisa)
            exibir_informacoes(index)
        else:
            print('Aluno não encontrado.')
    
    elif opcao == '2':
        matricula_pesquisa = int(input('Digite a matrícula: '))
        if matricula_pesquisa in matricula:
            index = matricula.index(matricula_pesquisa)
            exibir_informacoes(index)
        else:
            print('Matrícula não encontrada.')
    else:
        print("Opção inválida.")

def exibir_informacoes(index):
    print(f"\nMatrícula: {matricula[index]}")
    print(f"Nome: {nome[index]}")
    print(f"Idade: {idade[index]}")
    print(f"Data de Nascimento: {data_nascimento[index]}")
    print(f"Endereço: {endereco[index]}")
    print(f"Nome da Mãe: {nome_mae[index]}")
    print(f"Nome do Pai: {nome_pai[index]}")

    primeira_nota = nota[index] if nota[index] is not None else "Não lançada"
    segunda_nota = nota2[index] if nota2[index] is not None else "Não lançada"
    terceira_nota = nota3[index] if nota3[index] is not None else "Não lançada"

    print(f"Primeira nota: {primeira_nota}")
    print(f"Segunda nota: {segunda_nota}")
    print(f"Terceira nota: {terceira_nota}")

    if None not in (nota[index], nota2[index], nota3[index]):
        media = (nota[index] + nota2[index] + nota3[index]) / 3
        print(f"Média: {media:.2f}")
    else:
        print("Média: Não disponível - notas incompletas")

def lancar_nota():
    matricula_pesquisa = int(input('Digite a matrícula: '))
    if matricula_pesquisa in matricula:
        index = matricula.index(matricula_pesquisa)
        print(f"Nome: {nome[index]}\n")

        print("""Qual nota deseja cadastrar:
              [1] Primeira Nota
              [2] Segunda Nota
              [3] Terceira Nota""")
        cadastro_nota = int(input("\t>>>"))

        if cadastro_nota == 1:
            nota_aluno = float(input('Digite a primeira nota do aluno: '))
            nota[index] = nota_aluno
            print("Primeira nota lançada com sucesso!")
        elif cadastro_nota == 2:
            nota_aluno = float(input('Digite a segunda nota do aluno: '))
            nota2[index] = nota_aluno
            print("Segunda nota lançada com sucesso!")
        elif cadastro_nota == 3:
            nota_aluno = float(input('Digite a terceira nota do aluno: '))
            nota3[index] = nota_aluno
            print("Terceira nota lançada com sucesso!")
        else:
            print("Opção inválida")
    else:
        print('Matrícula não encontrada')
    ...

