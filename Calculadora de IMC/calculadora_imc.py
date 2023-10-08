import PySimpleGUI as sg
from funcoes import *

sg.theme('GrayGrayGray')   # Add a touch of color
# All the stuff inside your janela.
layout = [  [sg.Text('Altura (em metros)'), sg.InputText(key="altura")],
            [sg.Text('Peso (em Kg)       '), sg.InputText(key="peso")],
            [sg.Text('Idade                   '), sg.InputText(key="idade")],
            [sg.Text('')],
            [sg.Text('', key="print_imc")],
            [sg.Text('', key="print_aval")],
            [sg.Text('')],
            [sg.Button('Calcular'), sg.Button('Cancelar')],
        ]

# Create the janela
janela = sg.Window('Calculadora IMC', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar': # if user closes janela or clicks cancel
        break
    if event == 'Calcular':
        try:
            altura = float(values["altura"])
            peso = float(values["peso"])
            idade = int(values["idade"])
            imc = calc_imc(altura, peso)
            janela["print_imc"].update(f"IMC: {imc:.2f}")
            if idade > 65:
                if imc < 22:
                    janela["print_aval"].update('Abaixo do peso.')
                elif imc > 22 and imc < 27:
                    janela["print_aval"].update('Peso ideal.')
                elif imc >= 27:
                    janela["print_aval"].update('Sobrepeso.')
            elif idade <= 65:
                if imc < 18.5:
                    janela["print_aval"].update('Abaixo do peso.')
                elif imc > 18.5 and imc < 25:
                    janela["print_aval"].update('Peso ideal.')
                elif imc > 25 and imc < 30:
                    janela["print_aval"].update('Levemente acima do peso.')
                elif imc > 30 and imc < 35:
                    janela["print_aval"].update('Obesidade Grau I.')
                elif imc > 35 and imc < 40:
                    janela["print_aval"].update('Obesidade Grau II.')
                elif imc > 40:
                    janela["print_aval"].update('Obesidade Grau III.')
            janela["altura"].update('')
            janela["peso"].update('')
            janela["idade"].update('')
        except:
            janela["print_imc"].update("Dados inseridos incorretamente.")
            janela["print_aval"].update('Tente novamente.')

janela.close()