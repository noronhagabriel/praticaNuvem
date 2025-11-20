# Funções de conversão

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Entrada do usuário
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

# Conversão
if origem == "C":
    if destino == "F":
        resultado = celsius_para_fahrenheit(temp)
    elif destino == "K":
        resultado = celsius_para_kelvin(temp)
    else:
        resultado = temp

elif origem == "F":
    if destino == "C":
        resultado = fahrenheit_para_celsius(temp)
    elif destino == "K":
        resultado = fahrenheit_para_kelvin(temp)
    else:
        resultado = temp

elif origem == "K":
    if destino == "C":
        resultado = kelvin_para_celsius(temp)
    elif destino == "F":
        resultado = kelvin_para_fahrenheit(temp)
    else:
        resultado = temp

else:
    print("Unidade inválida!")
    exit()

# Resultado final
print(f"\n=== Conversor de Temperatura ===")
print(f"Temperatura original: {temp} {origem}")
print(f"Temperatura convertida: {resultado:.2f} {destino}")
