import pandas as pd
import pyautogui as pag
import time 
tabela = pd.read_csv("produtos.csv")
tabela.head()

pag.PAUSE = 0.5 #Pausa entre comandos pag

# Abrir o navegador
pag.press("win")
pag.write("chrome")
pag.press("enter")

# Acessar o site
pag.click(x=569, y=850)
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")     

pag.press("enter")
time.sleep(1)

# Fazer login
pag.press("tab")
pag.write("generic@email.com")
pag.press("tab")
pag.write("senha1234")
pag.press("tab")
pag.press("enter")

time.sleep(2)
print(pag.position())

for linha in range(10): 
    pag.click(x=859, y=252)
    pag.write(tabela.loc[linha,"codigo"])
    pag.press("tab")
    pag.write(tabela.loc[linha,"marca"])
    pag.press("tab")
    pag.write(tabela.loc[linha,"tipo"])
    pag.press("tab")
    pag.write(str(tabela.loc[linha,"categoria"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha,"preco_unitario"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha,"custo"]))
    pag.press("tab")
    if pd.isna(tabela.loc[linha,"obs"]):
        pag.write("Sem observacoes")
    else:
        pag.write(tabela.loc[linha,"obs"])
    pag.press("tab")
    pag.press("enter")
    


