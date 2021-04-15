from random import randint, uniform

from amaru.utilities import constants


def create_platforms(number_platforms, complete_locations, final_pig_positions, final_platforms=None):
    platform_centers = []
    platform_widths = []
    the_platforms = []
    attempts = 0  # number of attempts so far to find space for platform
    if final_platforms is None:
        final_platforms = []
    big_platforms_made = 0
    while big_platforms_made < number_platforms:
        platform_width = randint(5, 7)
        platform_position = [uniform(constants.level_width_min + ((platform_width * constants.platform_size[0]) / 2.0),
                                     constants.level_width_max - ((platform_width * constants.platform_size[0]) / 2.0)),
                             uniform(constants.level_height_min,
                                     (constants.level_height_max - constants.minimum_height_gap))]
        temp_platform = []

        start_platform = -0.5 * (platform_width - 1)
        for i in range(platform_width):
            temp_platform.append(
                [platform_position[0] + start_platform * constants.platform_size[0], platform_position[1]])
            start_platform += 1

        base_platform = temp_platform.copy()

        for h in [0, 2, 4, 6, 8, 9]:
            temp_platform.append([platform_position[0] - 5.5 * constants.platform_size[0],
                                  platform_position[1] + (h + 1) * constants.platform_size[1]])
            temp_platform.append(
                [platform_position[0] - 5.5 * constants.platform_size[0] + 5 * constants.platform_size[0],
                 platform_position[1] + (h + 1) * constants.platform_size[1]])
            temp_platform.append(
                [platform_position[0] - 5.5 * constants.platform_size[0] + 11 * constants.platform_size[0],
                 platform_position[1] + (h + 1) * constants.platform_size[1]])

        overlap = False
        for platform in temp_platform:

            if (((platform[0] - (constants.platform_size[0] / 2)) < constants.level_width_min) or (
                    (platform[0] + (constants.platform_size[0]) / 2) > constants.level_width_max)):
                overlap = True

            for block in complete_locations:
                if (round((platform[0] - constants.platform_distance_buffer - constants.platform_size[0] / 2),
                          10) <= round(
                        (block[1] + constants.blocks[str(block[0])][0] / 2), 10) and
                        round((platform[0] + constants.platform_distance_buffer + constants.platform_size[0] / 2),
                              10) >= round(
                            (block[1] - constants.blocks[str(block[0])][0] / 2), 10) and
                        round((platform[1] + constants.platform_distance_buffer + constants.platform_size[1] / 2),
                              10) >= round(
                            (block[2] - constants.blocks[str(block[0])][1] / 2), 10) and
                        round((platform[1] - constants.platform_distance_buffer - constants.platform_size[1] / 2),
                              10) <= round(
                            (block[2] + constants.blocks[str(block[0])][1] / 2), 10)):
                    overlap = True

            for pig in final_pig_positions:
                if (round((platform[0] - constants.platform_distance_buffer - constants.platform_size[0] / 2),
                          10) <= round(
                        (pig[0] + constants.pig_size[0] / 2), 10) and
                        round((platform[0] + constants.platform_distance_buffer + constants.platform_size[0] / 2),
                              10) >= round(
                            (pig[0] - constants.pig_size[0] / 2), 10) and
                        round((platform[1] + constants.platform_distance_buffer + constants.platform_size[1] / 2),
                              10) >= round(
                            (pig[1] - constants.pig_size[1] / 2), 10) and
                        round((platform[1] - constants.platform_distance_buffer - constants.platform_size[1] / 2),
                              10) <= round(
                            (pig[1] + constants.pig_size[1] / 2), 10)):
                    overlap = True

            for platform_set in final_platforms:
                for platform2 in platform_set:
                    if (round((platform[0] - constants.platform_distance_buffer - constants.platform_size[0] / 2),
                              10) <= round(
                            (platform2[0] + constants.platform_size[0] / 2), 10) and
                            round((platform[0] + constants.platform_distance_buffer + constants.platform_size[0] / 2),
                                  10) >= round(
                                (platform2[0] - constants.platform_size[0] / 2), 10) and
                            round((platform[1] + constants.platform_distance_buffer + constants.platform_size[1] / 2),
                                  10) >= round(
                                (platform2[1] - constants.platform_size[1] / 2), 10) and
                            round((platform[1] - constants.platform_distance_buffer - constants.platform_size[1] / 2),
                                  10) <= round(
                                (platform2[1] + constants.platform_size[1] / 2), 10)):
                        overlap = True

            for platform_set2 in final_platforms:
                for i in platform_set2:
                    if i[0] + constants.platform_size[0] > platform[0] and i[0] - constants.platform_size[0] < platform[
                        0]:
                        if i[1] + constants.minimum_height_gap > platform[1] and i[1] - constants.minimum_height_gap < \
                                platform[1]:
                            overlap = True

        if overlap == False:
            final_platforms.append(base_platform)
            platform_centers.append(platform_position)
            big_platforms_made += 1
            platform_widths.append(platform_width * constants.platform_size[0])
            the_platforms.append(base_platform)

        attempts = attempts + 1
        if attempts > constants.max_attempts:
            attempts = 0
            number_platforms = number_platforms - 1

    return number_platforms, final_platforms, platform_centers, platform_widths, the_platforms
