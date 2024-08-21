from funcoes2 import adicionar_medicamento, remover_medicamento, buscar_medicamento, listar_estoque, vender_medicamento

def menu():
    print('''\n=== Menu da Farmácia ===
          
    1. Adicionar Medicamento
    2. Remover Medicamento
    3. Buscar Medicamento
    4. Listar Estoque
    5. Vender Medicamento
    6. Sair  ''')

def main():
    estoque = {}
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do medicamento: ")
            quantidade = int(input("Quantidade: "))
            print(adicionar_medicamento(estoque, nome, quantidade))
        
        elif opcao == "2":
            nome = input("Nome do medicamento: ")
            quantidade = int(input("Quantidade: "))
            print(remover_medicamento(estoque, nome, quantidade))
        
        elif opcao == "3":
            nome = input("Nome do medicamento: ")
            print(buscar_medicamento(estoque, nome))
        
        elif opcao == "4":
            print(listar_estoque(estoque))
        
        elif opcao == "5":
            nome = input("Nome do medicamento: ")
            quantidade = int(input("Quantidade: "))
            print(vender_medicamento(estoque, nome, quantidade))
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
