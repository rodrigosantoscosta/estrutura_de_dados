# # # #Lista de exercicios - 01 - Revisão

# # # #Questão 1 - Faça um programa que calcule a média de três números inseridos pelo usuário.

# # nota1, nota2, nota3 = map(float, input('Digite as tres notas do aluno separadas por um espaço: ').split())
# # print(nota1, nota2, nota3) 
# # print(f'Média: {((nota1 + nota2 + nota3) / 3.0):.2f}')

# # # #Questão 2 - Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

# # numero = int(input('Digite um numero inteiro para verificar se é par ou impar: '))
# # def verifica_par(numero):
# #     if numero % 2 == 0:
# #         return('É par')
# #     else:
# #          return ('É impar')
# # print(f'{verifica_par(numero)}')

# # #Questão 3 - Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

# # numero = int(input('Digite um numero inteiro qualquer: '))

# # for i in range (numero + 1):
# #     if i % 2 == 0:
# #         print(f'{i} ', end='')

# #4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.
# lista_de_numeros = []
# n_itens = int(input('Digite quantos números você quer na lista: '))

# for i in range(n_itens):
#     lista_de_numeros.append(float(input(f'Digite o número {i + 1} da lista: ' )))

# maior = lista_de_numeros[0]
# menor = lista_de_numeros[0]

# for numero in lista_de_numeros:
#     if numero > maior:
#         maior = numero
#     if numero < menor:
#         menor = numero
# print(f'O maior número é {maior}.')
# print(f'O menor número é {menor}.')

# lista_de_numeros = []
# n_itens = int(input('Digite quantos números você quer na lista: '))
# lista_pares = []

# for i in range(n_itens):
#     lista_de_numeros.append(int(input(f'Digite o número {i + 1} da lista: ' )))

# for numero in lista_de_numeros:
#     if numero % 2 == 0:
#         lista_pares.append(numero)
# print(f'A média dos número pares é igual a {sum(lista_pares)/n_itens}')

# numero = int(input('Digite um numero inteiro para calcular o seu fatorial: '))
# fatorial = 1

# for i in range (1, numero + 1):
#     fatorial = fatorial * i
# print(f' O fatorial de {numero} é igual a {(fatorial)}.')

# def calculaFibonaci(numero):
#     primeiroNumeroFibonaci = 0
#     segundoNumeroFibonaci = 1
#     proximoNumero = 1
    
#     for i in range (numero):
#         print(proximoNumero)
#         primeiroNumeroFibonaci = segundoNumeroFibonaci
#         segundoNumeroFibonaci = proximoNumero
#         proximoNumero = primeiroNumeroFibonaci + segundoNumeroFibonaci

# if __name__ == "__main__":
    
#     numero = int(input('Digite quantos numeros da sequencia de Fibonaci a serem exibidos: '))
#     calculaFibonaci(numero)

# def ehPrimo(numero):
#     if numero == 2:
#         return True
    
#     if numero == 3:
#         return True
    
#     if numero > 1 :
#         for i in range (1, numero + 1):
#             if numero % i == 0:
#                 if numero > i != numero and i != 1:
#                     return False
#             else:
#                 return True
#     else:
#         False

# if __name__ == '__main__':
#     numero = int(input('Digite um numero para verificar se é primo: '))

#     if ehPrimo(numero):
#         print('É primo')
#     else:
#         print('Não é primo')

def comeca_com_letra_A(lista_de_nomes):
    for nome in lista_de_nomes:
        if nome.startswith('A'):
            return True
          
if __name__ == "__main__":
    lista_de_nomes = []
    n_itens = int(input('Digite quantos nomes você quer na lista de nomes: '))
    lista_comeca_A = []
    for i in range (n_itens):
        lista_de_nomes.append(input(f'Digite o nome da posição {i + 1} da lista: '))
    
    for nome in lista_de_nomes:
        if comeca_com_letra_A(nome):
            lista_comeca_A.append(nome)

    
    print(f'Os nomes digitados que começam com "A" são: {lista_comeca_A}')