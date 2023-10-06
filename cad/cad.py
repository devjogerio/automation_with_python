# pysimplegui
# pip install PySimpleGUI

import PySimpleGUI as sg
sg.theme('Reddit')

product_categories = ["Esportes", "Comida", "Jardinagem", "Esportes"]

layout = [
    [sg.Text("Clientes", size=(6,0)), sg.Input(key='1', size=(20,0))],
    [sg.Text("Produtos", size=(6,0)), sg.Input(key='2', size=(20,0))],
    [sg.Text("Quantidade", size=(6,0)), sg.Input(key='3', size=(3,0))],
    [sg.Text("Categorias", size=(6,0)), sg.Combo(product_categories, key='4')],
    [sg.Button("Salvar")]
]

w = sg.Window("Cadastro de Produtos", layout)

while True:
    event, values = w.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Salvar":
        sg.popup("Produto Salvo!")
        w["1"].update("")
        w["2"].update("")
        w["3"].update("")
        w["4"].update("")

