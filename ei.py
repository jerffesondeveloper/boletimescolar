# Estrutura para armazenar alunos por turma
turmas = {
    "Turma A": [
        {"nome": "João", "matricula": 101, "idade": 16},
        {"nome": "Maria", "matricula": 102, "idade": 17}
    ],
    "Turma B": [
        {"nome": "Carlos", "matricula": 201, "idade": 18},
        {"nome": "Ana", "matricula": 202, "idade": 16}
    ]
}

# Função para adicionar um aluno a uma turma
def adicionar_aluno(turma, nome, matricula, idade):
    if turma not in turmas:
        turmas[turma] = []
    turmas[turma].append({"nome": nome, "matricula": matricula, "idade": idade})

# Função para puxar alunos de uma turma
def listar_alunos(turma):
    if turma in turmas:
        return turmas[turma]
    else:
        return f"Turma {turma} não encontrada."

# Adicionar um aluno à Turma A
adicionar_aluno("Turma A", "Paulo", 103, 17)

# Listar alunos da Turma A
print(listar_alunos("Turma A"))
