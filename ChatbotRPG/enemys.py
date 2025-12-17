import random
from defs import calc_vida

def criar_slime(nivel=None):
    if nivel is None:
        nivel = random.randint(1, 5)

    return {
        "nome": "Slime",
        "nivel": nivel,
        "vida": calc_vida(nivel),
        "dano_min": 2 + nivel,
        "dano_max": 4 + nivel * 2
    }

slimes = [
    criar_slime(),
    criar_slime(),
    criar_slime()
]
