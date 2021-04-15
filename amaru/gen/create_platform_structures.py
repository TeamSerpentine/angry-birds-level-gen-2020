from amaru.gen.make_structure import make_structure
from amaru.utilities import constants


def create_platform_structures(final_platforms, platform_centers, complete_locations, final_pig_positions):
    current_platform = 0
    for platform_set in final_platforms:
        platform_set_width = len(platform_set) * constants.platform_size[0]

        above_blocks = []
        for platform_set2 in final_platforms:
            if platform_set2 != platform_set:
                for i in platform_set2:
                    if i[0] + constants.platform_size[0] > platform_set[0][0] and i[0] - constants.platform_size[0] < \
                            platform_set[-1][
                                0] and i[1] > platform_set[0][1]:
                        above_blocks.append(i)

        min_above = constants.level_height_max
        for j in above_blocks:
            if j[1] < min_above:
                min_above = j[1]

        center_point = platform_centers[current_platform][0]
        absolute_ground = platform_centers[current_platform][1] + (constants.platform_size[1] / 2)

        max_width = platform_set_width
        max_height = (min_above - absolute_ground) - constants.pig_size[1] - constants.platform_size[1]

        complete_locations2, final_pig_positions2 = make_structure(absolute_ground, center_point, max_width, max_height)
        complete_locations = complete_locations + complete_locations2
        final_pig_positions = final_pig_positions + final_pig_positions2

        current_platform = current_platform + 1

    return complete_locations, final_pig_positions
