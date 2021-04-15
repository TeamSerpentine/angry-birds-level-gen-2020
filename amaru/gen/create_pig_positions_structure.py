from random import randint

from amaru.gen.pig_position_locator import pig_position_locator


def create_pig_positions_structure(complete_locations, final_pig_positions=None):
    pig_width, pig_height, possible_pig_positions = pig_position_locator(complete_locations)

    if final_pig_positions is None:
        final_pig_positions = []

    while len(possible_pig_positions) > 0:
        pig_choice = possible_pig_positions.pop(
            randint(1, len(possible_pig_positions)) - 1
        )
        final_pig_positions.append(pig_choice)
        new_pig_positions = []
        for i in possible_pig_positions:
            if (
                    round((pig_choice[0] - pig_width / 2), 10)
                    >= round((i[0] + pig_width / 2), 10)
                    or round((pig_choice[0] + pig_width / 2), 10)
                    <= round((i[0] - pig_width / 2), 10)
                    or round((pig_choice[1] + pig_height / 2), 10)
                    <= round((i[1] - pig_height / 2), 10)
                    or round((pig_choice[1] - pig_height / 2), 10)
                    >= round((i[1] + pig_height / 2), 10)
            ):
                new_pig_positions.append(i)
        possible_pig_positions = new_pig_positions
    return final_pig_positions
