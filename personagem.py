from dataclasses import dataclass

@dataclass
class Personagem:
    nome: str
    golpe: str
    vida = 15000

    def diz_oi(self):
        print(f'Oi, eu sou o {self.nome}\n')

    def ataca(self, oponente):
        oponente.vida -= 500
        print(f'{self.nome} ataca {oponente.nome} com um {self.golpe}\n{oponente.nome} perde 500 pontos de vida! agora esta com {oponente.vida}\n')

    def xinga(self, oponente):
        self.vida += 250
        print(f'Ae {oponente.nome} vai toma no olho do teu cu viado, vai chupa um canavial de rola viado!\n{self.nome} recuperou 250 pontos de vida! agora esta com {self.vida}\n')

    def humilha(self, oponente):
        self.vida += 250
        print(f'Ae {oponente.nome} cê tem mó cara de crackudo, ta com a boca rachada de fumar lata fdp!\n{self.nome} recuperou 250 pontos de vida! e está com {self.vida}\n')
