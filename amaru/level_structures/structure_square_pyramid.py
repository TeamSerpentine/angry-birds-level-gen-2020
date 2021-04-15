from amaru.utilities import constants


def make_square_pyramid(complete_locations=None, final_platforms=None, final_pig_positions=None,
                        final_TNT_positions=None, ground=-3.5, pos_x=3, height=5):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    # Retrieve block data
    square_size = constants.blocks['1'][0]
    triangle_size = constants.additional_object_sizes['2'][0]
    pyramid_height = height
    left = pos_x - (triangle_size + (pyramid_height * 2 - 1) / 2 * square_size)

    reduction_factor = 0
    stack_factor = 0
    # Algorithm to generate the period based on the input variable pyramid height
    for i in range(pyramid_height):
        complete_locations.append([20, left + square_size / 2 + stack_factor, ground + stack_factor])
        for i in range(pyramid_height * 2 - 1 - reduction_factor):
            complete_locations.append(
                [1, left + triangle_size + square_size / 2 + i * square_size + stack_factor, ground + stack_factor])
        complete_locations.append(
            [15, left + square_size / 2 + (pyramid_height * 2 - reduction_factor) * square_size + stack_factor,
             ground + stack_factor])
        stack_factor += square_size
        reduction_factor += 2

    final_pig_positions += [[pos_x, ground + pyramid_height * square_size, "BasicBig"]]

    ground_width = triangle_size * 2 + (pyramid_height * 2 - 1) * square_size
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
