n = input("Digite um número: ")
cont = 0
for d in n:
    if int(d) % 2 != 0:
        cont += 1
f = 1
for i in range(1, cont + 1):
    f *= i
print(f"Resultado: {cont}! = {f}")