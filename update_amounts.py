# %%
import pprint

# Put old amounts here
AMOUNTS = {
    "Base": {
        "B": 76700,
        "C": 85200,
        "D": 93700,
        "E": 102200
    },
    "EAM": {
        "B": 4500,
        "C": 5000,
        "D": 5500,
        "E": 6000
    },
    "PM1": {
        "B": 13410,
        "C": 14900,
        "D": 16390,
        "E": 17880
        },
    "PM2": {
        "B": 9000,
        "C": 10000,
        "D": 11000,
        "E": 12000
        }
}

# Put multiplier here
mult = 1.043

amounts_new = {}
for k, v in AMOUNTS.items():
    amounts_new[k] = {}
    for k2, v2 in v.items():
        # Apply multiplier and round to nearest 10
        amounts_new[k][k2] = round(v2 * mult / 10) * 10

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(amounts_new)