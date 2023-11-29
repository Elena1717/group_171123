cities = (
    "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$".title()
    .strip("6..58")
    .strip("74$:?$")
    .split()
)

for city in range(len(cities)):
    print(f"Я " + "\u2764 " + cities[city])
