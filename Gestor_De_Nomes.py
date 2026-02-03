import time
import os

os.system('color 80')
##########
nomes = []
lista_negra = []
##########
def adicionar_nome():
    os.system('cls')
    time.sleep(0.2)
    print("============[ADICIONAR NOME]==============")
    nome = input("Digite um nome para adicionar: ")
    nome = nome[0].upper()+nome[1:]
    if len(nome) <= 3:
        print("Nome muito curto")
        nome = ""
    if any(not char.isalpha() for char in nome if char != " "): #Verificar se nao tem simbolos e ignorar espaço
        #isalpha vai verificar se é numeros alfabeticos, not isalpha vai passar a verificar se sao tudo menos alfabetos
        print("Eu pedi um nome não uma equação matematicas")
        nome = ""
    elif len(nome) > 3:
        nomes.append(nome)
        print(nome,"foi adicionado na lista!")
    input("Enter para continuar...")

def remover_nome():
    os.system('cls')
    time.sleep(0.2)
    print("=========[REMOVER NOME]============")
    nome = input("Digite o nome para remover: ").strip().title()
    # nome = nome[0].upper()+nome[1:]
    if nome in nomes:
        nomes.remove(nome)
        print(nome,"foi EXCLUIDO!")
    else:
        print("Nome não esta na lista")
    input("Pressione <enter> para continuar...")

def pesquisar_nome():
    os.system('cls')  # ou 'clear' se for Linux/Mac
    time.sleep(0.2)
    print("=========[PESQUISAR NOME]============")
    nome = input("Digite o nome para pesquisar: ").strip().split()[0]  # primeira palavra sem espaços
    nome = nome[0].upper()+nome[1:]
    temporario = []
    quantidade = 0
    for nom in nomes:  # nomes é a lista que você deve ter definido
        if nome in nom:
            temporario.append(nom)
            quantidade += 1

    if quantidade > 0:
        for encontrado in temporario:
            print(encontrado)
        print(quantidade,"pessoas com '"+nome+"' no nome foram encontradas")
    else:
        print("Nome não encontrado.")

    input("Pressione <enter> para continuar...")

def lista_negra_remover():
    os.system('cls')
    time.sleep(0.2)
    print("==========[LISTA NEGRA]===========")
    print("Quer ver os nomes na lista negra?")
    resposta = input("S/N : ").lower()
    if resposta == "s":
        contador = 1
        print("=================")
        for nme in lista_negra:
            print(str(contador),"-",nme)
    print("=============================")
    nomepr = input("Nome para remover: ")
    if nomepr in lista_negra:
        lista_negra.remove(nomepr)
        print("Nome removido")
    else:
        print("Nome não encontrado.")
    input("Pressione <enter> para continuar...")
def lista_negra_adicionar():
    os.system('cls')
    time.sleep(0.1)
    print("==========[ADICIONAR À LISTA NEGRA]===========")
    nome_negro = input("Diga um nome para adicionar a lista negra: ")
    if any(char.isalpha() for char in nome_negro if char != " "):
        print("Nome adicionado em lista negra")
        lista_negra.append(nome_negro)
    else:
        print("Nome não esta na lista")
        time.sleep(1)
        lista_negra_adicionar()
    input("Pressione <enter> para continuar...")

def ver_lista():
    os.system('cls')
    time.sleep(0.1)
    if nomes:
        print("======[LISTA DE NOMES]======")
        for nome in nomes:
            print(str(len(nomes))+" -",nome)
    else:
        print("A lista está vazia.")
    input("Pressione <enter> para continuar...")

def total_pessoas():
    os.system('cls')
    print("Total de pessoas cadastradas: "+str(len(nomes)))
    input("Pressione <enter> para continuar...")

while True:
    time.sleep(0.5)
    os.system('cls')
    print("=========[Gestor de Nomes]========")
    print("1 - Adicionar nome")
    print("2 - Remover nome")
    print("3 - Pesquisar nome")
    print("4 - Ver lista de nomes")
    print("5 - Ver total de pessoas")
    print("6 - Adicionar nome em lista negra")
    print("7 - Ver lista negra")
    print("8 - Remover da lista negra")
    print("0 - Sair")
    print("==================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_nome()
    elif opcao == "2":
        remover_nome()
    elif opcao == "3":
        pesquisar_nome()
    elif opcao == "4":
        ver_lista()
    elif opcao == "5":
        total_pessoas()
    elif opcao == "6":
        lista_negra_adicionar()
    elif opcao == "7":
        print("=====[LISTA NEGRA]========")
        for nome in lista_negra:
            print(nome)
        print("=========================")
        input("Pressione <enter> para continuar...")
    elif opcao == "8":
        lista_negra_remover()
    elif opcao == "0":
        print("Saindo.")
        break
    else:
        print("Opção inválida. Tente novamente.")
