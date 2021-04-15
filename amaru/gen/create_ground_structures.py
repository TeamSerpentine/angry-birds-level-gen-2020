from random import uniform

from amaru.gen.make_structure import make_structure
from amaru.utilities import constants


def create_ground_structures(number_ground_structures):
    valid = False
    while valid == False:
        ground_divides = []
        if number_ground_structures > 0:
            ground_divides = [constants.level_width_min, constants.level_width_max]
        for i in range(number_ground_structures - 1):
            ground_divides.insert(i + 1, uniform(constants.level_width_min, constants.level_width_max))
        valid = True
        for j in range(len(ground_divides) - 1):
            if (ground_divides[j + 1] - ground_divides[j]) < constants.min_ground_width:
                valid = False

    # determine the area available to each ground structure
    ground_positions = []
    ground_widths = []
    for j in range(len(ground_divides) - 1):
        ground_positions.append(ground_divides[j] + ((ground_divides[j + 1] - ground_divides[j]) / 2))
        ground_widths.append(ground_divides[j + 1] - ground_divides[j])

    print("number ground structures:", len(ground_positions))
    print("")

    # creates a ground structure for each defined area
    complete_locations = []
    final_pig_positions = []
    for i in range(len(ground_positions)):
        max_width = ground_widths[i]
        max_height = constants.ground_structure_height_limit
        center_point = ground_positions[i]
        complete_locations2, final_pig_positions2 = make_structure(constants.absolute_ground, center_point, max_width,
                                                                   max_height)
        complete_locations = complete_locations + complete_locations2
        final_pig_positions = final_pig_positions + final_pig_positions2

    return len(ground_positions), complete_locations, final_pig_positions
