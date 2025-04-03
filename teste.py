import pandas as pd

# URL do arquivo csv no GitHub
url = 'https://raw.githubusercontent.com/nisston/disciplinaestruturadedados/main/data_temp.csv'

# Ler o arquivo CSV usando pandas e criando o objeto df1 (DataFrame)
df1 = pd.read_csv(url)

# Verificando o tamanho do DataFrame
df1.shape

# Exibir a estrutura do DataFrame
df1.info()

# Verificando se existe conteúdo em branco no dataframe
df1.isnull().sum()

# Apagando os conteúdos em branco no dataframe
df1.dropna(inplace=True, axis=0)

lista_questao_9 = df1[4000:5000]['Temperature'].to_list()

acima = 0
print(len(lista_questao_9))
print(max(lista_questao_9))
print(min(lista_questao_9))

for i in range(len(lista_questao_9)):
  if lista_questao_9[i] >= 1550.0:
    acima += 1
print(f'A quantidade de temperaturas acima de 1550 é: {acima}')