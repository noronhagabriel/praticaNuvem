real = 100.00
dolar = 5.20
euro = 6.15

realDolar = round(real / dolar, 2)
realEuro = round(real / euro, 2)

print(str(real) + " reais ficam " + str(realDolar) + " dólares")
print(str(real) + " reais ficam " + str(realEuro) + " euros")