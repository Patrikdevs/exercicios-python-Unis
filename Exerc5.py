def inverter_palavras(frase):
  palavras = frase.split()
  nova_frase = []

  for palavra in palavras:
    invertida = palavra[::-1]
    nova_frase.append(invertida)

  return " ".join(nova_frase)


# Testando com a frase do exercício
frase = "ola professor alberane"
resultado = inverter_palavras(frase)

print("Frase original:", frase)
print("Frase invertida:", resultado)
