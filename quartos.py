"""Módulo de gestão de quartos para a aplicação de consola (TP2)."""

ESTADOS_VALIDOS = ("Disponível", "Ocupado", "Manutenção")

# Estrutura de dados em memória: cada quarto é um dicionário com detalhes e histórico.
quartos = [
    {
        "id": 101,
        "tipo": "Standard",
        "cama": "Casal",
        "estado": "Disponível",
        "historico": [],
    },
    {
        "id": 102,
        "tipo": "Superior",
        "cama": "Duas Individuais",
        "estado": "Ocupado",
        "historico": ["Ana Silva"],
    },
    {
        "id": 103,
        "tipo": "Suite",
        "cama": "King Size",
        "estado": "Manutenção",
        "historico": ["João Pereira", "Maria Costa"],
    },
]


def _encontrar_quarto(id_quarto: int) -> dict | None:
    """Procura e devolve o dicionário do quarto correspondente ao ID, ou None."""
    for quarto in quartos:
        if quarto["id"] == id_quarto:
            return quarto
    return None


def listar_quartos() -> None:
    """Apresenta o inventário completo e os detalhes (tipo, cama, estado) dos quartos."""
    print("\n=== INVENTÁRIO E DETALHES DOS QUARTOS ===")
    if not quartos:
        print("Não existem quartos registados.")
        return

    for quarto in quartos:
        print(
            f"Quarto #{quarto['id']} | "
            f"Tipo: {quarto['tipo']} | "
            f"Cama: {quarto['cama']} | "
            f"Estado: {quarto['estado']}"
        )


def criar_quarto() -> None:
    """Operação CRUD (Create): adiciona um novo quarto ao inventário."""
    print("\n=== ADICIONAR QUARTO ===")
    try:
        id_quarto = int(input("Número/ID do quarto: ").strip())
    except ValueError:
        print("Erro: o ID do quarto tem de ser um número inteiro.")
        return

    if _encontrar_quarto(id_quarto) is not None:
        print(f"Erro: já existe um quarto com o ID {id_quarto}.")
        return

    tipo = input("Tipo de quarto (ex.: Standard, Superior, Suite): ").strip()
    cama = input("Tipo de cama (ex.: Casal, Individual, King Size): ").strip()

    if not tipo or not cama:
        print("Erro: o tipo de quarto e o tipo de cama não podem estar vazios.")
        return

    novo_quarto = {
        "id": id_quarto,
        "tipo": tipo,
        "cama": cama,
        "estado": "Disponível",
        "historico": [],
    }
    quartos.append(novo_quarto)
    print(f"Quarto #{id_quarto} adicionado com sucesso.")


def editar_estado_quarto() -> None:
    """Operação CRUD (Update): altera o estado do quarto e regista hóspede se ocupado."""
    listar_quartos()
    if not quartos:
        return

    try:
        id_quarto = int(input("\nID do quarto a atualizar: ").strip())
    except ValueError:
        print("Erro: introduza um número de ID válido.")
        return

    quarto = _encontrar_quarto(id_quarto)
    if quarto is None:
        print(f"Erro: quarto #{id_quarto} não encontrado.")
        return

    print(f"Estado atual do quarto #{id_quarto}: {quarto['estado']}")
    print("Estados disponíveis: Disponível, Ocupado, Manutenção")
    novo_estado = input("Novo estado: ").strip().capitalize()

    # Normaliza acentos mais comuns para facilitar a escrita na consola
    mapa_estados = {
        "Disponivel": "Disponível",
        "Disponível": "Disponível",
        "Ocupado": "Ocupado",
        "Manutencao": "Manutenção",
        "Manutenção": "Manutenção",
    }

    if novo_estado not in mapa_estados:
        print("Erro: estado inválido. Escolha Disponível, Ocupado ou Manutenção.")
        return

    estado_final = mapa_estados[novo_estado]
    quarto["estado"] = estado_final

    if estado_final == "Ocupado":
        hospede = input("Nome da pessoa que vai ocupar o quarto: ").strip()
        if hospede:
            quarto["historico"].append(hospede)
            print(f"Registado '{hospede}' no histórico do quarto #{id_quarto}.")
        else:
            print("Aviso: nome vazio; ninguém foi adicionado ao histórico.")

    print(f"Estado do quarto #{id_quarto} atualizado para '{estado_final}'.")


def ver_historico_quarto() -> None:
    """Consulta o histórico de pessoas que estiveram ou estão em cada quarto."""
    print("\n=== HISTÓRICO DE OCUPAÇÃO DOS QUARTOS ===")
    if not quartos:
        print("Não existem quartos registados.")
        return

    try:
        id_quarto = int(input("ID do quarto para consultar histórico: ").strip())
    except ValueError:
        print("Erro: introduza um número de ID válido.")
        return

    quarto = _encontrar_quarto(id_quarto)
    if quarto is None:
        print(f"Erro: quarto #{id_quarto} não encontrado.")
        return

    print(f"Histórico do Quarto #{quarto['id']} ({quarto['tipo']}):")
    if not quarto["historico"]:
        print("  Sem registo de ocupações anteriores.")
    else:
        for indice, pessoa in enumerate(quarto["historico"], start=1):
            print(f"  {indice}. {pessoa}")


def remover_quarto() -> None:
    """Operação CRUD (Delete): remove um quarto existente do inventário."""
    listar_quartos()
    if not quartos:
        return

    try:
        id_quarto = int(input("\nID do quarto a remover: ").strip())
    except ValueError:
        print("Erro: introduza um número de ID válido.")
        return

    quarto = _encontrar_quarto(id_quarto)
    if quarto is None:
        print(f"Erro: quarto #{id_quarto} não encontrado.")
        return

    quartos.remove(quarto)
    print(f"Quarto #{id_quarto} removido com sucesso.")


def menu_quartos() -> None:
    """Executa o menu interativo na consola para gerir os quartos."""
    while True:
        print("\n--- GESTÃO DE QUARTOS ---")
        print("1. Visualizar todos os quartos (inventário, tipo, cama e estado)")
        print("2. Adicionar quarto (Create)")
        print("3. Editar estado do quarto (Update)")
        print("4. Consultar histórico de hóspedes")
        print("5. Remover quarto (Delete)")
        print("0. Voltar / Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_quartos()
        elif opcao == "2":
            criar_quarto()
        elif opcao == "3":
            editar_estado_quarto()
        elif opcao == "4":
            ver_historico_quarto()
        elif opcao == "5":
            remover_quarto()
        elif opcao == "0":
            print("A sair do menu de quartos...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_quartos()