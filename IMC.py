altura = input("Digite sua altura em metros: ")
peso = input("Digite seu peso em kg: ")
imc = float(peso) / float(altura**2)

if imc < 18.5:
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Eutrofia, peso adequado")
elif imc >= 25.0 and imc <= 29.9:
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Sobrepeso")
elif imc >= 30.0 and imc <= 34.9: 
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Obsesidade grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Obesidade grau 2")
else:
    print(f"{imc:,.1f} Sua classificação de acordo com a oms é: Obesidade extrema")



