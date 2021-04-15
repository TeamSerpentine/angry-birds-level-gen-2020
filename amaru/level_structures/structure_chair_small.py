from amaru.utilities import constants


def make_chair_small(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                     ground=-3.5, pos_x=0, facing="right"):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    width = constants.blocks['8'][0]
    complete_locations.append(
        [7, pos_x - width / 2 + constants.blocks['7'][0] / 2, ground + constants.blocks['7'][1] / 2, "wood"])
    complete_locations.append(
        [7, pos_x + width / 2 - constants.blocks['7'][0] / 2, ground + constants.blocks['7'][1] / 2, "wood"])
    complete_locations.append([8, pos_x, ground + constants.blocks['7'][1] + constants.blocks['8'][1] / 2, "wood"])
    seat_height = ground + constants.blocks['7'][1] + constants.blocks['8'][1]
    if facing == "right":
        complete_locations.append(
            [9, pos_x - width / 2 + constants.blocks['9'][0] / 2, seat_height + constants.blocks['9'][1] / 2, "wood"])
        final_pig_positions.append([pos_x + width / 2 - constants.blocks['9'][0], seat_height, "BasicSmall"])
    else:  # facing left
        complete_locations.append(
            [9, pos_x + width / 2 - constants.blocks['9'][0] / 2, seat_height + constants.blocks['9'][1] / 2, "wood"])
        final_pig_positions.append([pos_x - width / 2 + constants.blocks['9'][0], seat_height, "BasicSmall"])
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
