class Carro:

    class Motor:
        def __init__(self, velocidade):
            self.velocidade = velocidade

        def acelerar(self):
            self.velocidade += 1

        def frear(self):
            self.velocidade -= 2



    class Direcao:
        def __init__(self, dir = 'Norte'):
            self.dir = dir

        def girar_a_direita(self):
            if self.dir == 'Norte':
                self.dir = 'Leste'
            elif self.dir == 'Leste':
                self.dir = 'Sul'
            elif self.dir == 'Sul':
                self.dir = 'Oeste'
            else:
                self.dir = 'Norte'

        def girar_a_esquerda(self):
            if self.dir == 'Norte':
                self.dir = 'Oeste'
            elif self.dir == 'Oeste':
                self.dir = 'Sul'
            elif self.dir == 'Sul':
                self.dir = 'Leste'
            else:
                self.dir = 'Norte'






motor = Motor()
