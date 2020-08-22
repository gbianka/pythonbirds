"""
    Exercício:

        Você deve criar uma classe carro que vai possuir
        dois atributos compostos por outras duas classes:

        Motor
        Direção
        O Motor terá a responsabilidade de controlar a velocidade.
        Ele oferece os seguintes atributos:

        Atributo de dado velocidade
        Método acelerar, que deverá incremetar a velocidade de uma unidade
        Método frear que deverá decrementar a velocidade em duas unidades

        A Direção terá a responsabilidade de controlar a direção. Ela oferece
        os seguintes atributos:

        Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
        Método girar_a_direita
        Método girar_a_esquerda

               N
            O     L
               S

        Exemplo:
            >>> # Testando motor
            >>> motor = Motor()
            >>> motor.velocidade
            0
            >>> motor.acelerar()
            >>> motor.velocidade
            1
            >>> motor.acelerar()
            >>> motor.velocidade
            2
            >>> motor.acelerar()
            >>> motor.velocidade
            3
            >>> motor.frear()
            >>> motor.velocidade
            1
            >>> motor.frear()
            >>> motor.velocidade
            0
            >>> # Testando Direcao
            >>> direcao = Direcao()
            >>> direcao.valor
            'Norte'
            >>> direcao.girar_a_direita()
            >>> direcao.valor
            'Leste'
            >>> direcao.girar_a_direita()
            >>> direcao.valor
            'Sul'
            >>> direcao.girar_a_direita()
            >>> direcao.valor
            'Oeste'
            >>> direcao.girar_a_direita()
            >>> direcao.valor
            'Norte'
            >>> direcao.girar_a_esquerda()
            >>> direcao.valor
            'Oeste'
            >>> direcao.girar_a_esquerda()
            >>> direcao.valor
            'Sul'
            >>> direcao.girar_a_esquerda()
            >>> direcao.valor
            'Leste'
            >>> direcao.girar_a_esquerda()
            >>> direcao.valor
            'Norte'
            >>> carro = Carro(direcao, motor)
            >>> carro.calcular_velocidade()
            0
            >>> carro.acelerar()
            >>> carro.calcular_velocidade()
            1
            >>> carro.acelerar()
            >>> carro.calcular_velocidade()
            2
            >>> carro.frear()
            >>> carro.calcular_velocidade()
            0
            >>> carro.calcular_direcao()
            'Norte'
            >>> carro.girar_a_direita()
            >>> carro.calcular_direcao()
            'Leste'
            >>> carro.girar_a_esquerda()
            >>> carro.calcular_direcao()
            'Norte'
            >>> carro.girar_a_esquerda()
            >>> carro.calcular_direcao()
            'Oeste'
"""


class Motor:
    """
        O Motor terá a responsabilidade de controlar a velocidade.
        Ele oferece os seguintes atributos:
            Atributo de dado velocidade
            Método acelerar, que deverá incremetar a velocidade de uma unidade
            Método frear que deverá decrementar a velocidade em duas unidades

    """

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        """
            Incrementa a velocidade de 1 unidade
        """
        self.velocidade = self.velocidade + 1

    def frear(self):
        """
            Decrementa a velocidade em 2 unidades
        """

        if self.velocidade == 1:
            self.velocidade = self.velocidade = 0
        else:
            self.velocidade = self.velocidade - 2


class Direcao:
    """
        A Direção terá a responsabilidade de controlar a direção. Ela oferece
        os seguintes atributos:
            Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
            Método girar_a_direita
            Método girar_a_esquerda

               N
            O     L
               S
    """

    N = 'Norte'
    S = 'Sul'
    L = 'Leste'
    O = 'Oeste'
    DIRECAO_OPTIONS = [
        (N, 'Norte'),
        (S, 'Sul'),
        (L, 'Leste'),
        (O, 'Oeste'),
    ]

    def __init__(self, valor=N):
        self.valor = valor

    def girar_a_direita(self):
        """
            Altera para uma direção à direita da atual
        """

        if self.valor == 'Norte':
            self.valor = self.L
        elif self.valor == 'Leste':
            self.valor = self.S
        elif self.valor == 'Sul':
            self.valor = self.O
        else:
            self.valor = self.N

    def girar_a_esquerda(self):
        """
            Altera para uma direção à esquerda da atual
        """

        if self.valor == 'Norte':
            self.valor = self.O
        elif self.valor == 'Oeste':
            self.valor = self.S
        elif self.valor == 'Sul':
            self.valor = self.L
        else:
            self.valor = self.N


class Carro:

    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        """
            Mostra a velocidade atual
            :return: int com a velocidade atual, que pode ser a inicial ou a que
            o carro está depois da aceleração ou frenagem
        """
        return self.motor.velocidade

    def calcular_direcao(self):
        """
            Mostra a direção atual
            :return: string com a nova direção
        """
        return self.direcao.valor


if __name__ == '__main__':

    # Testando motor
    motor = Motor()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)

    # Testando Direcao
    direcao = Direcao()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_direita()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    direcao.girar_a_esquerda()
    print(direcao.valor)

    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.calcular_direcao())

    carro.girar_a_direita()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())