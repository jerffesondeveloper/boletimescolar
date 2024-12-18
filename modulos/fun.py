from rich import print
import modulos.cadastro as cadastro
# Listas para armazenar os dados dos 
nome = []
data_nascimento = []
endereco = []
nome_mae = []
nome_pai = []
idade = []
cadastro.matricula_inicial = []
nota = []
nota2 = []
nota3 = []

# Função que pesquisa somente notas
def pesquisar_notas():
    numero_matricula = int(input('Digite o número da cadastro.matricula_inicial: '))
    if numero_matricula in cadastro.matricula_inicial:
        index = cadastro.matricula_inicial.index(numero_matricula)
        exibir_notas(index)


def exibir_notas(index):
    print(f'Matrícula: {cadastro.matricula_inicial[index]}')
    print(f'Nome: {nome[index]}')

    primeira_nota = nota[index] if nota[index] is not None else "Não lançada"
    segunda_nota = nota2[index] if nota2[index] is not None else "Não lançada"
    terceira_nota = nota3[index] if nota3[index] is not None else "Não lançada"

    print('\n\tNOTAS\n')
    print(f'Primeira Nota\t {primeira_nota}')
    print(f'Segunda nota:\t {segunda_nota}')
    print(f'Terceira Nota:\t {terceira_nota}')

    if None not in (nota[index], nota2[index], nota3[index]):
        media = (nota[index] + nota2[index] + nota3[index]) / 3
        print(f"Média: {media:.2f}")
        if media >= 6:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')
    else:
        print("Média: Não disponível - notas incompletas")

def lancar_nota(matricula):
    matricula_pesquisa = int(input('Digite a matrícula: '))
    if matricula_pesquisa in cadastro.matricula:
        aluno = cadastro.alunos[matricula]
        print(f"Nome: {aluno['matricula']}\n")

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

