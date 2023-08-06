#inicialização do array de colaboradores
lista_colaboradores = []

#função para cadastro de colaborador
def cadastrar_colaborador(id):
    nome = input("Insira o nome do colaborador: ")
    setor = input("Insira o setor do colaborador: ")
    salário = float(input("Insira o salário do colaborador: "))

    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salário": salário
    }

    lista_colaboradores.append(colaborador)

#função para consulta de colaborador
def consultar_colaborador():
    while True:
        print('\nOpções de consulta\n 1 - Consultar todos \n 2 - Consultar por Id \n 3 - Consultar por Setor \n 4 - Retornar ao menu')
        
        try:
            switch = int(input("Insira a opção desejada: "))
            if switch == 1:
                #consulta de todos os colaboradores
                print("\nConsultar todos os colaboradores:")
                for colaborador in lista_colaboradores:
                    print(colaborador)
            elif switch == 2:
                #consulta de colaborador por id
                consultaID = int(input("Insira o ID do colaborador desejado: "))
                for colaborador in lista_colaboradores:
                    if colaborador["id"] == consultaID:
                        print(f"\n Colaborador com id {consultaID}:")
                        print(colaborador)
                        break
                else:
                    print(f"ID {consultaID} não encontrado.")
            elif switch == 3:
                #consulta de colaborador por setor
                consultaSetor = input("Digite o setor desejado: ")
                print(f"\nColaboradores do setor {consultaSetor}:")
                for colaborador in lista_colaboradores:
                    if colaborador["setor"].lower() == consultaSetor.lower():
                        print(colaborador)
            elif switch == 4:
                break
            else:
                print("Opção inválida, por favor tente novamente.")
        except ValueError:
            print("Por favor, digite um valor numérico.")

#função para remoção de colaborador
def remover_colaborador():
    removerID = int(input("Insira o id que deseja remover: "))
    for i, colaborador in enumerate(lista_colaboradores):
        if colaborador["id"] == removerID:
            del lista_colaboradores[i]
            print(f"Colaborador com ID {removerID} removido.")
            break
    else:
        print(f"ID {removerID} não encontrado.")

#função principal do programa, por ela iremos chamar as outras funções e encerrar o programa quando desejado.
def main():
    id_global = 0
    print("Bem vindo ao controle de colaboradores do Abraao Rocha de Paula")
    
    while True:
        print("\nMenu: \n 1 - Cadastrar Colaborador \n 2 - Consultar Colaborador \n 3 - Remover Colaborador \n 4 - Encerrar Programa")

        try:
            opcao_menu = int(input("Insira a operação desejada: "))
            if opcao_menu == 1:
                cadastrar_colaborador(id_global)
                id_global += 1
            elif opcao_menu == 2:
                consultar_colaborador()
            elif opcao_menu == 3:
                remover_colaborador()
            elif opcao_menu == 4:
                print("Programa encerrado")
                break
            else:
                print("Opção inválida, por favor tente novamente.")
        except ValueError:
            print("Por favor, digite um valor numérico.")

#chamada da função principal
main()
