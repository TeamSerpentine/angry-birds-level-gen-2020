from random import randint

from amaru.utilities import constants, subsets, block_checks
from amaru.utilities.choose_item import choose_item


def add_new_row(current_tree_bottom, total_tree):
    groupings = subsets.generate_subsets(current_tree_bottom)  # generate possible groupings of bottom row objects
    chosen_item = choose_item(constants.probability_table_blocks)  # chosen block for new row
    center_groupings = []  # collection of viable groupings with new block at center
    edge_groupings = []  # collection of viable groupings with new block at edges
    both_groupings = []  # collection of viable groupings with new block at both center and edges

    # check if new block is viable for each grouping in each position
    for grouping in groupings:
        if block_checks.check_center(grouping, chosen_item, current_tree_bottom):  # check if center viable
            center_groupings.append(grouping)
        if block_checks.check_edge(grouping, chosen_item, current_tree_bottom):  # check if edges viable
            edge_groupings.append(grouping)
        if block_checks.check_both(grouping, chosen_item, current_tree_bottom):  # check if both center and edges viable
            both_groupings.append(grouping)

    # randomly choose a configuration (grouping/placement) from the viable options
    total_options = len(center_groupings) + len(edge_groupings) + len(both_groupings)  # total number of options
    if total_options > 0:
        option = randint(1, total_options)
        if option > len(center_groupings) + len(edge_groupings):
            selected_grouping = both_groupings[option - (len(center_groupings) + len(edge_groupings) + 1)]
            placement_method = 2
        elif option > len(center_groupings):
            selected_grouping = edge_groupings[option - (len(center_groupings) + 1)]
            placement_method = 1
        else:
            selected_grouping = center_groupings[option - 1]
            placement_method = 0

        # construct the new bottom row for structure using selected block/configuration
        new_bottom = []
        for subset in selected_grouping:
            if placement_method == 0:
                new_bottom.append([chosen_item, subsets.find_subset_center(subset)])
            if placement_method == 1:
                new_bottom.append([chosen_item, subsets.find_subset_edges(subset)[0]])
                new_bottom.append([chosen_item, subsets.find_subset_edges(subset)[1]])
            if placement_method == 2:
                new_bottom.append([chosen_item, subsets.find_subset_edges(subset)[0]])
                new_bottom.append([chosen_item, subsets.find_subset_center(subset)])
                new_bottom.append([chosen_item, subsets.find_subset_edges(subset)[1]])

        for i in new_bottom:
            i[1] = round(i[1], 10)  # round all values to prevent floating point inaccuracy from causing errors

        current_tree_bottom = new_bottom
        total_tree.append(current_tree_bottom)  # add new bottom row to the structure
        return total_tree, current_tree_bottom  # return the new structure

    else:
        return add_new_row(current_tree_bottom, total_tree)  # choose a new block and try again if no options available
