#Projeto desevenvolvido durante o intensivão de Python da @hastagtreinamentos
#Projeto de automação para cadastramento de uma lista de produtos
#insight: organizar a lógica de programação por passos do que seria feito manualmente, fica mais fácil o entedimento inicialmente. por comentários
#lembrando de intalar o pyautogui e o pandas

import pyautogui
import pandas
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 1
#passo 1: entrar no site da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#fazer pausa maior pro site carregar
time.sleep(3)
#passo 2: fazer login
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")   
pyautogui.write("nicoli")   
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(3)
 

#passo 3: abrir base de dados
import pandas
tabela = pandas.read_csv("PROJETO_AUTOMACAO/produtos.csv")
  

#passo 4: cadastrar primeiro produto
#passo 5: laço de repetição enquanto houver produtos
pyautogui.press("tab")  
for linha in tabela.index:
    pyautogui.click(x=1153, y=232)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
pyautogui.scroll(5000)



      

