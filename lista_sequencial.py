from random import randint

import numpy as np

class Listasequencial:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i,' - ',self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida...')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if (valor==self.valores[i]):
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1
# # # Criando uma lista de valores simples usando range()
# # lista_valores = list(range(10, 60, 10))
# # # Exibindo a lista
# # print("Lista de valores:", lista_valores)
# # # Criando uma lista com valores aleatórios


# # resposta=[]
# # for i in range(10):
# # resposta.append(randint(10,29))

# from random import randint
# # 1. Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista.

# lista = []
# for i in range(10):
#     lista.append(randint(0,100))

# maior = lista[i]
# tail = lista[len(lista) - 1 ]

# print(lista)
# for i in range(len(lista)):
#    tmp = i + 1
   
#    if tmp > len(lista):
#        break
   
#    next = lista[tmp]
   

#    if next == tail:
#        break
   
#    if next >= maior:
#         maior = next

# print(maior)

# # 2. Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.

# def insira(valor , posicao):
#     list
# lista_nomes = ["Pablo Santos Pereira da Silva", "Alexander", "Pedro", "Marcelo"]
# head = lista[0]

# for i in range (len(lista_nomes)):
#     tmp = i + 1

# 3. Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da
# lista.

lista_soma = []

for i in range(3):
    lista_soma.append(randint(0,100))

# tail = lista_soma[len(lista_soma) - 1 ]
soma = 0

for i in range(len(lista_soma)):
    tmp = i + 1
    if tmp > len(lista_soma):
       break
    
    soma += lista_soma[i]
print(lista_soma)
print(soma)
