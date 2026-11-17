
import json
import os

FICHEIRO = "Dados_Funcionarios.json"

Dados_Funcionarios = []

Funcoes = {
    "1": "Rececionista",
    "2": "Limpeza",
    "3": "Serviço de quartos",
    "4": "Cozinheiro",
    "5": "Empregado de mesa",
    "6": "Segurança",
    "7": "Manutenção"
}


# GUARDAR FUNCIONÁRIOS NO FICHEIRO

def guardar_funcionarios():
    with open(FICHEIRO, "w", encoding="utf-8") as ficheiro:
        json.dump(Dados_Funcionarios, ficheiro, ensure_ascii=False, indent=4)


# CARREGAR FUNCIONÁRIOS DO FICHEIRO

def carregar_funcionarios():
    global Dados_Funcionarios

    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as ficheiro:
            Dados_Funcionarios = json.load(ficheiro)


def inserir_funcionarios():
    print("\n--- CRIAR FUNCIONÁRIO ---")

    NomeF = input("Nome do funcionário: ")
    IdadeF = int(input("Idade do funcionário: "))
    TelemovelF = input("Número de telemóvel: ")

    print("\nFunções disponíveis:")
    for numero, funcao in Funcoes.items():
        print(numero, "-", funcao)

    FuncaoF = input("Função do funcionário (1-7): ")

    if FuncaoF in Funcoes:
        FuncaoF = Funcoes[FuncaoF]
    else:
        print("Função inválida!")
        return

    SalarioF = float(input("Salário do funcionário: "))
    HorarioF = input("Horário do funcionário: ")

    funcionario = [NomeF, IdadeF, TelemovelF,
                   FuncaoF, SalarioF, HorarioF]

    Dados_Funcionarios.append(funcionario)

    guardar_funcionarios()

    print("\nFuncionário criado com sucesso!")


def ver_funcionarios():
    print("\n--- LISTA DE FUNCIONÁRIOS ---")

    if len(Dados_Funcionarios) == 0:
        print("Não existem funcionários registados.")
    else:
        for i in range(len(Dados_Funcionarios)):
            print("\nFuncionário", i + 1)
            print("Nome:", Dados_Funcionarios[i][0])
            print("Idade:", Dados_Funcionarios[i][1])
            print("Telemóvel:", Dados_Funcionarios[i][2])
            print("Função:", Dados_Funcionarios[i][3])
            print("Salário:", Dados_Funcionarios[i][4], "€")
            print("Horário:", Dados_Funcionarios[i][5])


def editar_funcionario():
    ver_funcionarios()

    if len(Dados_Funcionarios) == 0:
        return

    numero = int(input("\nQual o número do funcionário que deseja editar? "))

    if numero < 1 or numero > len(Dados_Funcionarios):
        print("Número inválido!")
        return

    funcionario = Dados_Funcionarios[numero - 1]

    print("\n--- EDITAR FUNCIONÁRIO ---")
    print("Deixe em branco aquilo que não pretende alterar.")

    NomeF = input("Novo nome (" + funcionario[0] + "): ")
    if NomeF != "":
        funcionario[0] = NomeF

    IdadeF = input("Nova idade (" + str(funcionario[1]) + "): ")
    if IdadeF != "":
        funcionario[1] = int(IdadeF)

    TelemovelF = input("Novo telemóvel (" + str(funcionario[2]) + "): ")
    if TelemovelF != "":
        funcionario[2] = TelemovelF

    print("\nFunções disponíveis:")
    for numeroF, funcao in Funcoes.items():
        print(numeroF, "-", funcao)

    FuncaoF = input("Nova função (atual: " + funcionario[3] + "): ")
    if FuncaoF != "":
        if FuncaoF in Funcoes:
            funcionario[3] = Funcoes[FuncaoF]
        else:
            print("Função inválida! Mantida a função anterior.")

    SalarioF = input("Novo salário (" + str(funcionario[4]) + "): ")
    if SalarioF != "":
        funcionario[4] = float(SalarioF)

    HorarioF = input("Novo horário (" + funcionario[5] + "): ")
    if HorarioF != "":
        funcionario[5] = HorarioF

    guardar_funcionarios()

    print("\nFuncionário editado com sucesso!")


def eliminar_funcionario():
    ver_funcionarios()

    if len(Dados_Funcionarios) == 0:
        return

    numero = int(input("\nQual o número do funcionário que deseja eliminar? "))

    if numero < 1 or numero > len(Dados_Funcionarios):
        print("Número inválido!")
        return

    confirmacao = input("Tem a certeza que deseja eliminar este funcionário? (S/N): ")

    if confirmacao.upper() == "S":
        Dados_Funcionarios.pop(numero - 1)

        guardar_funcionarios()

        print("Funcionário eliminado com sucesso!")
    else:
        print("Operação cancelada.")


# CARREGAR DADOS AO INICIAR O PROGRAMA

carregar_funcionarios()


# MENU PRINCIPAL

while True:

    print("\n========== GESTÃO DE FUNCIONÁRIOS ==========")
    print("1 - Ver funcionários")
    print("2 - Criar funcionário")
    print("3 - Editar funcionário")
    print("4 - Eliminar funcionário")
    print("5 - Sair")
    print("============================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_funcionarios()

    elif opcao == "2":
        inserir_funcionarios()

    elif opcao == "3":
        editar_funcionario()

    elif opcao == "4":
        eliminar_funcionario()

    elif opcao == "5":
        print("A sair do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
