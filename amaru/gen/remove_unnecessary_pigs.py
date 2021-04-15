from random import randint


def remove_unnecessary_pigs(number_pigs, final_pig_positions):
    removed_pigs = []
    while len(final_pig_positions) > number_pigs:
        remove_pos = randint(0, len(final_pig_positions) - 1)
        removed_pigs.append(final_pig_positions[remove_pos])
        final_pig_positions.pop(remove_pos)
    return final_pig_positions, removed_pigs
