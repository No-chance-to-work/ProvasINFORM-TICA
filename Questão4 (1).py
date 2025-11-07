maior_peso_m = 0
nome_maior_peso_m = ""
maior_altura_f = 0
nome_maior_altura_f = ""
soma_idades = 0
qtd = 0
while True:
    nome = input("Nome do atleta (@ para encerrar): ")
    if nome == "@":
        break
    sexo = input("Sexo (M/F): ").upper()
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    print()
    qtd += 1
    soma_idades += idade
    if sexo == "M" and peso > maior_peso_m:
        maior_peso_m = peso
        nome_maior_peso_m = nome
    if sexo == "F" and altura > maior_altura_f:
        maior_altura_f = altura
        nome_maior_altura_f = nome
media_idade = soma_idades / qtd if qtd > 0 else 0
print("Atleta masculino com maior peso:", nome_maior_peso_m)
print("Atleta feminina com maior altura:", nome_maior_altura_f)
print("Média das idades dos atletas:", media_idade)