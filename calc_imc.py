# Calculadora de IMC: Crie um programa que calcule o Índice de Massa Corporal com base no peso, idade e altura do usuário

def imc(altura, peso):
    x = peso / (altura**2)
    return x

idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua Altura (em metros): '))
peso = float(input('Digite seu peso (em Kg): '))
imc = imc(altura, peso)

print(f"IMC: {imc:.2f}")

if idade > 65:
    if imc < 22:
        print('Abaixo do peso.')
    elif imc > 22 and imc < 27:
        print('Peso ideal.')
    elif imc >= 27:
        print('Sobrepeso.')
elif idade <= 65:
    if imc < 18.5:
        print('Abaixo do peso.')
    elif imc > 18.5 and imc < 25:
        print('Peso ideal.')
    elif imc > 25 and imc < 30:
        print('Levemente acima do peso.')
    elif imc > 30 and imc < 35:
        print('Obesidade Grau I.')
    elif imc > 35 and imc < 40:
        print('Obesidade Grau II.')
    elif imc > 40:
        print('Obesidade Grau III.')