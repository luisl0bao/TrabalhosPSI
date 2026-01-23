import os
import random
import time
PodiCorrer = False
Pontos = 0
Selecao = 0
RetornarMenu = False
Tentativas = 10
NumeroInteiroCorreto = random.randint(0, 100)
N_Correto = str(NumeroInteiroCorreto)
NumeroCorretoHard = random.randint(0, 1000)
N_Hard = str(NumeroCorretoHard)
Skins = [
    "1: Skin Oceano - 3 Pontos",
    "2: Skin Fogo - 5 Pontos",
    "3: Skin Default"
    "0 - Retornar",
]
Lista = ["[Bem vindo ao Jogo da adivinha do Luis]",
         "",
         "==============[Menu]================",
         "-----------------------------------------------",
         "> 1- Jogar Normal(0-100) ",
         "> 2- Pontuação",
         "> 3- Como Jogar",
         "> 4- Modo Hardcore(0-1000) ",
         "> 5- Skins ",
         "< 0- Sair",
         "-----------------------------------------------",
         ]

for Opcao in Lista:
    print(Opcao)

Escolha = input("Escolha uma opção: ")

while Escolha != "0":
    if RetornarMenu:
        for Opcao in Lista:
            print(Opcao)
        Escolha = input("Escolha uma opção: ")
        RetornarMenu = False

    if Escolha == "1":
        RetornarMenu = True
        if RetornarMenu:
            Lista = ["======[Menu]======",
                     "--------------------------------",
                     " 1- Continuar Jogando",
                     " 2- Pontuação",
                     " 3- Como Jogar",
                     " 4- Modo Hardcore(0-1000)",
                     " 5- Skins",
                     " 0- Sair",
                     "--------------------------------",
                 ]
        RetornarMenu = False
        os.system("cls")
        time.sleep(0.5)
        print("Escolha um numero entre 0 a 100")
        print("Escreva 'Ver' para revelar ou 'Menu' para ir ao menu")
        adivinha = input("Digite um numero: ")

        if adivinha == "Ver":
            os.system("cls")
            print("O numero secreto da jogada é: ",N_Correto)
            print("Escolha um numero entre 0 a 100")
            print("Escreva 'Ver' para revelar ou 'Menu' para ir ao menu")
            adivinha = input("Digite um numero: ")

        if adivinha == "Menu":
            RetornarMenu = True
            continue

        entrada2 = adivinha
        if entrada2.isnumeric():
            adivinha = int(entrada2)
            PodiCorrer = True
        else:
            PodiCorrer = False

        if PodiCorrer and adivinha != NumeroInteiroCorreto:
            print("Errou.")
            Tentativas -= 1

            if adivinha > NumeroInteiroCorreto:
                print("O Numero é menor que", adivinha)
            elif adivinha < NumeroInteiroCorreto:
                print("O Numero é maior que", adivinha)

            BullDog = abs(NumeroInteiroCorreto - adivinha)

            if BullDog < 2:
                print("MUITO MUITO PERTO")
            elif BullDog < 5:
                print("Estás muito perto")
            elif BullDog < 20:
                print("Estás perto")
            else:
                print("Estás longe")

            print("Tentativas restastes: ", Tentativas)
            input()

        if PodiCorrer and adivinha == NumeroInteiroCorreto:
            Pontos += 1
            print("ACERTOU +1 PONTO")
            NumeroInteiroCorreto = random.randint(0, 100)
            N_Correto = str(NumeroInteiroCorreto)
            Tentativas = 8


        if Tentativas == 0:
            print("O numero correto era", N_Correto)
            NumeroInteiroCorreto = random.randint(0, 100)
            N_Correto = str(NumeroInteiroCorreto)
            print("...")
            time.sleep(2.3)
            Tentativas = 10

    if Escolha == "3":
        if Escolha == "3":
            os.system("cls")
            print("COMO JOGAR")
            print("-----------")
            print("Objetivo: Adivinhar o número secreto.")
            print("Modos:")
            print("Normal: número entre 0 e 100")
            print("Hardcore: número entre 0 e 1000")
            print("")
            print("Pontuação:")
            print("Normal: +1 ponto por acerto")
            print("Hardcore: +2 pontos por acerto")
            print("")
            print("Clique Enter para retornar")
            input("")
            os.system("cls")
            RetornarMenu = True

    if Escolha == "5":
        os.system("cls")
        for Skin in Skins:
            print(Skin)
        Opcao = input("Escolha: ")
        if Opcao == "1":
            if Pontos >=3:
                Skins = [
                    "1: Skin Oceano(Equipado)",
                    "2: Skin Fogo - 5 Pontos",
                    "0 - Retornar",
                    "",
                ]
                os.system("color 1")
                os.system("cls")
                for Skin in Skins:
                    print(Skin)
            else:
                print("Nao tem Pontos sufcientes.")
                time.sleep(1)

        if Opcao == "2":
            if Pontos >=5:
                Skins = [
                    "1: Skin Oceano - 3 Pontos",
                    "2: Skin Fogo - (Equipado)",
                    "0 - Retornar",
                    "",
                ]
                os.system("cls")
                for Skin in Skins:
                    print(Skin)
                os.system("color 4")
            else:
                print("Nao tem Pontos sufcientes.")
                time.sleep(1)


        if Opcao == "3":
            os.system("cls")
            os.system("color 8")
            input("Pressione Enter para retornar")
            os.system("cls")
            RetornarMenu = True

    if Escolha == "2":
        os.system("cls")
        print("Voce tem:", Pontos, "pontos")
        input("Pressione ENTER para sair.")
        os.system("cls")
        RetornarMenu = True

    if Escolha == "4":
        Podes = 1
        os.system("cls")
        print("MODO HARDCORE")
        print("Escolha um numero entre 0 a 1000")
        print("Escreva 'Ver' para revelar ou 'Menu' para ir ao menu")
        adivinha1 = input("Digite um numero: ")

        if adivinha1 == "Ver":
            os.system("cls")
            print("O numero secreto é",N_Hard)
            print("Escolha um numero entre 0 a 100")
            print("Escreva 'Ver' para revelar ou 'Menu' para ir ao menu")
            adivinha1 = input("Digite um numero: ")

        if adivinha1 == "Menu":
            os.system("cls")
            RetornarMenu = True
            continue

        entrada = adivinha1
        if entrada.isnumeric():
            adivinha1 = int(entrada)
            PodiCorrer = True
        else:
            PodiCorrer = False

        if PodiCorrer and adivinha1 != NumeroCorretoHard:
            print("Errou.")
            Tentativas -= 1

            if adivinha1 > NumeroCorretoHard:
                print("O número é MENOR que", adivinha1)
            elif adivinha1 < NumeroCorretoHard:
                print("O número é MAIOR que", adivinha1)

            DogBull = abs(NumeroCorretoHard - adivinha1)

            if DogBull < 5:
                print("MUITO MUITO PERTO")
            elif DogBull < 15:
                print("MUITO perto")
            elif DogBull < 50:
                print("Bastante perto")
            elif DogBull < 110:
                print("Estás perto")
            else:
                print("Longe")

            print("Tentativas restantes:", Tentativas)
            input()

        if PodiCorrer and adivinha1 == NumeroCorretoHard:
            Pontos += 2
            print("ACERTOU +2 PONTOS")
            NumeroCorretoHard = random.randint(0, 1000)
            N_Hard = str(NumeroCorretoHard)
            Tentativas = 10
            time.sleep(2)

        if Tentativas == 0:
            print("O número correto era", N_Hard)
            print("...")
            time.sleep(2.3)

            NumeroCorretoHard = random.randint(0, 1000)
            N_Hard = str(NumeroCorretoHard)
            Tentativas = 10

    if Escolha not in ["0", "1", "2", "3", "4","5"]:
        print("Escolha uma opção valida.")
        Escolha = "0"
        time.sleep(1)
        os.system("cls")

