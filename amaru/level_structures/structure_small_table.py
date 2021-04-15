from amaru.utilities import constants


def make_table_small(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                     ground=-3.5, pos_x=1, material="wood"):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    # the table:               [block type, x-coordinate, y-coordinate, material]
    complete_locations.append([9, pos_x - 0.55, ground + constants.blocks['9'][1] / 2, material])
    complete_locations.append([9, pos_x + 0.55, ground + constants.blocks['9'][1] / 2, material])
    complete_locations.append([10, pos_x, ground + constants.blocks['9'][1] + constants.blocks['10'][1] / 2, material])
    # the candle:
    complete_locations.append(
        [7, pos_x, ground + constants.blocks['9'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] / 2,
         "stone"])
    complete_locations.append([5, pos_x,
                               ground + constants.blocks['9'][1] + constants.blocks['10'][1] + constants.blocks['7'][
                                   1] + constants.blocks['5'][1] / 2, "wood"])
    # adding platforms, pig-positions, and TNT is also possible (but not done in this function)
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
