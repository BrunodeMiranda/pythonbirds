class Pessoa:
    def __init__(self, *filhos,  nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    bruno = Pessoa(nome = 'Bruno')
    antonio = Pessoa( bruno, nome = 'Antonio')
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
