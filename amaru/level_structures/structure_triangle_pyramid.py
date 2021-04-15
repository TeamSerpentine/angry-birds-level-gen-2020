import math

from amaru.utilities import constants


def make_triangle_pyramid(complete_locations=None, final_platforms=None, final_pig_positions=None,
                          final_TNT_positions=None, ground=-3.5, pos_x=1, height=3):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    triangle_size = constants.additional_object_sizes['2'][0]
    pyramid_height = height

    ground_width = (pyramid_height + 2) * 1.5 * triangle_size
    left = pos_x - ground_width / 2

    reduction_factor1 = 0
    reduction_factor2 = 0
    height_factor1 = 0
    height_factor2 = 0
    stack_factor = 0
    for i in range(2 * pyramid_height + 2):
        # Downwards stacking
        if (i % 2) == 0:
            for i in range(pyramid_height + 2 - reduction_factor1):
                complete_locations.append([18, left + i * 1.5 * triangle_size + 0.75 * stack_factor,
                                           ground + stack_factor - 0.25 - height_factor1])
                # print(i)
            stack_factor += triangle_size
            reduction_factor1 += 1
            height_factor1 += 0.1
        # Upwards stacking
        else:
            for i in range(pyramid_height + 1 - reduction_factor2):
                complete_locations.append([19, left + i * 1.5 * triangle_size + 0.75 * stack_factor,
                                           ground + stack_factor - 0.25 - height_factor2])
                # print(i)
            stack_factor += 0
            reduction_factor2 += 1
            height_factor2 += 0.1
    # final_pig_positions += [[(1.5 * pyramid_height + 2) / 2 * triangle_size, ground + (pyramid_height+1) * triangle_size-0.25,"BasicSmall"]]
    # final_pig_positions += [[(1.5 * (pyramid_height + 2)) / 2 * triangle_size, ground + (pyramid_height+1) * triangle_size-0.25,"BasicSmall"]]

    # ground_width = (pyramid_height+2) * 1.5 * triangle_size

    final_pig_positions += [[(1.5 * pyramid_height + 2) / 2 * triangle_size * math.sqrt(2) / 4 * 2.5 - 1.2,
                             constants.absolute_ground + (pyramid_height + 1) * triangle_size - 0.35,
                             "BasicBig"]]

    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
