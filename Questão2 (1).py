num = int(input("Digite um número decimal: "))
if num == 0:
    print("0")
else:
    binario = ""
    n = num
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2

    print(f"{num} em binário é {binario}")