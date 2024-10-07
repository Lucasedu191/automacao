import pyautogui
import time
import pandas as pd

# Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Espera um tempo para garantir que o sistema esteja pronto
time.sleep(3)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código (ajuste as coordenadas conforme necessário)
    pyautogui.click(x=486, y=257)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher os outros campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    # Verifica se o campo de observação não está vazio
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    # Cadastrar o produto (botão enviar)
    pyautogui.press("enter")
    
    # Dar scroll para garantir que o próximo produto seja cadastrado corretamente
    pyautogui.scroll(5000)

    # Pausa para evitar possíveis erros no preenchimento (ajuste o tempo conforme necessário)
    time.sleep(1)