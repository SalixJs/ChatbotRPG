import random
from player import inv_player
from player import player

def calc_vida(nivel):
    return 20 + (nivel - 1) * 4


def calc_block(p_nivel, i_nivel):
    diferenca = p_nivel - i_nivel
    chance = 50 + (diferenca * 10)
    chance = max(5, min(95, chance))
    return chance


def atacar(player, alvo):
    arma = player["arma"]

    if arma is None:
        print("Você está desarmado!")
        return False

    dano = arma["dano_base"] + random.randint(0, 3)

    if random.random() < arma["crit_chance"]:
        bonus = int(arma["dano_base"] * (arma["crit_mult"] - 1))
        dano += bonus
        print("CRÍTICO!")

    arma["durabilidade"] -= 1
    alvo["vida"] -= dano

    print(f"Você causou {dano} de dano com {arma['nome']}")

    if arma["durabilidade"] <= 0:
        print(f"{arma['nome']} quebrou!")
        player["arma"] = None

    return alvo["vida"] <= 0


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


def equipar_arma(player, inventario, slot):
    arma_atual = player["arma"]
    nova_arma = inventario[slot]
    
    if nova_arma is None:
        print("espaço vazio")
        return

    inventario[slot] = arma_atual
    player["arma"] = nova_arma

    print(f"voce equipou {nova_arma["nome"]}")


def desequipar_arma(player, inventario):
    if player["arma"] is None:
        print("Você não tem arma equipada.")
        return

    for slot in inventario:
        if inventario[slot] is None:
            nome_arma = player["arma"]["nome"]

            inventario[slot] = player["arma"]
            player["arma"] = None

            slot_num = slot.replace("slot", "")  # slot1 -> 1
            print(f"Você guardou {nome_arma} no espaço {slot_num}\n")
            return

    print("Inventário cheio!")


def menu_equipar_arma(player, inventario):
    mostrar_inventario(inventario)
    
    escolha = input("escolha o slot da arma para equipar (1/2/3) ou 0 para cancelar: \n")

    if escolha == 0:
        return
    
    slot = f"slot{escolha}"
    
    if slot not in inventario:
        print("slot invalido")
        return
    
    if inventario[slot] is None:
        print("esse slot esta vazio!")
        return

    equipar_arma(player, inventario, slot)







