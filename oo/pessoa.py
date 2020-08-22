class Pessoa:
    olhos = 2

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
    bianka.olhos = 1
    del bianka.olhos
    print(maria.__dict__)       # __dict__ retorna todos os atributos de instância do objeto, inclusive os dinâmicos
    print(bianka.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)         # só dá para acessar assim pq olhos é um atributo de classe
    print(maria.olhos)          # outra forma de acessar o atributo de classe é por um objeto do tipo Pessoa
    print(bianka.olhos)         # outra forma de acessar o atributo de classe é por um objeto do tipo Pessoa
    print(id(Pessoa.olhos), id(maria.olhos), id(bianka.olhos))    # o id do objeto é o mesmo




