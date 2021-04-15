from amaru.utilities import constants


def pig_position_locator(complete_locations):
    possible_pig_positions = []  # Create empty list

    for block in complete_locations:
        block_width = round(constants.blocks[str(block[0])][0], 10)  # Return block width
        block_height = round(constants.blocks[str(block[0])][1], 10)  # Return block height
        pig_width = constants.pig_size[0]  # Return pig width
        pig_height = constants.pig_size[1]  # Return pig height
        if (constants.blocks[str(block[0])][0] < pig_width):  # dont place block on edge if block too thin
            test_positions = [[round(block[1], 10), round(block[2] + (pig_height / 2) + (block_height / 2), 10), ]]

        else:
            test_positions = [[round(block[1], 10), round(block[2] + (pig_height / 2) + (block_height / 2), 10), ],
                              [round(block[1] + (block_width / 3), 10),
                               round(block[2] + (pig_height / 2) + (block_height / 2), 10), ],
                              [round(block[1] - (block_width / 3), 10),
                               round(block[2] + (pig_height / 2) + (block_height / 2),
                                     10), ], ]  # check above centre of block

        for test_position in test_positions:  # For loop to search for valid pig positions

            valid_pig = True
            for i in complete_locations:
                if (
                        round((test_position[0] - pig_width / 2), 10)
                        < round((i[1] + (constants.blocks[str(i[0])][0]) / 2), 10)
                        and round((test_position[0] + pig_width / 2), 10)
                        > round((i[1] - (constants.blocks[str(i[0])][0]) / 2), 10)
                        and round((test_position[1] + pig_height / 2), 10)
                        > round((i[2] - (constants.blocks[str(i[0])][1]) / 2), 10)
                        and round((test_position[1] - pig_height / 2), 10)
                        < round((i[2] + (constants.blocks[str(i[0])][1]) / 2), 10)
                ):
                    valid_pig = False
            if valid_pig == True:
                possible_pig_positions.append(test_position)
    return pig_width, pig_height, possible_pig_positions
