#Lista de exercicios - 01 - Revisão

#Questão 1 - Faça um programa que calcule a média de três números inseridos pelo usuário.

nota1, nota2, nota3 = map(float, input('Digite as tres notas do aluno separadas por um espaço: ').split())
print(nota1, nota2, nota3)
#media = (nota1 + nota2 + nota3) / 3.0 
print(f'Média: {(nota1 + nota2 + nota3) / 3.0}')

#Questão 2 - Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

numero = int(input('Digite um numero inteiro para verificar se é par ou impar: '))

def verifica_par(numero):
    if numero % 2 == 0:
        return('É par')
    else:
        return ('É impar')
print(f'{verifica_par(numero)}')

#Questão 3 - Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

# numero = int(input('Digite um numero inteiro qualquer: '))

# for i 