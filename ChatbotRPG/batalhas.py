import random
import enemys
import time
from defs import calc_block
from defs import atacar
from defs import mostrar_inventario
from defs import menu_equipar_arma
from player import inv_player 


def executar_batalha(player):
    turno = "player"

    if player["arma"] is None:
        print("Você está sem arma")
        menu_equipar_arma(player, inv_player)

    while True:

        # ================= TURNO DO PLAYER =================
        if turno == "player":
            print()

            for i, slime in enumerate(enemys.slimes):
                print(f"{slime['nome']} {i+1} | nivel {slime['nivel']} | vida {slime['vida']}")

            print("\n(1) atacar | (2) trocar arma | (3) bloquear | (4) dialogo | (5) fugir")
            escolha = input("Selecione sua ação:\n")

            if escolha == "2":
                menu_equipar_arma(player, inv_player)
                continue

            if escolha == "5":
                print("Você fugiu!")
                return player

            escolha_alvo = int(input("Escolha seu alvo:\n"))
            alvo = enemys.slimes[escolha_alvo - 1]

            if escolha == "1":
                ataque = atacar(player, alvo)

                if ataque:
                    print(f"{alvo['nome']} morreu!")
                    enemys.slimes.remove(alvo)

                    if not enemys.slimes:
                        print("Você ganhou!")
                        return player

            turno = "inimigos"

        # ================= TURNO DOS INIMIGOS =================
        elif turno == "inimigos":
            print("\nturno inimigo:\n")
            time.sleep(1)

            slime = random.choice(enemys.slimes)
            indice = enemys.slimes.index(slime)

            dano = random.randint(slime["dano_min"], slime["dano_max"])
            player["vida"] -= dano

            print(f"{slime['nome']} {indice + 1} te causou {dano} de dano")

            if player["vida"] <= 0:
                print("voce morreu")
                return player

            print(f"sua vida atual: {player['vida']}")
            time.sleep(1)

            turno = "player"

