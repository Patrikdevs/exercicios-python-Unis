idade = int(input("Entre com a idade em dias: "))

ano=idade//360

dias_meses=idade-(ano*360)

mes=dias_meses//30

dias=dias_meses-(mes*30)

print("Voce tem {0} ano/s, {1} mes/meses e {2} dia/s de vida.".format(ano, mes, dias))