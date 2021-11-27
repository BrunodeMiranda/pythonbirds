class Pessoa:
    olhos = 2

    def __init__(self, *filhos,  nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhhos {cls.olhos}'


if __name__ == '__main__':
    bruno = Pessoa(nome = 'Bruno')
    antonio = Pessoa( bruno, nome = 'Antonio')
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
    antonio.sobreonome = 'Brandão'
    del antonio.filhos
    antonio.olhos= 1
    del antonio.olhos
    print(antonio.__dict__)
    print(bruno.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(bruno.olhos)
    print(antonio.olhos)
    print(id(Pessoa.olhos), id(bruno.olhos), id(antonio.olhos))
    print(Pessoa.metodo_estatico(), antonio.metodo_estatico(), bruno.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), antonio.nome_e_atributos_de_classe())