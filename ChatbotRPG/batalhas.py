import random
import enemys
import time
from defs import calc_block, atacar, mostrar_inventario, menu_equipar_arma, dialogo, ganhar_xp, fugir, esquiva



def executar_batalha(player):
    turno = "player"

    if player["arma"] is None:
        print("Você está sem arma")
        menu_equipar_arma(player, player["inventario"])

    while True:

        # ================= TURNO DO PLAYER =================
        if turno == "player":
            bloqueando = False
            
            
            print()

            for i, slime in enumerate(enemys.slimes):
                print(f"{slime['nome']} {i+1} | nivel {slime['nivel']} | vida {slime['vida']}")

            print("\n(1) atacar | (2) trocar arma | (3) bloquear | (4) dialogo | (5) fugir")
            escolha = input("Selecione sua ação:\n")


            if escolha == "2":
                menu_equipar_arma(player, player["inventario"])
                continue



            
            if escolha == "3":
                bloqueando = True
                print("voce esta em posicao de bloqueio")
                turno = "inimigos"
                continue
            
            
            
            
            
            if escolha == "4":
                sucesso = dialogo(player)
                
                if sucesso:
                    print("os inimigos recuaram")
                    ganhar_xp(player, 15)
                    enemys.slimes.clear()
                    return player
                
                print("voce nao sabe conversar com slimes")
                turno = "inimigos"
                continue            
            
            
            
            
            if escolha == "5":
                sucesso = fugir(player, enemys.slimes)
                
                if sucesso:
                    return player
            
                turno = "inimigos"
                continue
                    
            
            
            

            escolha_alvo = int(input("Escolha seu alvo:\n"))
            alvo = enemys.slimes[escolha_alvo - 1]

            if escolha == "1":
                ataque = atacar(player, alvo)

                if ataque:
                    print(f"{alvo['nome']} morreu!")
                    enemys.slimes.remove(alvo)

                    if not enemys.slimes:
                        print("Você ganhou!")
                        player["dialogo_tentativas"] = 0
                        return player


            turno = "inimigos"

        # ================= TURNO DOS INIMIGOS =================
        elif turno == "inimigos":
            print("\nturno inimigo:\n")
            time.sleep(1)

            slime = random.choice(enemys.slimes)
            indice = enemys.slimes.index(slime)

            dano = random.randint(slime["dano_min"], slime["dano_max"])
            
            if esquiva(player["stats"]["destreza"], slime["nivel"]):
                dano = 0
            
            
            if bloqueando:
                chance = calc_block(player["nivel"], slime["nivel"])
                roll = random.randint(1,100)
                
                if roll <= chance:
                    print("voce bloqueou o ataque inimigo")
                    dano = 0
                else:
                    print("voce falhou em bloquear")

                bloqueando = False
            
            player["vida"] -= dano

            if dano > 0:
                print(f"{slime['nome']} {indice + 1} te causou {dano} de dano")

            if player["vida"] <= 0:
                print("voce morreu")
                return player

            print(f"sua vida atual: {player['vida']}")
            time.sleep(1)

            turno = "player"

