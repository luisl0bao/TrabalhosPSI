import os

turmas = [
    [
        "10ºA",
        "GPSI",
        ["João Marcos", "Paula Nunes"],
        [["Segunda", "08:00-09:00", "PSI"],
         ["Segunda", "09:10-10:10", "PSI"],
         ["Segunda", "10:20-11:20", "PSI"],
         ["Segunda", "11:25-12:25", "Arquitetura de computadores"],
         ["Segunda", "12:35-13:35", "Arquitetura de computadores"],
         ["Terça", "08:00-09:00", "PSI"],
         ["Terça", "09:10-10:10", "PSI"],
         ["Terça", "10:20-11:20", "Arquitetura de computadores"],
         ["Terça", "11:25-12:25", "Arquitetura de computadores"],
         ["Terça", "12:35-13:35", "Arquitetura de computadores"], ],
        ["Abel Chongolola", "Muhammed Ali", "Mike Tyson", "João Marcos", "Harry Kane", "Pedro Alonso", "Luis Lobão",
         "Cristiano Ronaldo", "Messi"],
        [
            ["", "Abel Chongolola,Harry Kane", "", ""],
            ["", "", "", "Muhhamed Ali,Mike Tyson"],
            ["Pedro Alonso", "", "", "Luis Lobão"],
            ["", "", "João Marcos", "Cristiano Ronaldo,Messi"]
        ]
    ]
]
# nome,curso,professores,horarios,alunos,lugar
turma_atual = "10ºA"

# cores asci
COR_AZUL = "\033[1;34m"  # Azul mais vibrante para menus principais
COR_CIANO = "\033[1;36m"  # Ciano suave para cabeçalhos
COR_AMARELO = "\033[1;33m"  # Amarelo brilhante para destaques
COR_VERDE = "\033[1;32m"  # Verde (sucesso)
COR_VERMELHA = "\033[1;31m"  # Vermelho (erro)
COR_BRANCA = "\033[0m"  # Reset


def lugares_turma():
    limpar_ecra()
    print("========[LUGARES DA TURMA", turma_atual, "]========")

    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    if turma_selecionada is None:
        mensagem_erro("Turma não encontrada")
        espera()
        return

    lugares = turma_selecionada[5]

    print(COR_AZUL + "================")
    print("1 - Ver lugares")
    print("2 - Editar um lugar")
    print("0 - Retornar")
    print("================")

    escolha = input("Escolha: ").strip()

    while escolha not in ["0", "1", "2"]:
        escolha = input("Inválido, escolha novamente: ").strip()

    if escolha == "1":
        print("===============")
        fila_num = 1
        for fila in lugares:
            print("Fila", fila_num, "->", fila)
            fila_num += 1
        espera()
        lugares_turma()

    if escolha == "2":
        print("\nEstado atual dos lugares:")
        fila_num = 1
        for fila in lugares:
            print(fila_num, "->", fila)
            fila_num += 1

        fila_input = input("\nFila (1-4): ").strip()
        lugar_input = input("Mesa (1-4): ").strip()

        if not fila_input.isdigit() or not lugar_input.isdigit():
            mensagem_erro("Entrada inválida")
            espera()
            lugares_turma()
            return

        f = int(fila_input) - 1
        l = int(lugar_input) - 1

        if f < 0 or f > 3 or l < 0 or l > 3:
            mensagem_erro("Lugar fora dos limites")
            espera()
            lugares_turma()
            return

        atual = lugares[f][l]
        if atual != "":
            print("Lugar atualmente ocupado por:", atual)

        nome = input("Nome do(s) aluno(s) (vazio para limpar): ").strip()
        lugares[f][l] = nome
        mensagem_sucesso("Lugar atualizado com sucesso")
        espera()
        lugares_turma()

    if escolha == "0":
        return


def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")


def espera():
    input("Pressiona Enter para continuar...")


def cabecalho(texto):
    print(COR_CIANO + "=" * 50)
    print(texto.center(60))
    print(COR_CIANO + "=" * 50 + COR_BRANCA)


def mensagem_sucesso(texto):
    print(COR_VERDE + texto + COR_BRANCA)


def mensagem_erro(texto):
    print(COR_VERMELHA + texto + COR_BRANCA)


def mudar_turma():
    global turma_atual
    limpar_ecra()
    cabecalho("MUDAR TURMA")

    for turma in turmas:
        print("- " + turma[0] + " | Curso: " + turma[1])

    nome = input("Nome da turma: ").strip().upper()

    encontrou = False
    for turma in turmas:
        if turma[0] == nome:
            turma_atual = nome
            encontrou = True
            mensagem_sucesso("Turma atual é agora: " + turma_atual)
            break

    if not encontrou:
        mensagem_erro("ERRO: Turma não encontrada")

    espera()


def listar_todas_turmas():
    limpar_ecra()
    cabecalho("LISTA DE TURMAS")

    for turma in turmas:
        texto = "- " + turma[0] + " | Curso: " + turma[1]
        if turma[0] == turma_atual:
            texto += " (ATUAL)"
        print(texto)

    espera()


def mostrar_turma():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    if turma_selecionada is None:
        mensagem_erro("Turma não encontrada")
        espera()
        return

    cabecalho("DETALHES DA TURMA " + turma_atual)

    print("Curso:", turma_selecionada[1])

    print("Professores:")
    if len(turma_selecionada[2]) == 0:
        print(" (nenhum)")
    else:
        for professor in turma_selecionada[2]:
            print(" -", professor)

    print("Horários:")
    if len(turma_selecionada[3]) == 0:
        print(" (nenhum)")
    else:
        for horario in turma_selecionada[3]:
            print(" -", horario[0], "|", horario[1], "|", horario[2])

    print("Alunos:")
    if len(turma_selecionada[4]) == 0:
        print(" (nenhum)")
    else:
        for aluno in turma_selecionada[4]:
            print(" -", aluno)

    espera()


def adicionar_professor():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    nome = input("Nome do professor: ").strip()
    if nome == "":
        mensagem_erro("ERRO: não pode ser vazio")
    elif nome in turma_selecionada[2]:
        mensagem_erro("Professor já existe")
    else:
        turma_selecionada[2].append(nome)
        mensagem_sucesso("Professor adicionado")

    espera()


def remover_professor():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    print("Lista de professores:")
    for professor in turma_selecionada[2]:
        print("-", professor)

    nome = input("Nome do professor a remover: ").strip()
    if nome in turma_selecionada[2]:
        turma_selecionada[2].remove(nome)
        mensagem_sucesso("Professor removido")
    else:
        mensagem_erro("Professor não encontrado")

    espera()


def adicionar_horario():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    dia = input("Dia: ").strip()
    hora = input("Hora: ").strip()
    disciplina = input("Disciplina: ").strip()

    if dia != "" and hora != "" and disciplina != "":
        turma_selecionada[3].append([dia, hora, disciplina])
        mensagem_sucesso("Horário adicionado")
    else:
        mensagem_erro("ERRO: dados incompletos")

    espera()


def remover_horario():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    print("Horários da turma:")
    for horario in turma_selecionada[3]:
        print("-", horario[0], "|", horario[1], "|", horario[2])

    dia = input("Dia do horário: ").strip()
    hora = input("Hora do horário: ").strip()

    encontrado = False
    for horario in turma_selecionada[3]:
        if horario[0] == dia and horario[1] == hora:
            turma_selecionada[3].remove(horario)
            encontrado = True
            mensagem_sucesso("Horário removido")
            break

    if not encontrado:
        mensagem_erro("Horário não encontrado")

    espera()


def adicionar_aluno():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    print("Alunos da turma:")
    for aluno in turma_selecionada[4]:
        print("-", aluno)

    nome = input("Nome do aluno: ").strip()
    if nome == "":
        mensagem_erro("ERRO: não pode ser vazio")
    elif nome in turma_selecionada[4]:
        mensagem_erro("Aluno já existe")
    else:
        turma_selecionada[4].append(nome)
        mensagem_sucesso("Aluno adicionado")

    espera()


def remover_aluno():
    limpar_ecra()
    print("-- REMOVER ALUNO --")

    turma_selecionada = None
    nome_turma = input("Turma: ").strip()
    for turma in turmas:
        if turma[0] == nome_turma:
            turma_selecionada = turma
            break

    if turma_selecionada is None:
        mensagem_erro("Turma não encontrada")
        espera()
        return

    limpar_ecra()
    print("-- REMOVER ALUNO --")
    print("Alunos da turma:")
    for aluno in turma_selecionada[4]:
        print("-", aluno)

    nome = input("Nome do aluno a remover: ").strip()
    if nome in turma_selecionada[4]:
        turma_selecionada[4].remove(nome)
        mensagem_sucesso("Aluno removido")
    else:
        mensagem_erro("Aluno não encontrado")

    espera()


def listar_alunos():
    limpar_ecra()
    turma_selecionada = None
    for turma in turmas:
        if turma[0] == turma_atual:
            turma_selecionada = turma
            break

    cabecalho("ALUNOS DA TURMA " + turma_atual)

    if len(turma_selecionada[4]) == 0:
        print("(nenhum aluno)")
    else:
        for aluno in turma_selecionada[4]:
            print("-", aluno)

    espera()


def adicionar_turma():
    limpar_ecra()
    cabecalho("ADICIONAR NOVA TURMA")

    nome = input("Nome da turma: ").strip()
    if nome == "":
        mensagem_erro("ERRO: nome vazio")
        espera()
        return

    curso = input("Curso [GPSI]: ").strip()
    if curso == "":
        curso = "GPSI"

    for turma in turmas:
        if turma[0] == nome:
            mensagem_erro("ERRO: Turma já existe")
            espera()
            return

    turmas.append([nome, curso, [], [], [], [
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""]
    ]])
    mensagem_sucesso("Turma adicionada com sucesso")
    espera()


def remover_turma():
    limpar_ecra()
    print("-- REMOVER TURMA --")

    print("Turmas disponíveis:")
    for turma in turmas:
        print("-", turma[0])

    nome = input("Nome da turma a remover: ").strip()

    turma_selecionada = None
    for turma in turmas:
        if turma[0] == nome:
            turma_selecionada = turma
            break

    if turma_selecionada is None:
        mensagem_erro("Turma não encontrada")
    else:
        turmas.remove(turma_selecionada)
        mensagem_sucesso("Turma removida")

    espera()


def menu():
    while True:
        limpar_ecra()
        cabecalho(COR_CIANO + "Turma atual: " + turma_atual + COR_BRANCA)
        print(COR_AMARELO + "	Opções:" + COR_BRANCA)
        print("0 - Lista de alunos")
        print("1 - Selecionar turma")
        print("2 - Lista de turmas")
        print("3 - Informações da turma")
        print(COR_VERDE + "4 - Adicionar professor" + COR_BRANCA)
        print(COR_VERMELHA + "5 - Remover professor" + COR_BRANCA)
        print(COR_VERDE + "6 - Adicionar horário" + COR_BRANCA)
        print(COR_VERMELHA + "7 - Remover horário" + COR_BRANCA)
        print(COR_VERDE + "8 - Adicionar aluno" + COR_BRANCA)
        print(COR_VERMELHA + "9 - Remover aluno" + COR_BRANCA)
        print(COR_VERDE + "10 - Adicionar uma turma" + COR_BRANCA)
        print(COR_VERMELHA + "11 - Remover turma" + COR_BRANCA)
        print(COR_AZUL + "12 - GERIR LUGARES" + COR_BRANCA)
        print("0 - Sair")

        opcao = input(COR_VERDE + "Opção: " + COR_AZUL).replace(" ", "").lower()
        if opcao == "1" or opcao == "selecionarturma":
            mudar_turma()
        elif opcao == "2" or opcao == "listadeturmas":
            listar_todas_turmas()
        elif opcao == "3" or opcao == "informaçõesdaturma":
            mostrar_turma()
        elif opcao == "4" or opcao == "adicionarprofessor":
            adicionar_professor()
        elif opcao == "5" or opcao == "removerprofessor":
            remover_professor()
        elif opcao == "6" or opcao == "adicionarhorario":
            adicionar_horario()
        elif opcao == "7" or opcao == "removerhorario":
            remover_horario()
        elif opcao == "8" or opcao == "adicionaraluno":
            adicionar_aluno()
        elif opcao == "0" or opcao == "listadealunos":
            listar_alunos()
        elif opcao == "10" or opcao == "adicionarumaturma":
            adicionar_turma()
        elif opcao == "11" or opcao == "removerturma":
            remover_turma()
        elif opcao == "9" or opcao == COR_VERMELHA + "removeraluno":
            remover_aluno()
        elif opcao == "0" or opcao == "sair":
            print(COR_VERMELHA + "A sair..." + COR_BRANCA)
            break
        elif opcao == "12":
            lugares_turma()
        else:
            mensagem_erro("Opção inválida")
            espera()


menu()
