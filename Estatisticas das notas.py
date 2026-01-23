notas = []
while True:
    quantidade = input("Digite quantas notas quer anotar: ")
    if quantidade.isnumeric():
        quantidade = int(quantidade)
    else:
        while not quantidade.isnumeric():
            quantidade = input("Escreva um numero inteiro, quantidade de notas?: ")
        quantidade = int(quantidade)
    for n in range(quantidade):
        nota = input("Digite a "+str(n+1)+"º nota: ")
        while not nota.isnumeric():
            nota = input("Escreva um numero,digite a "+str(n+1)+"º nota: ")
        nota = float(nota)
        notas.append(nota)
    print("A média das",str(quantidade),"notas listadas foi:",round(sum(notas)/len(notas),2))
    notas.sort()
    print("Nota mais baixa:",min(notas))
    print("Nota mais alta:",max(notas))
    res = input("Deseja continuar? [´N/n´ para encerrar] ")
    if res == "n" or res == "N":
        break
    else:
        print("Não escreveu N, cotinuando...")
        continue