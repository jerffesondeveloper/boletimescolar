
from rich import print
import modulos.fun as fun

print("[on red]                                             ")
print("[blue bold on white]BEM VINDO AO SISTEMA DE GERENCIAMENTO ESCOLAR")
print("[on red]                                             \n")



while True:
    print("""\n\t[black bold on white]SELECIONA A OPÇÃO DESEJADA[/]\n
    
     [blue] 1 - CADASTRO OU PESQUSIA DE ALUNO
      2 - LANÇAMENTO DE NOTAS
      3 - CONSULTAR NOTAS  
      4 - SAIR[/]
      """)

    op = int(input('\t>>> '))

    if op == 1:
       
        fun.menu_cadastro()
       
    elif op == 2:
        
        fun.lancar_nota()

    elif op == 3:
        fun.pesquisar_notas()
        
    elif op == 4:
        print("\n\tVocê saiu\n")
        break
    else:
        print('\tOpção inválida\n')



    
