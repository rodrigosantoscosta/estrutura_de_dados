frutas = ['banana', 'abacaxi', 'melao', 'laranja']
frutas_com_vogais = []

# for i in frutas:
#     n_vogais = 0
#     for j in i:
#         if j in 'aeiou':
#             n_vogais += 1
#     print(f'A palavra {i} tem {n_vogais}')

conta_vogal = []

# for i in frutas:
#     n_vogais = 0
#     for j in i:
#         if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
#             n_vogais += 1
#     print(f'A palavra "{i}" tem {n_vogais}.')
#     conta_vogal.append(n_vogais)

# print(conta_vogal)    

for i in frutas:
    n_vogais = 0
    if i[0] in 'aeiou':
            print(f'A palavra {i} começa com uma vogal')
    for j in i:
        
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            n_vogais += 1
    print(f'A palavra "{i}" tem {n_vogais}.')
