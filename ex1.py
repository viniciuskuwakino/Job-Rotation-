class Soma:
    def __init__(self):
        self.indice = 13
        self.soma = 0
        self.k = 0

    def run(self):
        while self.k < self.indice:
            self.k = self.k + 1
            self.soma = self.soma + self.k

    def imprime(self):
        print(self.soma)


if __name__ == '__main__':
    soma = Soma()
    soma.run()
    soma.imprime()
