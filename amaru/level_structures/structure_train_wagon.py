from amaru.utilities import constants


def make_train_wagon(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                     ground=-3.5, pos_x=3):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    circle_size = constants.additional_object_sizes['3'][0]
    rect_medium_length = constants.blocks['10'][0]
    rect_medium_height = constants.blocks['10'][1]
    two_length = constants.blocks['2'][0]
    three_height = constants.blocks['3'][1]
    left = pos_x - (1.75 * circle_size / 2)

    for i in range(2):
        complete_locations.append([16, left + 1.75 * i * circle_size, ground + circle_size / 2, "stone"])
    complete_locations.append([10, pos_x, ground + circle_size + constants.blocks['10'][1] / 2])
    complete_locations.append([7, pos_x - rect_medium_length / 2 + constants.blocks['7'][0] / 2,
                               ground + circle_size + rect_medium_height + constants.blocks['7'][1] / 2])
    complete_locations.append([7, pos_x + rect_medium_length / 2 - constants.blocks['7'][0] / 2,
                               ground + circle_size + rect_medium_height + constants.blocks['7'][1] / 2])
    # block_list = [row[0] for row in complete_locations]
    final_pig_positions += [[pos_x, ground + circle_size + rect_medium_height, "BasicSmall"]]

    ground_width = 1.8 * circle_size  # adding a bit of space for safety (to not fall off a platform)
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
