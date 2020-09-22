class Pessoa:
    """"""
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=46):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 46

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    leonardo = Pessoa(nome='Leonardo')
    luciano = Pessoa(leonardo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    del luciano.sobrenome
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(leonardo.__dict__)
    print('Olhos de Pessoa: ' + str(Pessoa.olhos))
    print('Olhos de Luciano: ' + str(luciano.olhos))
    print('Olhos de Leonardo: ' + str(leonardo.olhos))
    print(id(Pessoa.olhos), id(luciano.olhos), id(leonardo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())
