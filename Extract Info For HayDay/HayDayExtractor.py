# extract data from https://hayday.fandom.com/wiki/Crops_List

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://hayday.fandom.com/wiki/Crops_List'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable sortable'})


def extrairFrutas(dataa, Produtoss, Tipoo, Nivell, Preçoo, Tempoo, Xpp):
    for roww in dataa:
        if roww.__contains__('Bush') or roww.__contains__('Tree'):
            for i in range(len(roww)):
                if i == len(roww) - 1:
                    roww.pop(i)
                else:
                    match i:
                        case 0:
                            Produtoss.append(roww[i])
                        case 1:
                            Tipoo.append(roww[i])
                        case 2:
                            Nivell.append(roww[i])
                        case 3:
                            Preçoo.append(roww[i])
                        case 4:
                            Tempoo.append(roww[i])
                        case 5:
                            Xpp.append(roww[i])


def extrairPlantacao(dataa, Produtoss, Tipoo, Nivell, Preçoo, Tempoo, Xpp):
    for roww in dataa:
        if roww.__contains__('Crop'):
            for i in range(len(roww)):
                if i == len(roww) - 1:
                    roww.pop(i)
                else:

                    match (i):
                        case 0:
                            Produtoss.append(roww[i])
                        case 1:
                            Tipoo.append(roww[i])
                        case 2:
                            Nivell.append(roww[i])
                        case 3:
                            Preçoo.append(roww[i])
                        case 4:
                            Tempoo.append(roww[i])
                        case 5:
                            Xpp.append(roww[i])


def printarTempo(Tempoo):
    for i in Tempoo:
        if i.__contains__('h'):
            horas = i.split('h')[0]
            minutos = i.split('h')[1].split('m')[0]
            if len(minutos) > 0:
                minutos = int(horas) * 60 + int(minutos)
            else:
                minutos = int(horas) * 60

            print(minutos)
        else:
            print(i.split('m')[0])


def printarOutros(array):
    for i in array:
        print(i)


# extract data from table
data = []
for row in table.find_all('tr'):
    data.append([t.text.strip() for t in row.find_all('td')])

Produtos = []
Tipo = []
Nivel = []
Preço = []
Tempo = []
Xp = []

extrairFrutas(data, Produtos, Tipo, Nivel, Preço, Tempo, Xp)

printarOutros(Xp)
