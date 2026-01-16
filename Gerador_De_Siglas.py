def confusar(argumento):
    argumento = argumento.replace("e", "3").replace("E", "3")
    argumento = argumento.replace("i", "1").replace("I", "1")
    argumento = argumento.replace("o", "0").replace("O", "0")
    argumento = argumento.replace("s", "$").replace("S", "$")
    argumento = argumento.replace("a", "@").replace("A", "@")
    return argumento
    
print("=======<GERADOR DE SIGLAS>=======")

def continuar():
    frase = input("Digite uma frase: ")
    while frase == '':
        frase = input("Digite uma frase válida: ")
    sigla = ""
    for palavra in frase.split():
        sigla = sigla + palavra[0].upper()
    password = ""

    for palavra2 in frase.split():
        password = password + palavra2[:2].upper() #Vai pegar 2 por 2 letras por cada palavra

    password = confusar(password.upper())
    print(sigla, "=", "Sigla")
    print(password, "=", "Password")
    quer = input("Quer fazer denovo? S/N : ")
    if quer == 'n' or quer == 'N':
        exit()
    else:
        continuar()
continuar()
quer = input("Quer fazer denovo? S/N : ")
if quer == 'n' or quer == 'N':
    exit()
else:
    if quer != "S" or quer != "s":
        print("Você nao escreveu N ou S, escreveu:",quer,"-> Continuando...")
    print("Continuando..")
    continuar()
continuar()
