from scripts import funcoes
produtos = [
('1', 'Maças Vermelhas', 0.27),
('2', 'Bananas da madeira', 4.20),
('3', 'Amendoins', 2.00),
('4', 'Micro-Ondas', 37.10),
('5', 'Televisão', 120.00),
('6', 'Auriculares', 37.00),
]
def main():
    while True:
        funcoes.auchanmenu()
        escolha = input("Escolha: ")
        if escolha not in ["0","1","2","3","4"]:
            print("Escolha não encontrada")
            input("<Enter para continuar>")
        elif escolha == "1":
            funcoes.listar_produtos(produtos)
        elif escolha == "2":
            funcoes.adicionar_produto(produtos)
        elif escolha == "3":
            funcoes.remover_produto(produtos)
        elif escolha == "4":
            funcoes.procurar_produto(produtos)
        elif escolha == "0":
            break
if __name__ == "__main__":
    main()