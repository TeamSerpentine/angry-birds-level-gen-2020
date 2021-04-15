from amaru.utilities import constants, subsets


def check_valid(grouping, choosen_item, current_tree_bottom, new_positions):
    # check no overlap
    i = 0
    while i < len(new_positions) - 1:
        if (new_positions[i] + (constants.blocks[str(choosen_item)][0]) / 2) > (
                new_positions[i + 1] - (constants.blocks[str(choosen_item)][0]) / 2):
            return False
        i = i + 1

    # check if each structural bottom block's edges supported by new blocks
    for item in current_tree_bottom:
        edge1 = item[1] - (constants.blocks[str(item[0])][0]) / 2
        edge2 = item[1] + (constants.blocks[str(item[0])][0]) / 2
        edge1_supported = False
        edge2_supported = False
        for new in new_positions:
            if ((new - (constants.blocks[str(choosen_item)][0]) / 2) <= edge1 and (
                    new + (constants.blocks[str(choosen_item)][0]) / 2) >= edge1):
                edge1_supported = True
            if ((new - (constants.blocks[str(choosen_item)][0]) / 2) <= edge2 and (
                    new + (constants.blocks[str(choosen_item)][0]) / 2) >= edge2):
                edge2_supported = True
        if edge1_supported == False or edge2_supported == False:
            return False
    return True


# check if new block can be placed under center of bottom row blocks validly

def check_center(grouping, choosen_item, current_tree_bottom):
    new_positions = []
    for subset in grouping:
        new_positions.append(subsets.find_subset_center(subset))
    return check_valid(grouping, choosen_item, current_tree_bottom, new_positions)


# check if new block can be placed under edges of bottom row blocks validly

def check_edge(grouping, choosen_item, current_tree_bottom):
    new_positions = []
    for subset in grouping:
        new_positions.append(subsets.find_subset_edges(subset)[0])
        new_positions.append(subsets.find_subset_edges(subset)[1])
    return check_valid(grouping, choosen_item, current_tree_bottom, new_positions)


# check if new block can be placed under both center and edges of bottom row blocks validly

def check_both(grouping, choosen_item, current_tree_bottom):
    new_positions = []
    for subset in grouping:
        new_positions.append(subsets.find_subset_edges(subset)[0])
        new_positions.append(subsets.find_subset_center(subset))
        new_positions.append(subsets.find_subset_edges(subset)[1])
    return check_valid(grouping, choosen_item, current_tree_bottom, new_positions)
