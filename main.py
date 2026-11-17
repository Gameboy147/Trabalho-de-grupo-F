# --- Módulo de Gestão de Quartos (TP2 - Ambientes de Desenvolvimento Colaborativo) ---

# Estrutura de dados inicial para os quartos (Inventário, Detalhes e Histórico)
quartos = [
    {"id": 101, "tipo": "Casal", "cama": "King Size", "estado": "Disponível", "historico": []},
    {"id": 102, "tipo": "Twin", "cama": "Duas Individual", "estado": "Ocupado", "historico": ["Ana Silva"]},
    {"id": 103, "tipo": "Suite", "cama": "Queen Size", "estado": "Manutenção", "historico": []}
]

def listar_quartos():
    """Read: Permite ao funcionário visualizar todos os quartos, o seu inventário e detalhes."""
    print("\n--- Inventário e Detalhes dos Quartos ---")
    if not quartos:
        print("Não existem quartos registados.")
        return
    for q in quartos:
        print(f"ID: {q['id']} | Tipo: {q['tipo']} | Cama: {q['cama']} | Estado: {q['estado']}")

def adicionar_quarto():
    """Create: Permite adicionar um novo quarto ao inventário."""
    print("\n--- Adicionar Novo Quarto ---")
    try:
        id_quarto = int(input("ID do quarto (número): "))
        # Verificar se já existe
        if any(q['id'] == id_quarto for q in quartos):
            print(" Erro: Já existe um quarto com esse ID.")
            return
        
        tipo = input("Tipo de quarto (ex: Casal, Twin, Suite): ")
        cama = input("Tipo de cama (ex: King Size, Individual): ")
        estado = "Disponível"
        
        novo = {
            "id": id_quarto,
            "tipo": tipo,
            "cama": cama,
            "estado": estado,
            "historico": []
        }
        quartos.append(novo)
        print(f" Quarto {id_quarto} adicionado com sucesso!")
    except ValueError:
        print(" Entrada inválida. O ID tem de ser um número.")

def editar_estado_quarto():
    """Update: Permite atualizar o estado do quarto e registar o histórico de hóspedes."""
    listar_quartos()
    try:
        id_quarto = int(input("\nDigite o ID do quarto que quer atualizar: "))
        for q in quartos:
            if q['id'] == id_quarto:
                print(f"Estado atual: {q['estado']}")
                novo_estado = input("Novo estado (Disponível / Ocupado / Manutenção): ")
                q['estado'] = novo_estado
                
                # Se o quarto ficar ocupado, registamos o hóspede no histórico
                if novo_estado.lower() == "ocupado":
                    hospede = input("Nome do hóspede a registar no histórico: ")
                    q['historico'].append(hospede)
                    print(f" Hóspede '{hospede}' adicionado ao histórico do quarto {id_quarto}.")
                
                print(f" Estado do quarto {id_quarto} atualizado com sucesso!")
                return
        print(" Quarto não encontrado.")
    except ValueError:
        print(" Entrada inválida.")

def ver_historico_quarto():
    """Read (Histórico): Permite consultar quem esteve nos quartos."""
    print("\n--- Histórico de Ocupação dos Quartos ---")
    try:
        id_quarto = int(input("Digite o ID do quarto para ver o histórico: "))
        for q in quartos:
            if q['id'] == id_quarto:
                print(f"Histórico do Quarto {q['id']} ({q['tipo']}):")
                if not q['historico']:
                    print("  - Este quarto ainda não tem registo de hóspedes anteriores.")
                else:
                    for i, hospede in enumerate(q['historico'], 1):
                        print(f"  {i}. {hospede}")
                return
        print(" Quarto não encontrado.")
    except ValueError:
        print(" Entrada inválida.")

def remover_quarto():
    """Delete: Permite remover um quarto do inventário."""
    listar_quartos()
    try:
        id_quarto = int(input("\nDigite o ID do quarto que pretende eliminar: "))
        for q in quartos:
            if q['id'] == id_quarto:
                quartos.remove(q)
                print(f" Quarto {id_quarto} removido com sucesso!")
                return
        print(" Quarto não encontrado.")
    except ValueError:
        print(" Entrada inválida.")

def menu_quartos():
    while True:
        print("\n=== MENU GESTÃO DE QUARTOS (TP2) ===")
        print("1. Listar Quartos (Inventário & Detalhes)")
        print("2. Adicionar Novo Quarto (Create)")
        print("3. Editar Estado / Registar Hóspede (Update)")
        print("4. Ver Histórico de Hóspedes")
        print("5. Remover Quarto (Delete)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_quartos()
        elif opcao == "2":
            adicionar_quarto()
        elif opcao == "3":
            editar_estado_quarto()
        elif opcao == "4":
            ver_historico_quarto()
        elif opcao == "5":
            remover_quarto()
        elif opcao == "0":
            print("A sair do módulo de quartos...")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_quartos()