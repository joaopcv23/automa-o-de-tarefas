import pyautogui
import time



pyautogui.PAUSE = 1    
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep (1)
pyautogui.click(x=656, y=367)
pyautogui.write("joaopcv23")
pyautogui.press("tab")
pyautogui.write("Banheiro001.")     
pyautogui.press("tab")
pyautogui.press("enter")

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=454, y=241)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]

    pyautogui.write(str(marca))

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    

    cat = tabela.loc[linha, "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(cat))
    
    
    preco = tabela.loc [linha, "uni"]
    pyautogui.press("tab")
    pyautogui.write(str(preco))

    custo = tabela.loc [linha, "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna (obs):
        pyautogui.press("tab")
        pyautogui.write(str(obs))
    
   

    pyautogui.press("tab")
    pyautogui.press ("enter")

    pyautogui.scroll(10000)




