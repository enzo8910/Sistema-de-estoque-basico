def buscar_produto_por_nome(estoque, nome):

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

def buscar_produto_por_id(estoque, id):

    for produto in estoque:
        if produto["id"] == id:
            return produto
    return None

def gerar_id_produto(estoque):
    if len(estoque) == 0:
        return 1

    maior_id = 0

    for produto in estoque:
        if produto["id"] > maior_id:
            maior_id = produto["id"]

    return maior_id + 1

def adicionar_produto(estoque):
    id = input("Digite o ID do produto (deixe em branco para gerar automaticamente): ").strip()
    if id != "":
        try:
            id = int(id)
            if any(produto["id"] == id for produto in estoque):
                print("ID já existe. Produto não adicionado.")
                return
        except ValueError:
            print("ID inválido. Produto não adicionado.")
            return

    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print("O nome do produto não pode ser vazio. Produto não adicionado.")
        return
    
    produto_existente = buscar_produto_por_nome(estoque, nome)
    if produto_existente is not None:
        print("Produto já cadastrado. Produto não adicionado.")
        print("use a opção de atualizar a quantidade para modificar o estoque do produto existente.")
        return

    quantidade = pedir_inteiro("Digite a quantidade do produto: ")
    preco = pedir_float("Digite o preço do produto: ")

    produto = {
        "id": gerar_id_produto(estoque),
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def buscar_produto(estoque):
    id = input("Digite o ID do produto que deseja buscar: ").strip()
    if id != "":
        try:
            id = int(id)
            produto = buscar_produto_por_id(estoque, id)
        except ValueError:
            print("ID inválido. Buscando por nome...")
            produto = None
    else:
        nome = input("Digite o nome do produto que deseja buscar: ").strip()
        produto = buscar_produto_por_nome(estoque, nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("\n=== PRODUTO ENCONTRADO ===")
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R${produto['preco']:.2f}")

def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("Produtos em estoque:")
    for idx, produto in enumerate(estoque, start=1):
        print(f"{idx}. ID: {produto['id']} | Nome: {produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']:.2f}")

def remover_produto(estoque):
    listar_produtos(estoque)
    if not estoque:
        return
    id = input("Digite o ID do produto que deseja remover: ").strip()
    if id != "":
        try:
            id = int(id)
            produto = next((p for p in estoque if p["id"] == id), None)
        except ValueError:
            print("ID inválido.")
            return
    else:
        nome = input("Digite o nome do produto que deseja remover: ")
        produto = buscar_produto_por_nome(estoque, nome)

    if produto is None:
        print("Produto não encontrado. Nenhum produto removido.")
        return

    estoque.remove(produto)
    print(f"Produto '{produto['nome']}' removido com sucesso!")

def atualizar_quantidade(estoque):
    id = input("Digite o ID do produto que deseja atualizar a quantidade: ").strip()
    if id != "":
        try:
            id = int(id)
            produto = next((p for p in estoque if p["id"] == id), None)
        except ValueError:
            print("ID inválido. Buscando por nome...")
            produto = None
    else:
        nome = input("Digite o nome do produto que deseja atualizar a quantidade: ").strip()
        produto = buscar_produto_por_nome(estoque, nome)

    if produto is None:
        print("Produto não encontrado. Nenhuma quantidade atualizada.")
        return

    nova_quantidade = pedir_inteiro(f"Digite a nova quantidade para '{produto['nome']}': ")
    produto['quantidade'] = nova_quantidade
    print(f"Quantidade do produto '{produto['nome']}' atualizada para {nova_quantidade}.")

def verificar_estoque_baixo(estoque, limite=5):
    print("Produtos com estoque baixo:")
    for produto in estoque:
        if produto['quantidade'] < limite:
            print(f"{produto['nome']} - Quantidade: {produto['quantidade']}")
        
def pedir_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def pedir_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número decimal.")

def calcular_valor_total_estoque(estoque):

    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0

    print("\n=== VALOR TOTAL POR PRODUTO ===")

    for produto in estoque:
        total_produto = produto["quantidade"] * produto["preco"]
        valor_total += total_produto

        print(f"{produto['nome']} | Quantidade: {produto['quantidade']} | "
              f"Preço: R${produto['preco']:.2f} | Total: R${total_produto:.2f}")

    print(f"\nValor total em estoque: R${valor_total:.2f}")

    if len(estoque) == 0:
        return 1

    maior_id = 0

    for produto in estoque:
        if produto["id"] > maior_id:
            maior_id = produto["id"]

    return maior_id + 1

def editar_produto(estoque):

    listar_produtos(estoque)
    if len(estoque) == 0:
        return

    id = pedir_inteiro("Digite o ID do produto que deseja editar: ")

    produto = buscar_produto_por_id(estoque, id)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("\n=== EDITAR PRODUTO ===")
    print("1. Editar nome")
    print("2. Editar quantidade")
    print("3. Editar preço")
    print("4. Editar tudo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Novo nome: ").strip()

        if novo_nome == "":
            print("O nome não pode ficar vazio.")
            return

        produto["nome"] = novo_nome
        print("Nome atualizado com sucesso!")

    elif opcao == "2":
        nova_quantidade = pedir_inteiro("Nova quantidade: ")
        produto["quantidade"] = nova_quantidade
        print("Quantidade atualizada com sucesso!")

    elif opcao == "3":
        novo_preco = pedir_float("Novo preço: ")
        produto["preco"] = novo_preco
        print("Preço atualizado com sucesso!")

    elif opcao == "4":
        novo_nome = input("Novo nome: ").strip()

        if novo_nome == "":
            print("O nome não pode ficar vazio.")
            return

        nova_quantidade = pedir_inteiro("Nova quantidade: ")
        novo_preco = pedir_float("Novo preço: ")

        produto["nome"] = novo_nome
        produto["quantidade"] = nova_quantidade
        produto["preco"] = novo_preco

        print("Produto atualizado com sucesso!")

    else:
        print("Opção inválida.")

def relatorio_geral_do_estoque(estoque):
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(estoque)
    quantidade_total_itens = 0
    valor_total_estoque = 0
    produtos_estoque_baixo = 0
    limite_estoque_baixo = 5

    produto_maior_valor = estoque[0]
    produto_menor_quantidade = estoque[0]

    for produto in estoque:
        quantidade = produto["quantidade"]
        preco = produto["preco"]
        valor_total_produto = quantidade * preco

        quantidade_total_itens += quantidade
        valor_total_estoque += valor_total_produto

        if quantidade <= limite_estoque_baixo:
            produtos_estoque_baixo += 1

        if valor_total_produto > produto_maior_valor["quantidade"] * produto_maior_valor["preco"]:
            produto_maior_valor = produto

        if quantidade < produto_menor_quantidade["quantidade"]:
            produto_menor_quantidade = produto

    print("\n=== RELATÓRIO GERAL DO ESTOQUE ===")
    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Quantidade total de itens: {quantidade_total_itens}")
    print(f"Valor total em estoque: R${valor_total_estoque:.2f}")
    print(f"Produtos com estoque baixo: {produtos_estoque_baixo}")

    print("\n=== DESTAQUES ===")
    print(
        f"Produto com maior valor em estoque: {produto_maior_valor['nome']} "
        f"| Total: R${produto_maior_valor['quantidade'] * produto_maior_valor['preco']:.2f}"
    )

    print(
        f"Produto com menor quantidade: {produto_menor_quantidade['nome']} "
        f"| Quantidade: {produto_menor_quantidade['quantidade']}"
    )