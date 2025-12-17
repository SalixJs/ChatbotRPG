import random


def criar_madeira():
    nivel = random.choice([0,1])
    
    arma = {
        "nome": "pedaco de madeira",
        "nivel": nivel,
        "dano_base": 3 + nivel,
        "crit_chance": 0.05 + (nivel * 0.05),
        "crit_mult": 1.5,
        "durabilidade": 20 + (nivel * 5)
    }
    
    return arma