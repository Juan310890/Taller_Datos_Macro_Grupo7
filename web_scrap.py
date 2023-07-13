import requests
import pandas as pd
from bs4 import BeautifulSoup

fecha = []
pib_anual = []
var_pib = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

# soup.findAll('div', attrs={'class':'col-sm-6'})
tabla = soup.find('table')
filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fecha.append(celdas[0].string)
        pib_anual.append(celdas[1].string)
        var_pib.append(celdas[3].string)

print(fecha)
print(pib_anual)
print(var_pib)

df = pd.DataFrame({'Fecha': fecha, 'PIB ANUAL': pib_anual, 'VAR PIB(%)': var_pib})
df.to_csv('PIB-ECUADOR.csv', index=False, encoding='utf-8')
