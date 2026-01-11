# Pokémon Training Game
# Tracks minimum and maximum Pokémon power in linear time

powers = [3, 8, 9, 7]

mini, maxi = 0, 0

for power in powers:
    if mini == 0 and maxi == 0:
        mini, maxi = power, power
    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
    print(mini, maxi)