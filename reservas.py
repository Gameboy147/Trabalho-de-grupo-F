from datetime import date
import os
import json

file = "lista_reservas.json"
dados_reservas = []

def guardar_reservas():
    with open(file, "w", encoding="utf-8") as ficheiro:
        json.dump(dados_reservas, ficheiro, ensure_ascii=False)
        ficheiro.write("\n")

def carregar_reservas():
    global dados_reservas

    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as ficheiro:
            dados_reservas = json.load(ficheiro)
    else:
        dados_reservas = []

def inserir_reserva():
    print("\n--- CRIAR RESERVA ---")

    nome = input("Nome de quem fez a reserva: ")
    email = input("Email de quem fez a reserva: ")
    tele = input("Número de telemóvel de quem fez a reserva: ")
    check_in = input("Dia de chegada da reserva (dd/mm/yyyy): ")
    check_out = input("Dia de saída da reserva (dd/mm/yyyy): ")
    hora_chegada = input("Hora de chegada da reserva: ")
    tipo_quarto = input("Tipo de quarto da reserva: ")
    quarto = input("Quarto da reserva: ")
    preco = float(input("Preço da reserva: "))
    pedidos = input("Quaisquer pedidos de quem fez a reserva: ")

    dia_check_in = check_in.split("/")
    dia_check_out = check_out.split("/")
    dia_check_in = date(int(dia_check_in[2]), int(dia_check_in[1]), int(dia_check_in[0]))
    dia_check_out = date(int(dia_check_out[2]), int(dia_check_out[1]), int(dia_check_out[0]))
    dia_diferenca = (dia_check_out - dia_check_in).days

    reserva = [nome, email, tele, check_in, check_out, 
                      dia_diferenca, hora_chegada, tipo_quarto,
                      quarto, preco, pedidos]

    dados_reservas.append(reserva)

    guardar_reservas()

    print("\nReserva inserida com sucesso!")

def ver_reservas():
    print("\n--- LISTA DE RESERVAS ---")

    if len(dados_reservas) == 0:
        print("Não existem reservas registadas.")
    else:
        for i in range(len(dados_reservas)):
            print("\nReserva", i + 1)
            print("Nome:", dados_reservas[i][0])
            print("Email:", dados_reservas[i][1])
            print("Telemóvel:", dados_reservas[i][2])
            print("Check-in:", dados_reservas[i][3])
            print("Check-out:", dados_reservas[i][4])
            print("Duração:", dados_reservas[i][5], "dias")
            print("Hora de chegada:", dados_reservas[i][6])
            print("Tipo de quarto:", dados_reservas[i][7])
            print("Quarto:", dados_reservas[i][8])
            print("Preço:", dados_reservas[i][9], "€")
            print("Pedidos:", dados_reservas[i][10])

def editar_reserva():
    numero = int(input("\nQual o número da reserva que quer editar? "))

    if numero < 1 or numero > len(dados_reservas):
        print("Número inválido!")
        return

    reserva = dados_reservas[numero - 1]

    print("\n--- EDITAR RESERVA ---")
    print("Deixe em branco aquilo que não pretende alterar.")

    nome = input("Novo nome (" + reserva[0] + "): ")
    if nome != "":
        reserva[0] = nome

    email = input("Novo email (" + reserva[1] + "): ")
    if email != "":
        reserva[1] = email

    tele = input("Novo telemóvel (" + reserva[2] + "): ")
    if tele != "":
        reserva[2] = tele

    check_in = input("Novo check-in (" + reserva[3] + "): ")
    if check_in != "":
        reserva[3] = check_in

    check_out = input("Novo check-out (" + reserva[4] + "): ")
    if check_out != "":
        reserva[4] = check_out

    hora_chegada = input("Nova hora de chegada (" + reserva[6] + "): ")
    if hora_chegada != "":
        reserva[6] = hora_chegada

    tipo_quarto = input("Novo tipo de quarto (" + reserva[7] + "): ")
    if tipo_quarto != "":
        reserva[7] = tipo_quarto

    quarto = input("Novo quarto (" + reserva[8] + "): ")
    if quarto != "":
        reserva[8] = quarto

    preco = input("Novo preço (" + str(reserva[9]) + "): ")
    if preco != "":
        reserva[9] = float(preco)

    pedidos = input("Novos pedidos (" + reserva[10] + "): ")
    if pedidos != "":
        reserva[10] = pedidos

    guardar_reservas()

    print("\nReserva editada com sucesso!")


def remover_reserva():
    numero = int(input("\nQual o número da reserva que quer eliminar? "))

    if numero < 1 or numero > len(dados_reservas):
        print("Número inválido!")
        return

    confirmacao = input("Tem a certeza que quer eliminar esta reserva? (s/n): ")

    if confirmacao.lower() == "s":
        dados_reservas.pop(numero - 1)

        guardar_reservas()

        print("Reserva eliminada com sucesso!")
    else:
        print("Operação cancelada.")



carregar_reservas()

while True:
    op = int(input("\n\nO que quer fazer? \n" \
    "1 - Inserir reserva\n" \
    "2 - Ver reservas\n" \
    "3 - Editar reserva\n" \
    "4 - Remover reserva\n" \
    "5 - Sair\n"))
    match op:
        case 1:
            inserir_reserva()
        case 2:
            ver_reservas()
        case 3:
            editar_reserva()
        case 4:
            remover_reserva()
        case 5:
            print("\nA sair...")
            break
