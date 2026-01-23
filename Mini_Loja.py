import os
import time
import random

PodeCorrer = False
Escolha_Casa = 0
Tentativas = 5
LucroCasino = 0
Wage = 0
Dinheiro = 10
Escolha_Rua = 0
Escolha_Trabalho = 0

EspacoArmario = 4  #Contagem para meter o Numero do item depois das linhas ja adicionadas
EspacoFrigorifico = 1 # o mesmo que o espacoarmario


Armario = [
    "=====[ARMÁRIO]============",
    "<0- Fechar armário<",
    "1- Calçãs Rasgadas - (Equipado)",
    "2- Camisola Descolorida - (Equipado)",
    "3- Sapatos 2 numeros a cima rotos - (Equipado)",
]


Casino = [
    "=====[CASINO]===========",
    "LUCRO:"+str(LucroCasino)+"$",
    "< 1 - Cara ou coroa (Facil)",
    "< 2 - Adivinha o numero (Intermedio)",
    "< 3 - Jogo do dado 50X (Dificil)",
    "< 4 - VER REGRAS",
    "< 0 - Sair do casino",
]


ComoJogar = [
    "=====[COMO JOGAR NO CASINO]======",
    "",
    "LUCRO = QUANTIDADE GANHADA OU PERDIDA",
    "WAGE = QUANTIDADE GASTADA EM APOSTAS",
    "",
    "==[CARA OU COROA]====",
    "Adivinhe se é cara ou coroa (1 ou 2) em 1 tentativa",
    "Dificuldade: Facil",
    "Recompensa: 1.50X da Aposta",
    "",
    "==[ADIVINHE O NUMERO]====",
    "Tente adivinhar o numero de 0 a 100 em 5 tentativas com ajuda",
    "Dificuldade: Médio",
    "Recompensa: 2X da Aposta",
    "",
    "==[JOGO DO DADO]====",
    "Adivinhar o numero do dado (1 a 6)",
    "Dificuldade: Extrema",
    "Recompensa: 50X da Aposta (JACKPOT)",
]


Casa = [
    "=====[CASA]===============",
    "Data de hoje: "+time.strftime("%d/%m/%Y"), #Vai mostrar o dia(d)day mes(m)onth) e ano(Y)year), se quiser meter horas e minutos é so adicionar %H:%M:%S
    "Você está em casa.",
    "Dinheiro:" + str(Dinheiro) + "$",
    "=====[Opções]==================",
    "< 1 - Ver Armário",
    "< 2 - Ver Frigorifico",
    "< 3 - Sair para a rua",
    "< 4 - Dormir",
    "==========================",
]


Frigorifico = [
    "====[FRIGORIFICO]=============",
    "<0 Retornar",
]


locais = [
    "=====[RUA]===============",
    "Dinheiro:" + str(Dinheiro) + "$",
    "< 1 - Loja de Roupa >",
    "< 2 - Trabalho >",
    "< 3 - Meu Super",
    "< 4 - Casino",
    "< 5 - Voltar para casa >",
    "=========================",
]


LojaRoupa = [
    "=====[LOJA DE ROUPA]=============",
    "<0 - Retornar>",
    "1 - Camiseta Básica Branca - 10$",
    "2 - Calça skinny - 10$",
    "3 - Tênis Desportivos - 5$",
    "4 - Casaco de Couro - 10$",
    "5 - Meias usadas - 67$",
    "6 - Oculos do bob esponja - 4$",
    "7 - Meias - 2$",
    "8 - Boxers - 5$",
    "9 - Chinelos - 5$",
    "10 - Calça Aranha Galáctica - 50$",
    "11 - Camisola Bob esponja dourado - 60$",
    "12 - Sapatos do tralalelo tralala - 70$",
    "=================================",
    "Dinheiro:" + str(Dinheiro) + "$",
]


Meu_Super = [
    "=========[MEU SUPER]============",
    "<0 - Voltar>",
    "1 - Bolachas Milka - 3$",
    "2 - Coca-Cola - 2$",
    "3 - Oreo - 3$",
    "4 - Pringles - 4$",
    "5 - (OFERTA_Especial) Pringles + Luvas + Esponjas - 20$",
    "6 - 1kg de Batatas - 1$",
    "7 - Cerveja - 1$",
    "8 - Choca Pic - 3$",
    "9 - Barra de Chocolate - 1$",
    "10 - Palete de leite - 20$",
    "======[OFERTA ESPECIAL]================",
    "12 - Batatas Podres - 0$",
    "13 - Maça com minhocas - 1$",
    "14 - Peru do natal de 2018 - 2$",
    "=================================",
    "Dinheiro:" + str(Dinheiro) + "$",
]


Trabalho = [
    "====[TRABALHO]=====",
    "< 1 - Trabalhar",
    "< 0 - Sair do trabalho",
    "===================="
]

# =============================== LOOP PRINCIPAL ===============================

while True:

    os.system('cls')

    for Linha in Casa:
        if "Dinheiro" in Linha:
            print("Dinheiro:"+str(Dinheiro)+"$")
        else:
            print(Linha)

    Escolha_Casa = input("O que você deve fazer?: ")


    # =============================== ARMÁRIO ===============================
    if Escolha_Casa == "1":

        PodeCorrer = True

        while PodeCorrer:

            os.system('cls')

            for Linha in Armario:
                print(Linha)

            Escolha_Armario = input("O que você quer fazer?: ")

            if Escolha_Armario.isnumeric():
                Escolha_Armario = int(Escolha_Armario)
                Escolha_Armario += 1
            else:
                print("Escolha uma opção válida.")
                Escolha_Armario = int(input("O que você quer fazer?: "))

            if Escolha_Armario == 1:
                break

            if Armario[Escolha_Armario]:

                if Armario[Escolha_Armario].endswith(" - (Equipado)"):
                    Armario[Escolha_Armario] = Armario[Escolha_Armario].replace(" - (Equipado)", "")
                else:
                    Armario[Escolha_Armario] = Armario[Escolha_Armario] + " - (Equipado)"

                PodeCorrer = True

    # =============================== Dormir ======================================
    if Escolha_Casa == "4":
        time.sleep(1)
        print("Indo dormir...")
        time.sleep(2)
        print("Você Adormeceu")
        time.sleep(3)
        break
    # =============================== FRIGORÍFICO =================================
    if Escolha_Casa == "2":
        os.system("cls")
        for Linha in Frigorifico:
            print(Linha)

        ALA = input("Digite algo para fechar frigorifico: ")
        PodeCorrer = False

    # =============================== RUA ===============================
    if Escolha_Casa == "3":

        PodeCorrer = False
        os.system("cls")

        for x in locais:
            if "Dinheiro" in x:
                print("Dinheiro: "+str(Dinheiro)+"$")
            else:
                print(x)

        Escolha_Rua = input("Onde devemos ir?: ")

        if Escolha_Rua.isnumeric():
            Escolha_Rua = int(Escolha_Rua)
        else:
            print("Inválido escreva novamente.")
            Escolha_Rua = int(input("Onde devemos ir?: "))
        # =============================== LOJA DE ROUPA ===============================
        if Escolha_Rua == 1:

            PodeCorrer = True

            while PodeCorrer:

                os.system('cls')

                for x in LojaRoupa:
                    if "Dinheiro" in x:
                        print("Dinheiro:"+str(Dinheiro)+"$")
                    else:
                        print(x)

                Desejo = input("Quer comprar oque?: ")
                Temp = ""

                if Desejo.isnumeric():
                    Desejo = int(Desejo)
                    Desejo += 1
                else:
                    print("Escreva um valor valido")
                    time.sleep(1)
                    break

                if Desejo == 1:
                    PodeCorrer = False
                else:
                    if Desejo > 13:
                        print("Valor invalido")
                        time.sleep(1)
                        break
                    Temp = LojaRoupa[Desejo]
                    Ulti = Temp[-3:-1]
                    Ulti = Ulti.strip()

                    if "Dinheiro" in Temp:
                        print("Nao esta no menu")
                        time.sleep(1)
                        break

                    if Ulti.isnumeric():
                        Ulti = int(Ulti)
                        Ulti += 1
                    else:
                        print("Nao esta no menu")
                        time.sleep(1)
                        break

                    if Dinheiro >= Ulti:
                        Temp = str(str(EspacoArmario) + Temp[2:])
                        Temp = Temp[:-4]
                        Temp = Temp.strip()
                        EspacoArmario += 1
                        Armario.append(Temp)
                        print("Item adicionado ao Armário")
                        Dinheiro -= Ulti
                        time.sleep(0.8)

                    else:
                        print("Voce nao tem dinheiro sufciente :(")
                        time.sleep(0.8)


        # Gambling
        if Escolha_Rua == 4:

            PodeCorrer = True

            while PodeCorrer:

                os.system('cls')

                for linha in Casino:
                    if "LUCRO" in linha:
                        print("LUCRO:" + str(LucroCasino) + "$")
                        print("WAGE:" + str(Wage) + "$")
                    else:
                        print(linha)

                EscolhaCasino = input("Quer apostar em qual?: ")

                if not EscolhaCasino.isnumeric():
                    print("Escreva um valor valido")
                    EscolhaCasino = int(input("Onde devemos ir?: "))
                    break

                # --- Cara ou Coroa ---
                if EscolhaCasino == "0":
                    os.system('cls')
                    break

                if EscolhaCasino == "1":

                    PodeCorrer = True

                    while PodeCorrer:
                        os.system("cls")
                        print("====[CARA OU COROA]====")
                        print("(1) = CARA (2) = COROA")
                        print("=======================")
                        print("Escreva 0 para voltar")

                        Quantidade = input("Quer apostar quanto dinheiro?: ")

                        if Quantidade.isnumeric():
                            Quantidade = int(Quantidade)
                        else:
                            print("Escreva um valor valido")
                            time.sleep(1)
                            print("Voce tem: "+str(Dinheiro) + "$")
                            Quantidade = int(input("Quer apostar quanto?: "))
                            break

                        if Quantidade == 0:
                            break

                        if Quantidade <= Dinheiro:

                            Wage = Wage + Quantidade
                            os.system('cls')

                            print("====[CARA OU COROA]====")
                            print("(1) = CARA (2) = COROA")
                            print("=======================")
                            print("DINHEIRO APOSTADO: " + str(Quantidade) + "$")

                            NCerto = random.randint(1, 2)
                            Adivinha = input("Vai apostar em qual?: ")

                            if Adivinha.isnumeric():

                                # --- CARA ---
                                if Adivinha == "1":

                                    time.sleep(0.5)
                                    os.system("cls")
                                    print("APOSTA: CARA")
                                    print("A moeda esta no ar....")
                                    time.sleep(2)

                                    if NCerto == 1:

                                        print("CARA ESTA VIRADA PARA CIMA")
                                        time.sleep(1)
                                        os.system("cls")

                                        print("Você ganhou!!!!")
                                        print("O dinheiro de " + str(Quantidade) + "$")

                                        ganho = Quantidade + Quantidade / 2

                                        print("Para " + str(ganho) + "$")

                                        LucroCasino += (ganho - Quantidade)
                                        Dinheiro += (ganho - Quantidade)

                                        time.sleep(4)

                                    else:

                                        print("COROA ESTA VIRADA PARA CIMA")
                                        time.sleep(1)

                                        print("Você perdeu")
                                        print("O dinheiro de " + str(Quantidade) + "$")

                                        Dinheiro -= Quantidade
                                        LucroCasino -= Quantidade

                                        print("Para 0$")

                                        time.sleep(4)
                                        break

                                # coroa
                                elif Adivinha == "2":

                                    time.sleep(0.5)
                                    os.system("cls")

                                    print("APOSTA: COROA")
                                    print("A moeda esta no ar....")
                                    time.sleep(2)

                                    if NCerto == 2:

                                        print("COROA ESTA VIRADA PARA CIMA")
                                        time.sleep(1)

                                        os.system("cls")

                                        print("Você ganhou!!!!")
                                        print("O dinheiro de " + str(Quantidade) + "$")

                                        ganho = Quantidade + Quantidade / 2

                                        print("Para " + str(ganho) + "$")

                                        LucroCasino += (ganho - Quantidade)
                                        Dinheiro += (ganho - Quantidade)

                                        time.sleep(4)

                                    else:

                                        print("CARA ESTA VIRADA PARA CIMA")
                                        time.sleep(1)

                                        print("Você perdeu")
                                        print("O dinheiro de " + str(Quantidade) + "$")

                                        Dinheiro -= Quantidade
                                        LucroCasino += Quantidade

                                        print("Para 0$")
                                        time.sleep(4)
                                        break

                                else:
                                    print("Valor invalido")
                                    time.sleep(1)
                                    break

                            else:
                                print("Valor inválido")
                                time.sleep(1)

                        else:
                            print("Nao pode apostar essa quantidade")
                            time.sleep(1)
                            break

                # jOgo adivinha
                if EscolhaCasino == "2":

                    PodeCorrer = True

                    while PodeCorrer:

                        os.system("cls")

                        print("===[ADIVINHE O NUMERO]=======")
                        print("1- Jogar (0-100)")
                        print("0- Voltar")
                        print("============================")
                        time.sleep(0.5)

                        EscolhaAdivinha = input("O que você deve fazer?: ")

                        if EscolhaAdivinha.isnumeric():
                            EscolhaAdivinha = int(EscolhaAdivinha)
                        else:
                            print("Valor invalido")
                            time.sleep(1)
                            break

                        if EscolhaAdivinha == 0:
                            PodeCorrer = False

                        if EscolhaAdivinha == 1:

                            print("Voce tem: "+str(Dinheiro) + "$")

                            Aposta = input("Quanto dinheiro vai apostar?")

                            if Aposta.isnumeric():

                                Aposta = int(Aposta)

                                if Dinheiro < Aposta:
                                    print("Nao podes apostar essa quantidade")
                                    time.sleep(1)
                                    break

                                else:
                                    print("Dinheiro em linha: " + str(Aposta)+"$")
                                    NCerto = random.randint(0, 100)
                                    time.sleep(1)

                            else:
                                print("Valor invalido")
                                time.sleep(1)
                                break

                            PodeCorrer = True

                            while PodeCorrer:

                                os.system("cls")

                                print("===[JOGO ADIVINHA]=======")
                                print("Digite 'Menu' para perder e voltar")
                                print("Adivinhe o numero de 0 a 100")

                                AdivinhaJ = input("Qual a sua adivinha?: ")

                                if AdivinhaJ.isnumeric():

                                    AdivinhaJ = int(AdivinhaJ)

                                else:

                                    print("Você perdeu automaticamente.")
                                    time.sleep(1)

                                    Tentativas = 6
                                    Dinheiro = Dinheiro - Aposta
                                    LucroCasino -= Aposta
                                    Wage += Aposta

                                    break

                                if AdivinhaJ == NCerto:

                                    print("Você acertou!")
                                    NCerto = random.randint(0, 100)

                                    print("O dinheiro de " + str(Aposta) + "$")
                                    Dinheiro = Dinheiro + Dinheiro

                                    Wage += Aposta
                                    LucroCasino += Aposta

                                    Tentativas = 5
                                    Aposta = Aposta + Aposta

                                    print("Para " + str(Aposta) + "$")
                                    time.sleep(4)

                                    break

                                else:

                                    if Tentativas == 0:

                                        print("Ficou sem tentativas")
                                        print("Voce perdeu "+str(Aposta) + "$")

                                        Dinheiro = Dinheiro - Aposta
                                        LucroCasino -= Aposta
                                        Tentativas = 6

                                        Wage += Aposta

                                        time.sleep(2)

                                        break

                                    Distancia = abs(AdivinhaJ - NCerto)

                                    if AdivinhaJ > NCerto:
                                        print("O Numero é MENOR que ", AdivinhaJ)
                                    else:
                                        print("O Numero é MAIOR que ", AdivinhaJ)

                                    if Distancia <= 3:
                                        print("MUITO PERTO")
                                    elif Distancia <= 10:
                                        print("Muito perto")
                                    elif Distancia <= 15:
                                        print("Bastante Perto")
                                    elif Distancia <= 25:
                                        print("Perto")
                                    elif Distancia <= 40:
                                        print("Menos longe")
                                    else:
                                        print("Longe")

                                    print("Tentativas Restantes: " + str(Tentativas))

                                    Tentativas = Tentativas - 1

                                    time.sleep(2)


                # Jogo do Dado
                if EscolhaCasino == "3":
                    os.system("cls")
                    print("====[JOGO DO DADO]=========")
                    print("1- Jogar (1-6)")
                    print("0- Voltar")
                    print("===========================")

                    AHA = input("Qual a sua escolha?: ")

                    if AHA.isnumeric():
                        AHA = int(AHA)
                    else:
                        AHA = int(input("Valor invalido escreva denovo: "))

                    if AHA == 1:

                        NUCERTO = random.randint(1, 6)

                        print("Voce tem: " + str(Dinheiro) + "$")
                        ApostaD = input("Quanto dinheiro quer apostar?: ")

                        if ApostaD.isnumeric():
                            ApostaD = int(ApostaD)
                        else:
                            break

                        if Dinheiro < ApostaD:
                            print("Quantidade invalida")
                            time.sleep(1)
                            break

                        PodeCorrer = True

                        while PodeCorrer:

                            os.system("cls")

                            print("====[JOGO DO DADO]==================")
                            print("Adivinhe que numero vai calhar (1 a 6)")
                            print("=====================================")

                            adivinhap = input("Qual a sua adivinha?: ")

                            if adivinhap.isnumeric():
                                adivinhap = int(adivinhap)
                            else:
                                adivinhap = int(input("Inválido, escreva denovo: "))

                            print("O Dado está a ser lançado...")
                            time.sleep(1)

                            if adivinhap == NUCERTO:

                                os.system("cls")
                                print("JACKPOTT!!!!!!")
                                time.sleep(1)
                                print(".")
                                time.sleep(0.1)
                                print("..")
                                time.sleep(0.1)
                                print("...")
                                time.sleep(0.1)
                                print("....")
                                time.sleep(0.1)
                                print(".....")
                                time.sleep(0.1)
                                print(".......")
                                time.sleep(0.1)
                                print("........")
                                time.sleep(0.1)
                                print("..........")
                                time.sleep(0.1)

                                print("O DINHEIRO PASSOU DE "+str(ApostaD) + "$")

                                Wage += ApostaD
                                ApostaD = ApostaD * 50

                                print("PARA "+ str(ApostaD) + "$")

                                Dinheiro += ApostaD
                                LucroCasino += ApostaD

                                time.sleep(4)
                                break

                            else:

                                print("Errou.")
                                NUCERTO = random.randint(1, 6)
                                print("Gerando novo numero...")

                                Wage += ApostaD
                                Dinheiro -= ApostaD
                                LucroCasino -= ApostaD

                                time.sleep(3)
                                break

                    else:
                        print("Retornando")
                        os.system("cls")

                # --- Ver Regras ---
                if EscolhaCasino == "4":

                    os.system("cls")

                    for x in ComoJogar:
                        print(x)

                    input("Pressione ENTER para sair...")


        # =============================== MEU SUPER ===============================
        if Escolha_Rua == 3:

            PodeCorrer = True

            while PodeCorrer:

                os.system('cls')

                for x in Meu_Super:
                    if "Dinheiro" in x:
                        print("Dinheiro:" + str(Dinheiro) + "$")
                    else:
                        print(x)

                ItemDesejado = input("O que deseja comprar?: ")
                Temporario = ""

                if ItemDesejado.isnumeric():

                    ItemDesejado = int(ItemDesejado)
                    ItemDesejado += 1

                else:
                    print("Escreva um digito valido")
                    ItemDesejado = int(input("O que deseja comprar?: "))

                if ItemDesejado == 1:
                    PodeCorrer = False

                else:

                    Temporario = Meu_Super[ItemDesejado]

                    Ultimo = Temporario[-3:-1]
                    Ultimo = Ultimo.strip()

                    if "Dinheiro" in Temporario:
                        print("Nao está no menu")
                        time.sleep(1)
                        break

                    if Ultimo.isnumeric():
                        Ultimo = int(Ultimo)
                    else:
                        print("Nao está no menu")
                        time.sleep(1)
                        break

                    if Dinheiro >= Ultimo:

                        Temporario = str(str(EspacoFrigorifico) + Temporario[2:])
                        Temporario = Temporario[:-4]
                        Temporario = Temporario.strip()

                        EspacoFrigorifico += 1
                        Frigorifico.append(Temporario)

                        print("Item adicionado ao frigorifico")

                        Dinheiro -= Ultimo
                        time.sleep(0.8)

                    else:
                        print("Voce nao tem dinheiro sufciente :(")
                        time.sleep(0.8)


        # =============================== TRABALHO ===============================
        if Escolha_Rua == 2:

            os.system("cls")

            for Linha in Trabalho:
                print(Linha)

            Escolha_Trabalho = input("O que deves fazer?: ")

            if Escolha_Trabalho.isnumeric():
                Escolha_Trabalho = int(Escolha_Trabalho)
            else:
                print("Inválido escreva novamente.")
                Escolha_Trabalho = int(input("O que deves fazer?: "))

            if Escolha_Trabalho == 1:

                PodeCorrer = True

                while PodeCorrer:

                    os.system("cls")

                    print("===TRABALHO DE REAÇÃO===")
                    print("Quando aparecer VAI!, clique no ENTER o mais rápido possível!")

                    time.sleep(1)
                    input("Preparado? Enter para continuar...")

                    time.sleep(random.uniform(2, 4))

                    print("VAI!")

                    inicio = time.time()
                    input()
                    fim = time.time()

                    tempo = fim - inicio

                    print("Sua reação: " + str(round(tempo, 3)) + " segundos")

                    if tempo < 0.30:
                        print("EXCELENTE! +20$")
                        Dinheiro += 20

                    elif tempo < 0.50:
                        print("Bom! +10$")
                        Dinheiro += 10

                    elif tempo < 1:
                        print("És uma lesma... +1$")
                        Dinheiro += 1

                    else:
                        print("Que tempo de reação é esse? +0$")

                    time.sleep(1)

                    TEM = input("Enter para continuar ou 0 para sair: ")

                    if TEM == "0":
                        PodeCorrer = False
                    else:
                        PodeCorrer = True