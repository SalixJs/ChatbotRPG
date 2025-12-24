import random
from defs import calc_vida, calc_dano




def criar_slime(nivel=None):
    if nivel is None:
        nivel = random.randint(1, 5)

    return {
        "nome": "Slime",
        "nivel": nivel,
        
        
        "stats": {
            "forca": 5, # dano físico corpo a corpo
            "destreza": 5,  # chance de acerto, esquiva e crítico
            "constituicao": 5,  # vida máxima e resistência 
            "inteligencia": 5,  # habilidades especiais / diálogo técnico   SABER
            "sabedoria": 5, # percepção, decisões em diálogo, status    ENTENDER
            "carisma": 0    # diálogo, intimidação, persuasão   CONVENCER
            

        },
        
        "vida_max": calc_vida(nivel), 
        "dano_base": calc_dano(nivel, ["stats"]["forca"]), 
        
        
    }

tipos_slime = {
    "comum": {
        "vida": criar_slime["vida_max"],
        "dano": criar_slime["dano_base"],
        "habilidade": "nenhuma"
    },
    "acido": {
        "vida": 80%,
        "dano": 90%,
        "habilidade":
            cada ataque tem 25% de chance de:
                reduzir 1 de durabilidade
                ou causar dano continuo baixo
    }
    "viscoso":
    "explosivo":
    "leve":
    "pesado":
}


slimes = [
    criar_slime(),
    criar_slime(),
    criar_slime()
]
