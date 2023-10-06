# openpysl
# pyautogui
# mouseinfo -> pip install mouseinfo (windows)

import openpyxl
import pyautogui

# mapeou o caminho da planilha
wb = openpyxl.load_workbook("sheet.xlsx")

p_produto = wb["cadastro"]

for linha in p_produto.iter_rows(min_row=2):
    # Cliente
    pyautogui.click(2175, 88, duration=1.3)
    pyautogui.write(linha[0].value)
    # Produto
    pyautogui.click(2175, 115, duration=1.3)
    pyautogui.write(linha[1].value)
    # Quantidade
    pyautogui.click(2172, 145, duration=1.3)
    pyautogui.write(str(linha[2].value))
    #  Categoria
    pyautogui.click(2238, 181, duration=1.3)
    pyautogui.write(linha[1].value)
    pyautogui.click(2198, 194, duration=1.3)
    # clique em salvar
    pyautogui.click(2132, 209, duration=1.3)
    # clique em OK
    pyautogui.click(1279, 574, duration=1.3)