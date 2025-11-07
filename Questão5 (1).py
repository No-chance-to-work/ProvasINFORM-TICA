def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat
n = int(input("Digite um número: "))
soma = 0
for i in range(1, n+1):
    soma += fatorial(i)
print("Soma dos fatoriais =", soma)