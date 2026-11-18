def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


# Testando de 1 a 100
for n in range(1, 101):
    if eh_primo(n):
        print(n, "é primo")
    else:
        print(n, "não é primo")
