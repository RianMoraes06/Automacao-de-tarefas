#passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar: pip install pyautogui
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> pressionar uma combinação de teclas
pyautogui.PAUSE = 0.3

# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.click(x=1086, y=468)
# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

# Passo 2: Fazer login
# Selecionar campo de email
pyautogui.click(x=696, y=375)
pyautogui.write("rianmorae8@gmail.com")
pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("automacao_python")

pyautogui.press("tab") # clique no botao de login
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Abrir/importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)
# tabula -> transforma pdf em pandas
# Passo 4: Cadastrar um produto

for linha in tabela.index: # As linhas da tabela são chamadas de índices = index

# str = string = texto
    # Clicar no campo do código do produto
    # Preencher o codigo
    pyautogui.click(x=701, y=258)
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
    # Passar pro proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # Passar pro proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # Passar pro proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # Passar pro proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # Passar pro proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # Passar pro proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # Passar pro proximo campo
    pyautogui.press("tab")
    # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Usa o scroll do mouse para subir ou descer a tela

# Passo 5: Repetir isso até acabar a lista de produtos
# pyperclip