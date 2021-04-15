from amaru.utilities import constants


def make_TV(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
            ground=-3.5, width=5, height=5, pos_x=3):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    platforms = []

    # blocktypes
    block_tv_vert = 9
    block_tv_hori = 8
    tv_stand = 3

    vert_x = constants.blocks[str(block_tv_vert)][0]
    vert_y = constants.blocks[str(block_tv_vert)][1]
    hori_x = constants.blocks[str(block_tv_hori)][0]
    hori_y = constants.blocks[str(block_tv_hori)][1]
    stand_x = constants.blocks[str(tv_stand)][0]
    stand_y = constants.blocks[str(tv_stand)][1]

    buffer_space = 0.12

    # these change when size changes
    nr_platforms = width // constants.platform_size[0]  # (floor division)
    actual_width = nr_platforms * constants.platform_size[0]
    nr_under = (actual_width / 2) // hori_x
    under_width = nr_under * hori_x
    left = pos_x - actual_width / 2
    right = pos_x + actual_width / 2
    rects_side = (height - 2 * constants.platform_size[1] - hori_y - stand_y - 2 * buffer_space) // vert_y

    # under the stand
    if int(nr_under) % 2 == 0:
        # even nr
        for i in range(int(nr_under)):
            if i % 2 == 0:
                complete_locations.append(
                    [block_tv_hori, pos_x + hori_x / 2 + i / 2 * hori_x, ground + hori_y / 2, "ice"])
            else:
                complete_locations.append(
                    [block_tv_hori, pos_x - hori_x / 2 - (i - 1) / 2 * hori_x, ground + hori_y / 2, "ice"])
    else:
        # odd nr
        complete_locations.append([block_tv_hori, pos_x, ground + hori_y / 2, "ice"])
        for i in range(int(nr_under) - 1):
            if i % 2 == 0:
                complete_locations.append([block_tv_hori, pos_x + hori_x + i / 2 * hori_x, ground + hori_y / 2, "ice"])
            else:
                complete_locations.append(
                    [block_tv_hori, pos_x - hori_x - (i - 1) / 2 * hori_x, ground + hori_y / 2, "ice"])

    # the stand itself
    complete_locations.append([tv_stand, pos_x, ground + hori_y + stand_y / 2, "ice"])
    stand_height = ground + hori_y + stand_y + buffer_space  # adding buffer space

    # low bar of tv
    for i in range(int(nr_platforms)):
        platforms.append([left + constants.platform_size[0] / 2 + i * constants.platform_size[0],
                          stand_height + constants.platform_size[1] / 2])

    # left side
    for i in range(int(rects_side)):
        complete_locations.append(
            [block_tv_vert, left + vert_x / 2, stand_height + constants.platform_size[1] + vert_y / 2 + i * vert_y,
             "ice"])

    # right side
    for i in range(int(rects_side)):
        complete_locations.append(
            [block_tv_vert, right - vert_x / 2, stand_height + constants.platform_size[1] + vert_y / 2 + i * vert_y,
             "ice"])

    side_height = stand_height + constants.platform_size[1] + rects_side * vert_y + buffer_space  # adding buffer space

    # upper bar of tv
    for i in range(int(nr_platforms)):
        platforms.append([left + constants.platform_size[0] / 2 + i * constants.platform_size[0],
                          side_height + constants.platform_size[1] / 2])

    final_platforms += [platforms]

    ground_width = under_width

    final_pig_positions += [[pos_x, stand_height + 1, "BasicBig"]]

    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
