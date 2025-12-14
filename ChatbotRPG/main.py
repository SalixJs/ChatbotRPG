import random
from defs import calc_vida
from defs import calc_block

from player import player

import caminho_1

pc1 = "Caminho 1: facil com recompensas pequenas"
pc2 = "Caminho 2: mediano com recompensas pequenas e grandes"
pc3 = "Caminho 3: dificil com recompensas grandes "
c1 = "caminho 1"
c2 = "caminho 2"
c3 = "caminho 3"
while True:
    # vida do player +20 por nivel
    
    player = input("Digite seu nome de jogador:\n")

    print("\nvc acorda no meio do nada nivel 1 com apenas um pedaço de madeira")
    print("olhando para frente voce ve 3 caminhos\n")
    print(f"{pc1}")
    print(f"{pc2}")
    print(f"{pc3}\n")
    p1 = input("para qual deles vc vai?\n")

    if p1 == c1:
        player = caminho_1.executar_caminho1(player)

    if player.player("vida") <= 0:
        r = input("Tentar denovo? (s/n): ")
        if r.lower() != "s":
            break
