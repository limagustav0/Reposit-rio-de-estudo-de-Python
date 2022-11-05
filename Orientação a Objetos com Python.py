class animal():
    def __init__(self, cor, ambiente, tamanho, tipo):
        self.cor = cor,
        self.ambiente = ambiente,
        self.tamanho = tamanho,
        self.tipo = tipo

    def voar(self):
        print('voando')

    def nadar(self):
        print('nadar')

    def __str__(self):
        return f"{self.__class__.__name__} : {[f'{chave} = {valor}' for chave, valor in self.__dict__.items()]}"


class macaco(animal):
    def __init__(self,cor, ambiente, tamanho, tipo,escalar):
        self.escalar = escalar

        super().__init__(cor, ambiente, tamanho, tipo)

    def escalando(self):
        print(f"{'SIM' if self.escalar else 'nao'} estou escalando")

macaco1 = macaco('dourado','floresta','medio','mamifero',True)


class tilapia(animal):
    def __init__(self,nadar,cor, ambiente, tamanho, tipo):
        self.nadar = nadar

        super().__init__(cor, ambiente, tamanho, tipo)

    def nadar(self):
        print(f"{'Sim' if self.nadar else 'nao'} estou nadando")

t1 = tilapia(True,'branca','mar','pequeno','onivoro')

print(t1)




class tigre():
    pass