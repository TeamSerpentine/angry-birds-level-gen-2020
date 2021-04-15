from copy import deepcopy
from random import randint

from amaru.gen.add_new_row import add_new_row
from amaru.gen.make_peaks import make_peaks
from amaru.utilities import constants, analyze_structure


def make_structure(absolute_ground, center_point, max_width, max_height):
    total_tree = []  # all blocks of structure (so far)

    # creates the first row (peaks) for the structure, ensuring that max_width restriction is satisfied
    current_tree_bottom = make_peaks(center_point)
    if max_width > 0.0:
        while analyze_structure.find_structure_width(current_tree_bottom) > max_width:
            current_tree_bottom = make_peaks(center_point)

    total_tree.append(current_tree_bottom)

    # recursively add more rows of blocks to the level structure
    structure_width = analyze_structure.find_structure_width(current_tree_bottom)
    structure_height = (constants.blocks[str(current_tree_bottom[0][0])][1]) / 2
    if max_height > 0.0 or max_width > 0.0:
        pre_total_tree = [current_tree_bottom]
        while structure_height < max_height and structure_width < max_width:
            total_tree, current_tree_bottom = add_new_row(current_tree_bottom, total_tree)
            complete_locations = []
            ground = absolute_ground
            for row in reversed(total_tree):
                for item in row:
                    complete_locations.append(
                        [item[0], item[1], round((((constants.blocks[str(item[0])][1]) / 2) + ground), 10)])
                ground = ground + (constants.blocks[str(item[0])][1])
            structure_height = analyze_structure.find_structure_height(complete_locations)
            structure_width = analyze_structure.find_structure_width(complete_locations)
            if structure_height > max_height or structure_width > max_width:
                total_tree = deepcopy(pre_total_tree)
            else:
                pre_total_tree = deepcopy(total_tree)

    # make structure vertically correct (add y position to blocks)
    complete_locations = []
    ground = absolute_ground
    for row in reversed(total_tree):
        for item in row:
            complete_locations.append(
                [item[0], item[1], round((((constants.blocks[str(item[0])][1]) / 2) + ground), 10)])
        ground = ground + (constants.blocks[str(item[0])][1])

    print("Width:", analyze_structure.find_structure_width(complete_locations))
    print("Height:", analyze_structure.find_structure_height(complete_locations))
    print("Block number:", len(complete_locations))  # number blocks present in the structure

    # identify all possible pig positions on top of blocks (maximum 2 pigs per block, checks center before sides)
    possible_pig_positions = []
    for block in complete_locations:
        block_width = round(constants.blocks[str(block[0])][0], 10)
        block_height = round(constants.blocks[str(block[0])][1], 10)
        pig_width = constants.pig_size[0]
        pig_height = constants.pig_size[1]

        if constants.blocks[str(block[0])][0] < pig_width:  # dont place block on edge if block too thin
            test_positions = [[round(block[1], 10), round(block[2] + (pig_height / 2) + (block_height / 2), 10)]]
        else:
            test_positions = [[round(block[1], 10), round(block[2] + (pig_height / 2) + (block_height / 2), 10)],
                              [round(block[1] + (block_width / 3), 10),
                               round(block[2] + (pig_height / 2) + (block_height / 2), 10)],
                              [round(block[1] - (block_width / 3), 10),
                               round(block[2] + (pig_height / 2) + (block_height / 2),
                                     10)]]  # check above centre of block
        for test_position in test_positions:
            valid_pig = True
            for i in complete_locations:
                if (round((test_position[0] - pig_width / 2), 10) < round((i[1] + (constants.blocks[str(i[0])][0]) / 2),
                                                                          10) and
                        round((test_position[0] + pig_width / 2), 10) > round(
                            (i[1] - (constants.blocks[str(i[0])][0]) / 2),
                            10) and
                        round((test_position[1] + pig_height / 2), 10) > round(
                            (i[2] - (constants.blocks[str(i[0])][1]) / 2),
                            10) and
                        round((test_position[1] - pig_height / 2), 10) < round(
                            (i[2] + (constants.blocks[str(i[0])][1]) / 2),
                            10)):
                    valid_pig = False
            if valid_pig == True:
                possible_pig_positions.append(test_position)

    # identify all possible pig positions on ground within structure
    left_bottom = total_tree[-1][0]
    right_bottom = total_tree[-1][-1]
    test_positions = []
    x_pos = left_bottom[1]

    while x_pos < right_bottom[1]:
        test_positions.append([round(x_pos, 10), round(absolute_ground + (pig_height / 2), 10)])
        x_pos = x_pos + constants.pig_precision

    for test_position in test_positions:
        valid_pig = True
        for i in complete_locations:
            if (round((test_position[0] - pig_width / 2), 10) < round((i[1] + (constants.blocks[str(i[0])][0]) / 2),
                                                                      10) and
                    round((test_position[0] + pig_width / 2), 10) > round((i[1] - (constants.blocks[str(i[0])][0]) / 2),
                                                                          10) and
                    round((test_position[1] + pig_height / 2), 10) > round(
                        (i[2] - (constants.blocks[str(i[0])][1]) / 2), 10) and
                    round((test_position[1] - pig_height / 2), 10) < round(
                        (i[2] + (constants.blocks[str(i[0])][1]) / 2), 10)):
                valid_pig = False
        if valid_pig == True:
            possible_pig_positions.append(test_position)

    # randomly choose a pig position and remove those that overlap it, repeat until no more valid positions
    final_pig_positions = []
    while len(possible_pig_positions) > 0:
        pig_choice = possible_pig_positions.pop(randint(1, len(possible_pig_positions)) - 1)
        final_pig_positions.append(pig_choice)
        new_pig_positions = []
        for i in possible_pig_positions:
            if (round((pig_choice[0] - pig_width / 2), 10) >= round((i[0] + pig_width / 2), 10) or
                    round((pig_choice[0] + pig_width / 2), 10) <= round((i[0] - pig_width / 2), 10) or
                    round((pig_choice[1] + pig_height / 2), 10) <= round((i[1] - pig_height / 2), 10) or
                    round((pig_choice[1] - pig_height / 2), 10) >= round((i[1] + pig_height / 2), 10)):
                new_pig_positions.append(i)
        possible_pig_positions = new_pig_positions

    print("Pig number:", len(final_pig_positions))  # number of pigs present in the structure
    print("")

    return complete_locations, final_pig_positions
