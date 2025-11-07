a, b = 1, 1  # primeiros dois termos
for i in range(3, 52):  # vai até o 51º termo
    a, b = b, a + b
print("51º termo da sequência:", b)