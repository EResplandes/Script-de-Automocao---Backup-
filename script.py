# Importando Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import date
import datetime
import time
import pyautogui as pya

dia = date.today()

# Passo 1 - Abrindo o FileZila
pya.hotkey("win")
time.sleep(2)
pya.write("Filezila")
time.sleep(2)
pya.press("Enter")
time.sleep(3)

# Passo 2 - Abrindo a Rede Pública
pya.click(x=136, y=306)
time.sleep(2)
pya.hotkey('Ctrl' , 'a')
time.sleep(2)
pya.press("Backspace")  
time.sleep(2)
pya.write("V:/")
time.sleep(2)
pya.press("Enter")

# Passo 3 - Logando na Rede de Manutenção
pya.click(x=121, y=88)
time.sleep(2)
pya.write("Endeço IP da VM)
time.sleep(2)
pya.press("Tab")
time.sleep(2)
pya.write("Usuário da VM")
pya.press("Tab")
time.sleep(2)
pya.write("Senha da VM")
pya.press("Tab")
pya.press("Tab")
time.sleep(2)
pya.press("Enter")

# Passo 4 - Abrindo Diretório de Backup
pya.click(x=846, y=309)
time.sleep(2)
pya.hotkey("Ctrl" , "a")
time.sleep(2)
pya.press("Backspace")
time.sleep(2)
pya.write("/mnt/Principal/Rede_Manutencao/Backups/Rede_Publica/2023")
time.sleep(2)
pya.press("Enter")
time.sleep(2)

# Passo 5 - Criando Pasta com a Data do Dia
pya.click(x=913, y=536)
time.sleep(2)
pya.hotkey("Ctrl" , "Shift", "n")
time.sleep(2)
pya.write(f"{dia}")
time.sleep(2)
pya.press("Enter")
time.sleep(2)
pya.click(x=747, y=468)
time.sleep(2)
pya.press('Enter')
time.sleep(2)

# Passo 6 - Colando arquivos da Rede Pública
pya.click(x=245, y=582)
time.sleep(2)
pya.hotkey("Ctrl" , "a" )
time.sleep(2)
pya.click(button="right")
time.sleep(2)
pya.press("down")
time.sleep(2)
pya.press('Enter')
time.sleep(3600)

# Passo 7 - Apagando arquivos da pública
pya.click(x=234, y=604)
time.sleep(2)
pya.hotkey('Ctrl' , 'a')
time.sleep(2)
# pya.press('Delete')
time.sleep(2)
# pya.press('Enter')
time.sleep(1000)

# Passo 8 - Escolhendo diretório do SISGRAFEx e Sistema de Portaria
pya.click(x=1187, y=309)
time.sleep(2)
pya.hotkey('Ctrl', 'a')
time.sleep(2)
pya.write('/mnt/Principal/Rede_Manutencao/Backups/Rede_Publica/Padrao')
time.sleep(2)
pya.click(x=723, y=466)
time.sleep(2)
pya.hotkey('Ctrl', 'a')
time.sleep(2)
pya.click(button= 'right')
time.sleep(2)
pya.press("down")
time.sleep(2)
pya.press('Enter')
time.sleep(2)
