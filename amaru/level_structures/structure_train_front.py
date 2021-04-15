from amaru.utilities import constants


def make_train_front(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                     ground=-3.5, pos_x=3):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    # block_list = []
    circle_size = constants.additional_object_sizes['3'][0]
    rect_medium_length = constants.blocks['10'][0]
    rect_medium_height = constants.blocks['10'][1]
    two_length = constants.blocks['2'][0]
    three_height = constants.blocks['3'][1]

    left = pos_x - 2 * circle_size + 0.5 * circle_size
    offset = - circle_size / 2 + constants.blocks['3'][0] / 2

    for i in range(4):
        complete_locations.append([16, left + i * circle_size, ground + circle_size / 2, "stone"])
    complete_locations.append([10, left + 0.25 * rect_medium_length, ground + circle_size + rect_medium_height / 2])
    complete_locations.append(
        [10, left + 0.25 * rect_medium_length, ground + circle_size + rect_medium_height + rect_medium_height / 2])
    complete_locations.append(
        [10, left + 0.25 * rect_medium_length + rect_medium_length, ground + circle_size + rect_medium_height / 2])
    complete_locations.append([10, left + 0.25 * rect_medium_length + rect_medium_length,
                               ground + circle_size + rect_medium_height + rect_medium_height / 2])
    complete_locations.append([2, left + offset + constants.blocks['3'][0] / 2 + 0.5 * two_length,
                               ground + circle_size + 2 * rect_medium_height + constants.blocks['2'][1] / 2])
    complete_locations.append([2, left + offset + constants.blocks['3'][0] / 2 + 1.5 * two_length,
                               ground + circle_size + 2 * rect_medium_height + constants.blocks['2'][1] / 2])
    complete_locations.append(
        [3, left + offset, ground + circle_size + 2 * rect_medium_height + constants.blocks['3'][1] / 2])
    complete_locations.append(
        [9, left + offset + constants.blocks['3'][0] / 2 + 2 * two_length + constants.blocks['9'][0] / 2,
         ground + circle_size + 2.2 * rect_medium_height + constants.blocks['9'][1] / 2])
    complete_locations.append([3, left + offset + 1.6 * rect_medium_length + 0.2 * two_length,
                               ground + circle_size + 2.2 * rect_medium_height + constants.blocks['3'][1] / 2])
    complete_locations.append([10, left + 0.4 * rect_medium_length + rect_medium_length,
                               ground + circle_size + 2 * rect_medium_height + three_height + constants.blocks['10'][
                                   1] / 2])
    # block_list = [row[0] for row in complete_locations]
    final_pig_positions.append(
        [left + offset + constants.blocks['3'][0] / 2 + 2 * two_length + constants.blocks['9'][0] + 0.26,
         ground + circle_size + 2 * rect_medium_height, "BasicSmall"])

    ground_width = 4 * circle_size - 0.8 * circle_size
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
