import random
from defs import calc_vida


s1 = random.randint(1, 5)
s2 = random.randint(1, 5)
s3 = random.randint(1, 5)
s1_vida = calc_vida(s1)
s2_vida = calc_vida(s2)
s3_vida = calc_vida(s3)

slimes = [
    {"nome": "slime", "nivel": s1, "vida": s1_vida},
    {"nome": "slime", "nivel": s2, "vida": s2_vida},
    {"nome": "slime", "nivel": s3, "vida": s3_vida},
]


print(slimes)