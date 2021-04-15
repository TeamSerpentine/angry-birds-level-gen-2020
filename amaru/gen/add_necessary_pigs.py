from random import uniform

from amaru.utilities import constants


def add_necessary_pigs(number_pigs, final_pig_positions, complete_locations):
    while len(final_pig_positions) < number_pigs:
        test_position = [uniform(constants.level_width_min, constants.level_width_max), constants.absolute_ground]
        pig_width = constants.pig_size[0]
        pig_height = constants.pig_size[1]
        valid_pig = True
        for i in complete_locations:
            if (round((test_position[0] - pig_width / 2), 10) < round((i[1] + (constants.blocks[str(i[0])][0]) / 2),
                                                                      10) and
                    round((test_position[0] + pig_width / 2), 10) > round((i[1] - (constants.blocks[str(i[0])][0]) / 2),
                                                                          10) and
                    round((test_position[1] + pig_height / 2), 10) > round(
                        (i[2] - (constants.blocks[str(i[0])][1]) / 2), 10) and
                    round((test_position[1] - pig_height / 2), 10) < round(
                        (i[2] + (constants.blocks[str(i[0])][1]) / 2), 10)):
                valid_pig = False
        for i in final_pig_positions:
            if (round((test_position[0] - pig_width / 2), 10) < round((i[0] + (pig_width / 2)), 10) and
                    round((test_position[0] + pig_width / 2), 10) > round((i[0] - (pig_width / 2)), 10) and
                    round((test_position[1] + pig_height / 2), 10) > round((i[1] - (pig_height / 2)), 10) and
                    round((test_position[1] - pig_height / 2), 10) < round((i[1] + (pig_height / 2)), 10)):
                valid_pig = False
        if valid_pig == True:
            final_pig_positions.append(test_position)
    return final_pig_positions
