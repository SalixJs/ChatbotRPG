import random
import enemys
from defs import calc_block
from acoes import acoes
from acoes import alvo
from player import player
from acoes import atacar



def executar_batalha(batalha):
    for i, slime in enumerate(enemys.slimes):
        print(f"{slime["nome"]} {i+1} | nivel {slime["nivel"]} | vida {slime["vida"]}")
    print("(1)atacar | (2)bloqueio | (3)Usar o poder da amizade(dialogo) | (4)Fugir ")
    escolha = input("Selecione sua acao:\n")
    
    
    
    for i, slime in enumerate(enemys.slimes):
        print(f"{slime["nome"]} {i+1} | nivel {slime["nivel"]} | vida {slime["vida"]}")
    escolha_alvo = int(input("escolha seu alvo (1,2,3)\n"))
    alvo = enemys.slimes[escolha_alvo - 1]

    if escolha == "1":
        atacar(player, alvo)
        




















