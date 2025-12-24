import random
from player import criar_player

#region ACOES DO PLAYER
def atacar(player, alvo):
    arma = player["arma"]
    if arma is None:
        print("Você está desarmado!")
        return False

    forca = player["stats"]["forca"]
    destreza = player["stats"]["destreza"]

    dano = arma["dano_base"] + int(forca * 0.4) + random.randint(0, 2)

    crit_chance = arma["crit_chance"] + (destreza * 0.01)
    crit_chance = min(0.5, crit_chance)

    if random.random() < crit_chance:
        dano = int(dano * arma["crit_mult"])
        print("CRÍTICO!")

    dano = max(1, dano)

    arma["durabilidade"] -= 1
    alvo["vida"] -= dano

    print(f"Você causou {dano} de dano com {arma['nome']}")

    if arma["durabilidade"] <= 0:
        print(f"{arma['nome']} quebrou!")
        player["arma"] = None

    return alvo["vida"] <= 0


def dialogo(player):
    tentativas = player.get("dialogo_tentativas", 0)

    carisma = player["stats"]["carisma"]
    inteligencia = player["stats"]["inteligencia"]
    sabedoria = player["stats"]["sabedoria"]

    chance = (
        5
        + (carisma * 3)
        + (inteligencia * 1.5)
        + (sabedoria * 2)
        - (tentativas * 10)
    )

    chance = max(2, min(50, int(chance)))

    roll = random.randint(1, 100)
    player["dialogo_tentativas"] = tentativas + 1

    if roll <= chance:
        print("Você conseguiu acalmar a situação.")
        return True

    print("O diálogo falhou.")
    return False


def fugir(player, inimigos):
    nivel_inimigos = sum(i["nivel"] for i in inimigos) / len(inimigos)
    diferenca = player["nivel"] - nivel_inimigos

    destreza = player["stats"]["destreza"]

    chance = 30 + (destreza * 4) + (diferenca * 3)
    chance = max(5, min(90, int(chance)))

    roll = random.randint(1, 100)

    if roll <= chance:
        print("Você conseguiu fugir da batalha!")
        return True

    print("Os inimigos não te deixaram fugir.")
    return False


def calc_block(p_nivel, i_nivel, player):
    diferenca = p_nivel - i_nivel
    constituicao = player["stats"]["constituicao"]

    chance = 15 + (diferenca * 5) + (constituicao * 2)
    return max(5, min(65, chance))


def equipar_arma(player, inventario, slot):
    nova_arma = inventario[slot]

    if nova_arma is None:
        print("Espaço vazio")
        return

    inventario[slot] = player["arma"]
    player["arma"] = nova_arma

    print(f"Você equipou {nova_arma['nome']}")



def desequipar_arma(player, inventario):
    if player["arma"] is None:
        print("Você não tem arma equipada.")
        return

    for slot in inventario:
        if inventario[slot] is None:
            arma = player["arma"]
            inventario[slot] = arma
            player["arma"] = None

            slot_num = slot.replace("slot", "")
            print(f"Você guardou {arma['nome']} no espaço {slot_num}")
            return

    print("Inventário cheio!")


#endregion




#region COISAS DO PLAYER

#region XP
    


def atualizar_status(player):
    c = player["stats"]["constituicao"]
    player["vida_max"] = 50 + (c * 10)

    if player["vida"] > player["vida_max"]:
        player["vida"] = player["vida_max"]



def distribuir_pontos(player):
    pontos = 3

    while pontos > 0:
        print("\nEscolha um atributo para upar:")
        for stat, valor in player["stats"].items():
            print(f"{stat}: {valor}")

        escolha = input("> ").lower()

        if escolha in player["stats"]:
            player["stats"][escolha] += 1
            pontos -= 1
        else:
            print("Atributo inválido")




def subir_nivel(player):
    player["xp"] -= player["xp_max"]
    player["nivel"] += 1
    player["xp_max"] = int(player["xp_max"] * 1.35 + 20)

    print(f"\n vocesubiu para o nível {player['nivel']}!")

    distribuir_pontos(player)
    atualizar_status(player)




def ganhar_xp(player, quantidade):
    player["xp"] += quantidade

    while player["xp"] >= player["xp_max"]:
        subir_nivel(player)




#endregion

#region MENUS


def mostrar_xp(player):
    total = 20
    cheio = int((player["xp"] / player["xp_max"]) * total)
    barra = "█" * cheio + "-" * (total - cheio)

    print(f"XP [{barra}] {player['xp']}/{player['xp_max']}")


def mostrar_inventario(inventario):
    print("\n=== INVENTÁRIO ===")

    for slot, item in inventario.items():
        slot_nome = slot.replace("slot", "Espaço ")

        if item is None:
            print(f"{slot_nome}: [vazio]")
        else:
            print(
                f"{slot_nome}: {item['nome']} "
                f"(Nv {item['nivel']}) | "
                f"Dano {item['dano_base']} | "
                f"Dur {item['durabilidade']}"
            )

    print("==================\n")




def menu_equipar_arma(player, inventario):
    mostrar_inventario(inventario)
    
    escolha = input("Escolha o slot (1/2/3) ou 0 para cancelar:\n")

    if escolha == "0":
        return
    
    slot = f"slot{escolha}"
    
    if slot not in inventario:
        print("Slot inválido")
        return
    
    if inventario[slot] is None:
        print("Esse slot está vazio!")
        return

    equipar_arma(player, inventario, slot)




#endregion

#endregion




def esquiva(destreza, nivel_inimigo):
    chance = 10 + (destreza * 2) - (nivel_inimigo * 1.5)
    chance = max(5, min(90, chance))
    
    roll = random.randint(1,100)
    
    if roll <= chance:
        print("voce esquivou")
        return True
    
    return False

def calc_vida(nivel):
    return 20 + (nivel - 1) * 4


def calc_dano(nivel, forca):
    return 2 + (nivel * 1) + (forca * 0.5)

def calc_esquiva(destreza, nivel_player):
    chance = 5 + (destreza * 1) - (nivel_player * 1)
    chance = max(5, min(90,  chance))

    roll = random.randint(1,100)
    
    if roll <= chance:
        print("inimigo esquivou")
        return True

    return False





















