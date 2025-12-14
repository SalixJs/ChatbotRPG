import random
import enemys
import defs
import player
from batalhas import executar_batalha

# acoes (1)atacar | (2)Bloquear | (3)Esquivar | (4)Usar o poder da amizade(dialogo) | (5)Fugir





#ataque

def atacar(player, inimigo):
    dano = random.randint(5,13)
    alvo["vida"] -= dano
    print(f"voce causou {dano} de dano em {alvo["nome"]}")
    return atacar