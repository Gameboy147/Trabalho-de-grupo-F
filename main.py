# --- Módulo de Gestão de Quartos ---
# User Stories: Inventário, Estado/Tipo/Cama, Edição de Estado e Histórico

# Exemplo de estrutura de dados inicial (lista de dicionários para representar os quartos)
quartos = [
    {"id": 101, "tipo": "Casal", "cama": "King Size", "estado": "Disponível", "historico": []},
    {"id": 102, "tipo": "Twin", "cama": "Duas Individual", "estado": "Ocupado", "historico": ["Ana Silva"]},
    {"id": 103, "tipo": "Suite", "cama": "Queen Size", "estado": "Manutenção", "historico": []}
]

def listar_quartos():
    """Permite ao funcionário visualizar todos os quartos e o seu inventário."""
    print("\n--- Inventário de Quartos ---")
    for q in quartos:
        print(f"Quarto {q['id']} | Tipo: {q['tipo']} | Cama: {q['cama']} | Estado: {q['estado']}")

def editar_estado_quarto():
    """Permite ao funcionário atualizar o estado de um quarto."""
    listar_quartos()
    try:
        id_quarto = int(input("\nDigite o ID do quarto que quer atualizar: "))
        for q in quartos:
            if q['id'] == id_quarto:
                novo_estado = input(f"Novo estado para o quarto {id_quarto} (Disponível/Ocupado/Manutenção): ")
                q['estado'] = novo_estado
                print(f" Estado do quarto {id_quarto} atualizado com sucesso!")
                return
        print(" Quarto não encontrado.")
    except ValueError:
        print(" Entrada inválida. Introduza um número de ID válido.")

def menu_quartos():
    while True:
        print("\n=== MENU QUARTOS (TP2) ===")
        print("1. Listar Quartos (Inventário & Detalhes)")
        print("2. Editar Estado do Quarto")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_quartos()
        elif opcao == "2":
            editar_estado_quarto()
        elif opcao == "0":
            print("A sair do módulo de quartos...")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_quartos()