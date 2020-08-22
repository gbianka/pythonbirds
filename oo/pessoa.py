class Pessoa:

    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    bianka = Pessoa(nome='Bianka')
    maria = Pessoa(bianka, nome='Maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)
    maria.sobrenome = 'Teles'   # atribuito dinâmico apenas para o objeto maria.
    del maria.filhos            # removendo dinamicamente um atributo
    print(maria.__dict__)       # __dict__ retorna todos os atributos de instância do objeto, inclusive os dinâmicos
    print(bianka.__dict__)


