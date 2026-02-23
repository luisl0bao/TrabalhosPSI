def auchanmenu():
    print("======[Auchan]======")
    print("Opções".center(18))
    print("[1] Ver produtos")
    print("[2] Adicionar produto")
    print("[3] Remover produto")
    print("[4] Procurar produto")
    print("[0] Sair")
    print("==================")


def adicionar_produto(produtos):
    id = input("Digite seu id do produto: ")
    if not id.isdigit:
        print("Escreva um numero")
        return
    for artigo in produtos:
        if artigo[0] == id:
            print("Esse ID ja esta registado.")
            input("Enter para continuar")
            adicionar_produto(produtos)
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto (ex:1.25): "))
    produto = (id, nome, preco)
    produtos.append(produto)
    print("Produto adicionado")
    input("Pressione <enter> para continuar")


def procurar_produto(produtos):
    encontrado = False
    if input("quer ver lista de produtos? S/N: ").lower() == "s":
        for produto in produtos:
            print(produto)
    pesquisa = input("Digite nome ou id do produto: ")
    print("<Produtos encontrados>")
    for i, produto in enumerate(produtos):
       if pesquisa in produto[1] or pesquisa in produto[0]:
           encontrado = True
           print("ID: "+str(i+1),"|",produto[1],"|",str(produto[2])+"$")
    if not encontrado:
        print("Nao foi encontrado nenhum produto")
    input("<Enter para continuar>")


def listar_produtos(produtos):
    produtos.sort()
    for produto in produtos:
        print("ID: "+str(produto[0])+" -",produto[1]," | Preço: " + str(produto[2]))
    input("<Enter para continuar>")


def remover_produto(produtos):
    print("===[lista de ids]===")
    for produto in produtos:
        print("ID: "+str(produto[0])+" -",produto[1],"Preço: "+str(produto[2]))
    print("=====================")
    procura = int(input("Digite o id do produto: "))
    while procura == "":
        procura = int(input("Digite um id valido: "))

