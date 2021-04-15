from amaru.utilities import constants


def find_structure_width(structure):
    min_x = 999999.9
    max_x = -999999.9
    for block in structure:
        if round((block[1] - (constants.blocks[str(block[0])][0] / 2)), 10) < min_x:
            min_x = round((block[1] - (constants.blocks[str(block[0])][0] / 2)), 10)
        if round((block[1] + (constants.blocks[str(block[0])][0] / 2)), 10) > max_x:
            max_x = round((block[1] + (constants.blocks[str(block[0])][0] / 2)), 10)
    return (round(max_x - min_x, 10))


# finds the height of the given structure

def find_structure_height(structure):
    min_y = 999999.9
    max_y = -999999.9
    for block in structure:
        if round((block[2] - (constants.blocks[str(block[0])][1] / 2)), 10) < min_y:
            min_y = round((block[2] - (constants.blocks[str(block[0])][1] / 2)), 10)
        if round((block[2] + (constants.blocks[str(block[0])][1] / 2)), 10) > max_y:
            max_y = round((block[2] + (constants.blocks[str(block[0])][1] / 2)), 10)
    return (round(max_y - min_y, 10))
