from copy import deepcopy
from random import randint, shuffle

from amaru.gen.choose_structure import choose_structure
from amaru.gen.create_pig_positions_structure import create_pig_positions_structure
from amaru.gen.create_platforms import create_platforms
from amaru.level_structures import structure_windmill, \
    structure_tank, structure_ship, structure_car, structure_train_front, \
    structure_train_wagon, structure_square_pyramid, structure_triangle_pyramid, structure_dinner_small
from amaru.utilities import constants
from amaru.utilities.write_level_xml import write_level_xml

if __name__ == "__main__":

    structure_list = [
        structure_dinner_small.make_dinner_small,
        structure_square_pyramid.make_square_pyramid,
        structure_train_front.make_train_front,
        structure_train_wagon.make_train_wagon,
        structure_car.create_structure_car,
        structure_tank.create_structure_tank,
        structure_windmill.make_windmill,
        structure_triangle_pyramid.make_triangle_pyramid,
        structure_ship.make_structure_ship
    ]
    nr_structures_we_have = len(structure_list)

    all_ground_widths = [
        (1.30 + constants.blocks['8'][0] / 2) * 2,  # dinner
        constants.additional_object_sizes['2'][0] * 2 + (5 * 2 - 1) * constants.blocks['1'][0],  # square pyramid
        4 * constants.additional_object_sizes['3'][0] - 0.8 * constants.additional_object_sizes['3'][0],  # train front
        1.8 * constants.additional_object_sizes['3'][0],  # train wagon
        constants.blocks['12'][0] + 0.1,  # car
        3.2 * constants.blocks['16'][0],  # tank
        constants.blocks['1'][0] + constants.blocks['3'][0] * 2,  # windmill
        (3 + 2) * 1.5 * constants.additional_object_sizes['2'][0],  # triangle pyramid
        24 * 0.44  # ship
    ]

    backup_probability_table_blocks = deepcopy(constants.probability_table_blocks)
    backup_materials = deepcopy(constants.materials)

    FILE = open("parameters.txt", 'r')
    checker = FILE.readline()
    finished_levels = 0
    while (checker != ""):
        if checker == "\n":
            checker = FILE.readline()
        else:
            number_levels = int(deepcopy(checker))
            restricted_combinations = FILE.readline().split(',')
            for i in range(len(restricted_combinations)):
                restricted_combinations[i] = restricted_combinations[i].split()
            pig_range = FILE.readline().split(',')
            time_limit = int(FILE.readline())
            checker = FILE.readline()

            for current_level in range(number_levels):

                number_ground_structures = 1
                number_platforms = randint(1, 3)
                number_pigs = randint(int(pig_range[0]), int(
                    pig_range[1]))

                if (current_level + finished_levels + 4) < 10:
                    level_name = "0" + str(current_level + finished_levels + 4)
                else:
                    level_name = str(current_level + finished_levels + 4)

                all_indices = list(range(nr_structures_we_have))
                shuffle(all_indices)
                complete_locations, final_platforms, final_pig_positions, final_TNT_positions = choose_structure(
                    structure_list, all_indices.pop(0))
                for platf in range(3):
                    number_platforms, final_platforms, platform_centers, platform_widths, the_platforms = create_platforms(
                        1, complete_locations, final_pig_positions, final_platforms)
                    if number_platforms >= 1:
                        built_on_plat = False
                        for struc in range(len(all_indices)):
                            chosen = all_indices[struc]
                            if all_ground_widths[chosen] <= platform_widths[0]:
                                location = [platform_centers[0][0],
                                            platform_centers[0][1] + constants.platform_size[1] / 2]
                                complete_locations, final_platforms, final_pig_positions, final_TNT_positions = choose_structure(
                                    structure_list, 0, location, complete_locations, final_platforms,
                                    final_pig_positions, final_TNT_positions)
                                built_on_plat = True
                                all_indices.pop(struc)
                                break
                        if not built_on_plat:
                            plt = the_platforms[0]
                            final_platforms.remove(plt)

                selected_other = []
                number_birds = round(len(final_pig_positions) / 2) + round(len(complete_locations) / 15)
                if number_birds == 0:
                    number_birds = 1
                if number_birds > 5:
                    number_birds = 5

                final_pig_positions = create_pig_positions_structure(
                    complete_locations, final_pig_positions
                )

                write_level_xml(complete_locations, selected_other, final_pig_positions, final_TNT_positions,
                                final_platforms, number_birds, level_name, restricted_combinations,
                                nr_structures_we_have, structure_list)
            finished_levels = finished_levels + number_levels
