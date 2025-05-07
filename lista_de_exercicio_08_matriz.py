# Você precisa verificar quantas horas de sono uma determinada pessoa dorme durante o mês, considerando
# que o mês apresente apenas quatro semanas e que os dias da semana a considerar devem ser segunda, terça,
# quarta, quinta e sexta-feira. Construa uma estrutura de matriz para representar esses dados e tentar

#    Seg Ter Qua Qui Sex
# S1 8 6 7 8 6
# S2 5 5 6 7 8
# S3 6 7 8 6 5
# S4 7 5 9 7 4

# 1. Qual o dia da semana com maior horário de descanso?
# 2. Qual o dia da semana com menor horário de descanso?
# 3. Qual a semana com maior horário de descanso?
# 4. Qual a semana com menor horário de descanso?
# 5. Qual o menor tempo de descanso?
# 6. Qual o maior tempo de descanso?
# 7. Quantos dias da semana tive com o menor tempo de descanso?
# 8. Quantos dias da semana tive com o maior tempo de descanso?
# 9. Qual a percentagem por semana em relação ao total por mês?


# Respostas:
# # 1. Dia com maior descanso: Qua
# # 2. Dia com menor descanso: Ter
# # 3. Semana com maior descanso: S1
# # 4. Semana com menor descanso: S2
# # 5. Menor valor de descanso: 4
# # 6. Maior valor de descanso: 9
# # 7. Quantidade de dias com menor valor: 1
# # 8. Quantidade de dias com maior valor: 1
# # 9. Porcentagem de descanso por semana:
# # S1: 26.92%
# # S2: 23.85%
# # S3: 24.62%
# # S4: 24.62%

dados = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex"]
semanas = ["S1", "S2", "S3", "S4"]

totais_dias = [0, 0, 0, 0, 0]
i = 0
while i < 4:
    j = 0
    while j < 5:
        totais_dias[j] = totais_dias[j] + dados[i][j]
        j = j + 1
    i = i + 1

maior_dia = 0
menor_dia = 0
i = 1
while i < 5:
    if totais_dias[i] > totais_dias[maior_dia]:
        maior_dia = i
    if totais_dias[i] < totais_dias[menor_dia]:
        menor_dia = i
    i = i + 1

totais_semana = [0, 0, 0, 0]
i = 0
while i < 4:
    j = 0
    while j < 5:
        totais_semana[i] = totais_semana[i] + dados[i][j]
        j = j + 1
    i = i + 1

maior_semana = 0
menor_semana = 0
i = 1
while i < 4:
    if totais_semana[i] > totais_semana[maior_semana]:
        maior_semana = i
    if totais_semana[i] < totais_semana[menor_semana]:
        menor_semana = i
    i = i + 1


maior_valor = dados[0][0]
menor_valor = dados[0][0]
i = 0
while i < 4:
    j = 0
    while j < 5:
        if dados[i][j] > maior_valor:
            maior_valor = dados[i][j]
        if dados[i][j] < menor_valor:
            menor_valor = dados[i][j]
        j = j + 1
    i = i + 1

cont_maior = 0
cont_menor = 0
i = 0
while i < 4:
    j = 0
    while j < 5:
        if dados[i][j] == maior_valor:
            cont_maior = cont_maior + 1
        if dados[i][j] == menor_valor:
            cont_menor = cont_menor + 1
        j = j + 1
    i = i + 1

total_geral = 0
i = 0
while i < 4:
    total_geral = total_geral + totais_semana[i]
    i = i + 1


porcentagens = [0, 0, 0, 0]
i = 0
while i < 4:
    porcentagens[i] = (totais_semana[i] * 100.0) / total_geral
    i = i + 1

print("1. Dia com maior descanso:", dias_semana[maior_dia])
print("2. Dia com menor descanso:", dias_semana[menor_dia])
print("3. Semana com maior descanso:", semanas[maior_semana])
print("4. Semana com menor descanso:", semanas[menor_semana])
print("5. Menor valor de descanso:", menor_valor)
print("6. Maior valor de descanso:", maior_valor)
print("7. Quantidade de dias com menor valor:", cont_menor)
print("8. Quantidade de dias com maior valor:", cont_maior)
print("9. Porcentagem de descanso por semana:")

i = 0
while i < 4:
    print(semanas[i] + ": " + str(round(porcentagens[i], 2)) + "%")
    i = i + 1