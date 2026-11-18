a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Os valores formam um triângulo")
    print("Área =", area)
else:
    print("Não formam um triângulo")
    print("Valores lidos:", a, b, c)
    )

