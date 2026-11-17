from datetime import date

dados_reservas = []

def inserir_reserva():
    nome = input("Insira o nome do que fez a reserva: ")
    email = input("Insira o email do que fez a reserva: ")
    tele = input("Insira o número de telemóvel do que fez a reserva: ")
    check_in = input("Insira o dia de chegada do que fez a reserva (dd/mm/yyyy): ")
    check_out = input("Insira o dia de saída do que fez a reserva (dd/mm/yyyy): ")
    hora_chegada = input("Insira a hora de chegada do que fez a reserva: ")
    tipo_quarto = input("Insira o tipo de quarto da reserva: ")
    quarto = input("Insira o quarto da reserva: ")
    preco = float(input("Insira o preço da reserva: "))
    pedidos = input("Insira quaisquer pedidos do que fez a reserva: ")

    dia_check_in = check_in.split("/")
    dia_check_out = check_out.split("/")
    dia_check_in = date(int(dia_check_in[2]), int(dia_check_in[1]), int(dia_check_in[0]))
    dia_check_out = date(int(dia_check_out[2]), int(dia_check_out[1]), int(dia_check_out[0]))
    dia_diferenca = (dia_check_out - dia_check_in).days

    dados_reservas = [nome, email, tele, check_in, check_out, 
                      dia_diferenca, hora_chegada, tipo_quarto,
                      quarto, preco, pedidos]

    print(dados_reservas)

inserir_reserva()