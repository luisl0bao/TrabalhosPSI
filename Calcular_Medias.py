import os
registro = 0 #Vai ser usado para calcular o numero de notas registadas
media = 0
nota = None #Nota inserida
notas = 0 #valor de todas as notas registadas
devecontinuar = True
Abc = 1
turma = []

#Funçôes
def e_float(x): #vai verificar se é numero float
    try:
        float(x)
        return True
    except ValueError:
        return False
######
def calcularmedia(nots,reg): #Nots = Notas | reg = registo |
    global media
    global notas
    global nota
    global registro
    global Abc
    global devecontinuar
    if nots == 0 and reg == 0:
        print("Nenhum valor inserido")
        nota = 0
        pedirnota()
        return
    media = nots/reg
    media = round(media,1)
    turma.append(media)
    turma[Abc-1] = "O aluno Nº"+str(Abc)+" Teve: "+str(media)
    Abc = Abc+1
    print("Media do aluno: ", media)
    print("Quer registar notas para outro aluno?")
    a = input("s/n | ")
    if a == "s" or a == "S":
        nota = None
        notas = 0
        registro = 0
        pedirnota()
    elif a == "n":
        nota = None
        notas = 0
        registro = 0
        for lin in turma:
            print(lin)
        input("Pressione <enter> para sair")
        devecontinuar = False
        os.system('exit')
        return
    else:
        os.system("exit")
        devecontinuar = False
######
def pedirnota():
    global registro
    global media
    global nota
    global notas
    print("Qual é a nota do aluno?")
    print("Escreva 'calcular' para ver média")
    nota = input("Nota: ")

    if nota == "calcular":
        print("Calculando")
        calcularmedia(notas,registro)

    if e_float(nota): #Vai retornar verdadeiro ou falso para evitar erros caso estreva uma string ao inves de float ou int
        nota = float(nota)
        if nota>100:
            print("Nota maior que 100, introduza numero valido")
            pedirnota()
        nota = round(nota,2)
        registro += 1
        notas = notas + nota
        print("Nota registada")
        pedirnota()
    else:
        print("Nota invalida")
        pedirnota()

#programa
if devecontinuar:
    pedirnota()