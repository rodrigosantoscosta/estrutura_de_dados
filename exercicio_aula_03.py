# 1 - Crie uma classe chamada Carro com um método acelerar() que imprime
# "O carro está acelerando!" e um método frear() que imprime "O carro
# está freando!".

class Carro:
    def __init__(self, nome):
        self.nome =  nome
    
    def acelerar():
        print("O carro está acelerando!")
    
    def frear():
        print("O carro está freando!")

# 2 - Crie uma classe chamada Pessoa com um método cumprimentar(nome)
# que imprime "Olá, [nome]!".

class Pessoa:
    def __init__(self, nome):
        self.nome = nome 

    def cumprimentar(nome): 
        print(f"Olá {nome}!")

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b 

    def divisao(self):
        return self.a / self.b

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

