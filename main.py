from personagem import Personagem
from dataclasses import dataclass

class main():
    while True:
        resposta=int(input("""  
        1 - Criar personagens (limitado a dois)\n
        2 - Combate\n
        3 - sair\n
        R:"""))
        if resposta == 1:
            nome1 = input('insira o nome do seu personagem: ')
            ataque1 = input('insira o nome do ataque do seu personagem: ')
            player1 = Personagem(nome1, ataque1)

            nome2 = input('insira o nome do seu personagem: ')
            ataque2 = input('insira o nome do ataque do seu personagem: ')
            player2 = Personagem(nome2, ataque2)

            print('persoangens criados! inicie um combate entre eles.\n')

        elif resposta == 2:
            while True:
                resp = int(input(f'''é a vez de {player1.nome}, o que fará?\n\n
                1 - Atacar \n
                2 - xingar\n
                3 - Humilhar\n
                4 - Sair\n
                R:'''))

                if resp == 1:
                    player1.ataca(player2)
                elif resp == 2:
                    player1.xinga(player2)
                elif resp == 3:
                    player1.humilha(player2)
                elif resp == 4:
                    print('Saindo da arena de combate...')
                    break
                else:
                    print('opção inválida\n')

                resp = int(input(f'''é a vez de {player2.nome}, o que fará?\n\n
                1 - Atacar \n
                2 - xingar\n
                3 - Humilhar\n
                4 - Sair\n
                R:'''))

                if resp == 1:
                    player2.ataca(player1)
                elif resp == 2:
                    player2.xinga(player1)
                elif resp == 3:
                    player2.humilha(player1)
                elif resp == 4:
                    print('Saindo da arena de combate...')
                    break
                else:
                    print('opção inválida\n')

        elif resposta == 3:
            print('Obrigado por jogar!')
            break
        else:
            print('erro desconhecido!')
            break

main()