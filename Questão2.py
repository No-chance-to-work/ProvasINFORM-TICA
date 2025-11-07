n = int(input("Digite um número decimal: "))
hexadecimal = ""
hex_chars = "0123456789ABCDEF"
while n > 0:
    resto = n % 16
    hexadecimal = hex_chars[resto] + hexadecimal
    n //= 16
print("Hexadecimal:", hexadecimal)