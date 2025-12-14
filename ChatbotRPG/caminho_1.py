import random

from defs import calc_vida
from defs import calc_block

from player import player

import enemys

import batalhas


def executar_caminho1(player):
    print("\nvc encontra 3 slimes\n")
    print(
        "(1)passar escondido | (2)correr e dar a volta | (3)enfrentar eles | (4)observar eles"
    )
    c1p1 = input("oq vc faz?\n")
    if c1p1 == "1":

        print("vc tenta passar escondindo mas vc acaba sendo visto\n")
        player = batalhas.executar_batalha(player)

    return player
