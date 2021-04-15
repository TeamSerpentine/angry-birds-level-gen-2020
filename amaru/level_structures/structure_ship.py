from random import randint

from amaru.utilities import constants


def make_structure_ship(complete_locations=None, final_platforms=None, final_pig_positions=None,
                        final_TNT_positions=None, ground=-3.5, pos_x=4):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []
    # sea
    total_number_of_seablocks = 24
    shifting_value_y = 0.50 / 2
    for i in range(3):
        start_point = -(total_number_of_seablocks / 2 * constants.blocks['4'][1])
        for j in range(total_number_of_seablocks):
            complete_locations.append([4, pos_x + start_point, ground + shifting_value_y, "ice"])
            start_point += 0.46
        shifting_value_y += 0.50
        total_number_of_seablocks -= 2
        start_point += 0.44
    ground += constants.blocks['4'][1] * 3 + 0.2
    # ship build
    for shifting_value in range(-170, 170, 90):  # floor
        complete_locations.append([2, pos_x + (shifting_value / 100), ground + constants.blocks['2'][1] / 2, "wood"])
    complete_locations.append(
        [18, pos_x - (constants.blocks['17'][1] / 2 + 2.3), ground + constants.blocks['2'][1] / 2, "wood"])  # left
    complete_locations.append(
        [15, pos_x - (constants.blocks['17'][1] / 2 + 2.3), ground + constants.blocks['2'][1] / 2, "ice"])  # left
    for height_value in range(2):  # right hole squares
        complete_locations.append([1, pos_x + (constants.blocks['17'][1] / 2 + 1.65),
                                   ground + (constants.blocks['1'][1] / 2) + height_value * constants.blocks['1'][1],
                                   "wood"])  # right
    complete_locations.append([1, pos_x - 2 * constants.blocks['2'][1] - constants.blocks['1'][1] / 2 - 1.25,
                               ground + constants.blocks['17'][1] + (constants.blocks['17'][1] / 2) + 0.3, "wood"])
    # middle dock
    complete_locations.append(
        [12, pos_x - 1.09, ground + constants.blocks['2'][1] + (constants.blocks['12'][1] / 2), "wood"])  # bottom big
    complete_locations.append(
        [9, pos_x - 1.95, ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][1] / 2,
         "wood"])  # column left
    complete_locations.append(
        [9, pos_x - 0.125, ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][1] / 2,
         "wood"])  # column right
    complete_locations.append([12, pos_x - 1.0,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] / 2 + 0.5, "wood"])  # upper big
    complete_locations.append([13, pos_x - 0.65,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['13'][1] / 2 + 0.6,
                               "wood"])  # vert part 1
    complete_locations.append([10, pos_x - 0.65,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['13'][1] + constants.blocks['8'][
                                   1] / 2 + 0.6, "wood"])  # vert part 2
    complete_locations.append([9, pos_x - 0.65,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['13'][1] + constants.blocks['8'][
                                   1] + constants.blocks['9'][1] / 2 + 0.6, "wood"])  # vert part 3
    complete_locations.append([4, pos_x - 0.2,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['9'][1] / 2 + 0.3,
                               "stone"])  # right tiny
    complete_locations.append([4, pos_x - 1.0,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['9'][1] / 2 + 0.3,
                               "stone"])  # left tiny
    complete_locations.append([3, pos_x - 1.5,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['9'][1] / 2 + 0.3,
                               "stone"])  # fat left
    complete_locations.append([17, pos_x - 1.5,
                               ground + constants.blocks['2'][1] + constants.blocks['12'][1] + constants.blocks['9'][
                                   0] + constants.blocks['12'][1] + constants.blocks['9'][1] + constants.blocks['17'][
                                   1] / 2 + 0.5, "stone"])  # circ on top of fat
    complete_locations.append([17, pos_x - 2 * constants.blocks['2'][1] - constants.blocks['1'][1] / 2 - 1.5,
                               ground + constants.blocks['17'][1] + constants.blocks['17'][1] + constants.blocks['17'][
                                   1] / 2 + 0.7, "stone"])
    complete_locations.append([12, pos_x - 2 * constants.blocks['2'][1] - constants.blocks['1'][1] / 2 - 1.6,
                               ground + constants.blocks['15'][1] + constants.blocks['1'][1] + constants.blocks['17'][
                                   1], "wood", 150])  # canon
    complete_locations.append([17, pos_x - 2 * constants.blocks['2'][1] - constants.blocks['1'][1] / 2 - 0.5,
                               ground + constants.blocks['17'][1] + constants.blocks['17'][1] + constants.blocks['17'][
                                   1] / 2 + 0.9, "stone"])
    random = randint(0, 2)
    for i in range(2):
        if random == 0:
            final_TNT_positions.append([pos_x - 0.6, ground + constants.blocks['2'][1] + constants.blocks['12'][1] +
                                        constants.blocks['9'][1] / 2 - 0.1])
        elif random == 1:
            final_TNT_positions.append([pos_x + 1, ground + constants.blocks['2'][1] + constants.blocks['12'][1] - 0.1])
        else:
            final_TNT_positions.append([pos_x + (constants.blocks['17'][1] / 2 + 1.7),
                                        ground + (constants.blocks['1'][1] / 2) + 2 * constants.blocks['1'][1] - 0.1])
        random_next = randint(0, 2)
        if random_next == random:
            random = (random_next + 1) % 2
        else:
            random = random_next
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
