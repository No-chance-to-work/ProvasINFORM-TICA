num = input("Digite um número: ")
soma = 0
for d in num:
    d = int(d)
    if d in [2, 3, 5, 7]:
        soma += d
print("Soma dos dígitos primos:", soma)