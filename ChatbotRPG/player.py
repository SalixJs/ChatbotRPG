from armas import criar_madeira

def criar_player(nome):
    return {
        "nome": nome,              
        "vida": 100,
        "vida_max": 100,
        "nivel": 1,
        "xp": 0,
        "xp_max": 100,

        "arma": criar_madeira(),

        "stats": {
            "forca": 5, # dano físico corpo a corpo
            "destreza": 5,  # chance de acerto, esquiva e crítico
            "constituicao": 5,  # vida máxima e resistência 
            "inteligencia": 5,  # habilidades especiais / diálogo técnico   SABER
            "sabedoria": 5, # percepção, decisões em diálogo, status    ENTENDER
            "carisma": 5    # diálogo, intimidação, persuasão   CONVENCER
        },

        "inventario": {
            "slot1": None,
            "slot2": None,
            "slot3": None
        }
    }

