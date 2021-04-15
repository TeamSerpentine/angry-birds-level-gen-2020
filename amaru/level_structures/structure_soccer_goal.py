from amaru.utilities import constants


def make_soccer_goal(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                     ground=-3.5, width=5, height=3, pos_x=6):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    platforms = []
    blocktype_goalpost = 3
    rectx = constants.blocks[str(blocktype_goalpost)][0]  # 0.43 for type 3
    recty = constants.blocks[str(blocktype_goalpost)][1]  # 0.85 for type 3

    # these change when size changes
    nr_platforms = width // constants.platform_size[0]  # (floor division)
    actual_width = nr_platforms * constants.platform_size[0]  # so the crossbar doesn't stick out
    left = pos_x - actual_width / 2 + rectx / 2
    right = pos_x + actual_width / 2 - rectx / 2
    rects_in_pole = (height - constants.platform_size[1]) // recty

    # left goal post
    for i in range(int(rects_in_pole)):
        #                            [  block type,     x-coordinate,    y-coordinate,      material     ]
        complete_locations.append([blocktype_goalpost, left, ground + recty / 2 + i * recty, "stone"])

    # right goal post
    for i in range(int(rects_in_pole)):
        complete_locations.append([blocktype_goalpost, right, ground + recty / 2 + i * recty, "stone"])

    post_height = ground + rects_in_pole * recty + 0.15  # adding some space,
    # since otherwise the goalposts get crammed for some reason

    # the horizontal cross bar
    for i in range(int(nr_platforms)):
        platforms.append(
            [left - rectx / 2 + constants.platform_size[0] / 2 + i * constants.platform_size[0],
             post_height + constants.platform_size[1] / 2])

    final_platforms += [platforms]

    final_pig_positions += [[pos_x, ground, "BasicBig"]]

    ground_width = actual_width
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
