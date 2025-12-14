def calc_vida(nivel):
    return 20 + (nivel - 1) * 4


def calc_block(p_nivel, i_nivel):
    diferenca = p_nivel - i_nivel
    chance = 50 + (diferenca * 10)
    chance = max(5, min(95, chance))
    return chance
