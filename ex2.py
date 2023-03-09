class Fibonacci:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def fib(n):
        f = [0, 1]

        for i in range(2, n + 2):
            if n >= f[i-1]:
                f.append(f[i-1] + f[i-2])
            else:
                break

        return f

    def imprime(self):
        number = self.num
        arr = self.fib(number)

        if number in arr:
            print("O numero informado pertence!")
        else:
            print("O numero informado nao pertence!")


if __name__ == '__main__':
    n = int(input('Informe um numero: '))
    fibo = Fibonacci(n)
    fibo.imprime()
