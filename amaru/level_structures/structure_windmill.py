from amaru.utilities import constants


def make_windmill(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                  ground=-3.5, pos_x=1):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    complete_locations.append([1, pos_x, ground + constants.blocks['1'][1] / 2, "ice"])
    complete_locations.append(
        [3, pos_x - constants.blocks['1'][0] / 2 - 0.2, ground + constants.blocks['3'][1] / 2, "stone"])
    complete_locations.append(
        [3, pos_x + constants.blocks['1'][0] / 2 + 0.2, ground + constants.blocks['3'][1] / 2, "stone"])
    complete_locations.append(
        [2, pos_x - constants.blocks['1'][0] / 2, ground + constants.blocks['1'][1] + constants.blocks['2'][1] / 2,
         "stone"])
    complete_locations.append(
        [2, pos_x + constants.blocks['1'][0] / 2, ground + constants.blocks['1'][1] + constants.blocks['2'][1] / 2,
         "stone"])
    complete_locations.append([2, pos_x - constants.blocks['1'][0] / 2 + 0.1,
                               ground + constants.blocks['1'][1] + 1.5 * constants.blocks['2'][1], "stone"])
    complete_locations.append([7, pos_x + constants.blocks['1'][0] / 2 - 0.3,
                               ground + constants.blocks['1'][1] + constants.blocks['2'][1] + constants.blocks['7'][
                                   1] / 2, "stone"])
    complete_locations.append([4, pos_x + constants.blocks['1'][0] / 2 + 0.1,
                               ground + constants.blocks['1'][1] + constants.blocks['2'][1] + constants.blocks['4'][
                                   1] / 2, "stone"])
    complete_locations.append(
        [3, pos_x - constants.blocks['1'][0] / 2, ground + 2 * constants.blocks['1'][1] + constants.blocks['3'][1] / 2,
         "wood"])
    complete_locations.append(
        [3, pos_x + constants.blocks['1'][0] / 2, ground + 2 * constants.blocks['1'][1] + constants.blocks['3'][1] / 2,
         "wood"])
    complete_locations.append(
        [10, pos_x, ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] / 2, "stone"])
    complete_locations.append([7, pos_x - constants.blocks['10'][0] / 2 + constants.blocks['7'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] / 2, "stone"])
    complete_locations.append([7, pos_x + constants.blocks['10'][0] / 2 - constants.blocks['7'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] / 2, "stone"])
    complete_locations.append([12, pos_x, ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + constants.blocks['12'][1] / 2, "wood"])
    complete_locations.append([12, pos_x - constants.blocks['12'][0] + 0.1,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + 1.5 * constants.blocks['12'][1], "wood"])
    complete_locations.append([12, pos_x + constants.blocks['12'][0] - 0.1,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + 1.5 * constants.blocks['12'][1], "wood"])
    complete_locations.append([7, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + constants.blocks['7'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.5 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "wood"])
    complete_locations.append([7, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 2.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.5 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "wood"])
    complete_locations.append([7, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 4.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.5 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "wood"])
    complete_locations.append([7, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 6.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.5 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "wood"])
    complete_locations.append([5, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 1.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.25 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "stone"])
    complete_locations.append([5, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 3.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.25 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "stone"])
    complete_locations.append([5, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 5.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.25 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "stone"])
    complete_locations.append([5, pos_x - 1.5 * constants.blocks['12'][0] + 0.1 + 7.5 * constants.blocks['7'][0],
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + 1.25 *
                               constants.blocks['7'][1] + 2 * constants.blocks['12'][1], "stone"])
    complete_locations.append([16, pos_x, ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + constants.blocks['12'][1] + constants.blocks['16'][1] / 2,
                               "wood"])
    complete_locations.append([4, pos_x - constants.blocks['16'][0] / 2 - constants.blocks['4'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + constants.blocks['12'][1] + constants.blocks['16'][1] / 2,
                               "stone"])
    complete_locations.append([4, pos_x + constants.blocks['16'][0] / 2 + constants.blocks['4'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + constants.blocks['12'][1] + constants.blocks['16'][1] / 2,
                               "stone"])
    complete_locations.append(
        [17, pos_x - constants.blocks['10'][0] / 2 + constants.blocks['7'][0] + constants.blocks['17'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['17'][1] / 2, "wood"])
    complete_locations.append(
        [17, pos_x + constants.blocks['10'][0] / 2 - constants.blocks['7'][0] - constants.blocks['17'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['17'][1] / 2, "wood"])
    complete_locations.append([11, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] / 2,
                               ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] +
                               constants.blocks['7'][1] + constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[
                                   1] + constants.blocks['11'][1] / 2, "wood"])
    complete_locations.append(
        [6, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + constants.blocks['6'][1] / 2, "wood"])
    complete_locations.append(
        [6, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 2.5 * constants.blocks['6'][1], "wood"])
    complete_locations.append(
        [6, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 4.5 * constants.blocks['6'][1], "wood"])
    complete_locations.append(
        [6, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 6.5 * constants.blocks['6'][1], "wood"])
    complete_locations.append(
        [5, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 1.5 * constants.blocks['6'][1], "stone"])
    complete_locations.append(
        [5, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 3.5 * constants.blocks['6'][1], "stone"])
    complete_locations.append(
        [5, pos_x - constants.platform_size[0] / 2 + constants.blocks['11'][0] + constants.blocks['6'][0] / 2,
         ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
         constants.blocks['12'][1] + 0.3 + 2 * constants.platform_size[1] + 5.5 * constants.blocks['6'][1], "stone"])
    platforms = [[pos_x - 1.5 * constants.blocks['12'][0] + 0.1,
                  ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
                  constants.blocks['12'][1] - constants.platform_size[1] / 2 + 0.1],
                 [pos_x + 0.9 * constants.blocks['12'][0],
                  ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
                  constants.blocks['12'][1] - constants.platform_size[1] / 2 + 0.2],
                 [pos_x + 1.5 * constants.platform_size[0] + 0.9 * constants.blocks['12'][0],
                  ground + 3 * constants.blocks['1'][1] + constants.blocks['10'][1] + constants.blocks['7'][1] +
                  constants.blocks['12'][1] - constants.platform_size[1] / 2 + 0.2], [pos_x,
                                                                                      ground + 3 *
                                                                                      constants.blocks['1'][1] +
                                                                                      constants.blocks['10'][1] +
                                                                                      constants.blocks['7'][1] +
                                                                                      constants.blocks['12'][
                                                                                          1] + 0.3 + 1.5 *
                                                                                      constants.platform_size[1]]]
    final_platforms += [platforms]

    ground_width = constants.blocks['1'][0] + constants.blocks['3'][0] * 2
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
