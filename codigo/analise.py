#importação biblioteca

import pandas as pd


dgf = pd.read_csv('Gapminder.csv',error_bad_lines=False, sep=";")
#Alterando o cabeçalho da coluna!
traducao_nome_tabela = dgf.rename(columns={'country':"Pais",'continent':"Continente",'year':"Ano",'lifeExp':"Exp de Vida",'pop':"Populacao Total",'gdpPercap':"Pib"})
print(f'Traduzindo cabecalho da Tabela\n')
print(traducao_nome_tabela)
#Total de linhas e Colunas
print("===================================================")
total_linhas_colunas = traducao_nome_tabela.shape
print(f'Total de Linhas e Colunas: {total_linhas_colunas}')
print("===================================================")
#Tipo de dados nas Colunas
tipo_de_dados = traducao_nome_tabela.dtypes
print(f'Tipos de dados: {tipo_de_dados}')
print("===================================================")
#Ultimas LInhas da Tabela
print("Ultimas Linhas\n")
ultimas_linhas_tabela = traducao_nome_tabela.tail()
print(ultimas_linhas_tabela)
print("===================================================")
#Informações estatisticas
print("Informacao Estatistica")
info_estatistica = traducao_nome_tabela.describe()
print(info_estatistica)
print("===================================================")
#Pesquisa
filtro = traducao_nome_tabela.loc[traducao_nome_tabela['Continente'] == "Asia"]
print("Pesquisa Especifica")
print(filtro)
print("===================================================")