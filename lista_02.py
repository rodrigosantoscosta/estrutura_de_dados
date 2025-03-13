# Questão 1
# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
# “calcular_area” que retorna a área do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * (self.raio ** 2)
    
teste = Circulo(5)
print(teste.calcular_area())


# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return (f'*Informações do livro*\nTitulo: "{self.titulo}"\nAutor: {self.autor}')

teste2 = Livro("Grande Sertão: Veredas", "Guimarães Rosa")
print(teste2.detalhes())

# 3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
# chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def __init__(self, base, altura):
        self.largura = base
        self.altura = altura

    def calcular_area(base, altura):
        return  base * altura 
    
    def calcular_perimetro(base, altura):
        return 2 * (base + altura)
# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
    
    def sacar(self, saque):
        self.saldo = self.saldo - saque

teste4 = ContaBancaria(500, "Entoni")
print(f"Titular: {teste4.titular}\nSaldo atual: {teste4.saldo}")
teste4.depositar(50)
print(f"Saldo após deposito: {teste4.saldo}")
teste4.sacar(50)
print(f"Saldo após saque: {teste4.saldo}")

# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
# chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"O nome da pessoa é {self.nome}")
    
teste5 = Pessoa("Entoni", 23)
teste5.falar()

# 6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return (self.preco) * (self.quantidade)

teste6 = Produto("Coca-Cola lata 350mL", 5, 5)
print(f"{teste6.quantidade} - {teste6.nome}\nValor total: R$ {(teste6.calcular_total()):.2f}")

# 7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return (f"- Informações do carro -\n\tMarca: {self.marca}\n\tModelo: {self.modelo}\n\tAno: {self.ano}")
teste7 = Carro("Fiat", "Uno", "1995")
print(teste7.detalhes())

# 8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
# “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
notas = [7,7]

teste7 = Aluno("Entoni", notas)
print(f"Aluno: {teste7.nome}\nMédia: {(teste7.calcular_media()):.2f}")
