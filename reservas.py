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
    check_in = input("Dia de chegada de quem fez a reserva (dd/mm/yyyy): ")
    check_out = input("Dia de saída de quem fez a reserva (dd/mm/yyyy): ")
    hora_chegada = input("Hora de chegada de quem fez a reserva: ")
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
            print("Duração:", dados_reservas[i][6], "dias")
            print("Hora de chegada:", dados_reservas[i][7])
            print("Tipo de quarto:", dados_reservas[i][8])
            print("Quarto:", dados_reservas[i][9])
            print("Preço:", dados_reservas[i][10], "€")
            print("Pedidos:", dados_reservas[i][11])

def editar_reserva():
    pass

def remover_reserva():
    pass



carregar_reservas()

while True:
    op = int(input("\n\nO que quer fazer? \n" \
    "1 - Inserir reserva\n" \
    "2 - Ver reservas\n" \
    "3 - Editar reserva\n" \
    "4 - Remover reserva\n"))
    match op:
        case 1:
            inserir_reserva()
        case 2:
            ver_reservas()
        case 3:
            editar_reserva()
        case 4:
            remover_reserva()
        
