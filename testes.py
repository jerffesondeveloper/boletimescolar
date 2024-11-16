from midias import sons
from playsound import playsound


matricula = [1001]
ano_1 = []
nome = ['jerffeson']

def cadastro_turma():
    while True:
        matricula_turma = int(input('Digite a matrícula: '))

        if matricula_turma in matricula:
            index = matricula.index(matricula_turma)
            print(f'Deseja adicionar o aluno(a) {nome[index]} em qual turma? ')
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
                playsound(midias\)
                print(f'{nome[index]} foi matriculado no 1° ano com sucesso!')
                  
        else:
             print('Algo de errado aconteceu. Você pode ter digitado a matrícula errada')

cadastro_turma()