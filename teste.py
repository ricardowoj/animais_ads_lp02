

class Reptil:

    # Atributos
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    # Métodos   
    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)

class Camaleao(Reptil):
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

camaleaoGenerico = Camaleao('bob', 'azul', 3, 'mosquito')
print(camaleaoGenerico.comer_inseto)

class Cobra(Reptil, Camaleao):
    def __init__(self, nome, cor, idade, inseto_favorito, veneno):
        super().__init__(nome, cor, idade, inseto_favorito, veneno)
        self.veneno = veneno
    
    def rastejar(self):
        return '{} rastejando !'.format(self.nome)
    
    def trocar_pele(self): 
        return '{} está trocando de pele !'.format(self.nome)


cobraGenerica = Cobra('Ana', 'Coral', 3, False)
print(cobraGenerica.cor)
print('É venenosa?' , cobraGenerica.veneno)
print(cobraGenerica.tomar_sol())
print(cobraGenerica.tomar_sol())