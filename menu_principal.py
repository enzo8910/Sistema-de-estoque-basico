from funcoes.arquivo import carregar_estoque, salvar_estoque
from funcoes.produtos import adicionar_produto, atualizar_quantidade, listar_produtos, remover_produto, verificar_estoque_baixo, buscar_produto, calcular_valor_total_estoque, editar_produto, relatorio_geral_do_estoque

def mostrar_menu():
    estoque = carregar_estoque()

    while True:
        print("\nMenu Principal")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Atualizar Quantidade")
        print("5. Verificar Estoque Baixo")
        print("6. Buscar Produto")
        print("7. Calcular Valor Total do Estoque")
        print("8. Editar Produto")
        print("9. Relatório Geral do Estoque")
        print("10. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto(estoque)
            salvar_estoque(estoque)
        elif opcao == '2':
            listar_produtos(estoque)
        elif opcao == '3':
            remover_produto(estoque)
            salvar_estoque(estoque)
        elif opcao == '4':
            atualizar_quantidade(estoque)
            salvar_estoque(estoque)
        elif opcao == '5':
            verificar_estoque_baixo(estoque)
        elif opcao == '6':
            buscar_produto(estoque)
        elif opcao == '7':
            calcular_valor_total_estoque(estoque)
        elif opcao == '8':
            editar_produto(estoque)
            salvar_estoque(estoque)
        elif opcao == '9':
            relatorio_geral_do_estoque(estoque)
        elif opcao == '10':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
            

