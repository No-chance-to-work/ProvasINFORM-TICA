n = input("Digite um número: ")
digitos = [int(d) for d in n]
media = sum(digitos) / len(digitos)
mais_proximo = digitos[0]
for d in digitos:
    if abs(d - media) < abs(mais_proximo - media):
        mais_proximo = d
print("Dígito mais próximo da média:", mais_proximo)