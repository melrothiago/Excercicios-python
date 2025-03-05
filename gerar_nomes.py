"""Script para gerar combinações aleatórias de nomes.

Este programa cria nomes aleatórios combinando elementos de duas listas
e permite ao usuário gerar novos nomes continuamente até optar por sair.
"""

import sys
import random


def main():
    """Função principal para gerar combinações aleatórias de nomes."""

    # Título do programa
    print("GERADOR DE NOMES")

    # Listas de nomes
    nomes1 = (
        'Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
        '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
        'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
        'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
        "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms', 'Barcho', 'Zergto', 'Thini', 'Phasha',
        'Yentappay', 'Nemushang', 'Morlusxa', 'Gudmoran', 'Zacthe', 'Casnor',
        'Ga', 'Ca', "Anvi'drag", 'Ulfroth', 'Zethild', 'Laruul', 'Ne', 'Cusard',
        'Le', 'Rielzorg'
    )

    nomes2 = (
        'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks', 'Zaron', 'Rothgo', 'Gluibra', 'Lhurho', "Gofhtak'n",
        'Ctu', 'Migoth', 'Chthuron', "Miph'n", 'Thothsog', 'Nema', 'Has',
        'Abmglw', "Guaph'n", 'Goggu', 'Mako', "Mitlaglnx'o", 'Teplo', 'Xuthoth',
        'Nacquahsha'
    )

    # Loop principal
    while True:
        primeiro_nome = random.choice(nomes1)
        sobrenome = random.choice(nomes2)

        print("\n\n")
        print(f"{primeiro_nome} {sobrenome}", file=sys.stderr)
        print("\n\n")

        continuar = input("Deseja continuar? Pressione Enter para continuar ou 'n' para sair: ")
        if continuar.lower() == "n":
            print("\n\nPrograma encerrado. Até a próxima!")
            break


if __name__ == "__main__":
    main()
