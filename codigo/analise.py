#importação biblioteca

import pandas as pd


print("Usando Pandas")

dgf = pd.read_csv('Gapminder.csv',error_bad_lines=False, sep=";")
#Alterando o cabeçalho da coluna!
traducao_nome_tabela = dgf.rename(columns={'country':"Pais",'continent':"Continente",'year':"Ano",'lifeExp':"Exp de Vida",'pop':"Populacao Total",'gdpPercap':"Pib"})

print(dgf.describe())