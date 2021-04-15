from math import ceil


def choose_number_birds(final_pig_positions, number_ground_structures, number_platforms):
    number_birds = int(ceil(len(final_pig_positions) / 2))
    if (number_ground_structures + number_platforms) >= number_birds:
        number_birds = number_birds + 1
    number_birds = number_birds + 1  # adjust based on desired difficulty
    return number_birds
