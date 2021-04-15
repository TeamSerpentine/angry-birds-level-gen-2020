from random import randint

from amaru.utilities import constants
from amaru.utilities.choose_item import choose_item


def make_peaks(center_point):
    current_tree_bottom = []  # bottom blocks of structure
    number_peaks = randint(1, constants.max_peaks)  # this is the number of peaks the structure will have
    top_item = choose_item(constants.probability_table_blocks)  # this is the item at top of structure
    distance_apart_extra = round(randint(min_peak_split, max_peak_split) / 100.0, 10)

    if number_peaks == 1:
        current_tree_bottom.append([top_item, center_point])

    if number_peaks == 2:
        current_tree_bottom.append(
            [top_item, round(center_point - (constants.blocks[str(top_item)][0] * 0.5) - distance_apart_extra, 10)])
        current_tree_bottom.append(
            [top_item, round(center_point + (constants.blocks[str(top_item)][0] * 0.5) + distance_apart_extra, 10)])

    if number_peaks == 3:
        current_tree_bottom.append(
            [top_item, round(center_point - (constants.blocks[str(top_item)][0]) - distance_apart_extra, 10)])
        current_tree_bottom.append([top_item, round(center_point, 10)])
        current_tree_bottom.append(
            [top_item, round(center_point + (constants.blocks[str(top_item)][0]) + distance_apart_extra, 10)])

    if number_peaks == 4:
        current_tree_bottom.append(
            [top_item,
             round(center_point - (constants.blocks[str(top_item)][0] * 1.5) - (distance_apart_extra * 2), 10)])
        current_tree_bottom.append(
            [top_item, round(center_point - (constants.blocks[str(top_item)][0] * 0.5) - distance_apart_extra, 10)])
        current_tree_bottom.append(
            [top_item, round(center_point + (constants.blocks[str(top_item)][0] * 0.5) + distance_apart_extra, 10)])
        current_tree_bottom.append(
            [top_item,
             round(center_point + (constants.blocks[str(top_item)][0] * 1.5) + (distance_apart_extra * 2), 10)])

    if number_peaks == 5:
        current_tree_bottom.append(
            [top_item,
             round(center_point - (constants.blocks[str(top_item)][0] * 2.0) - (distance_apart_extra * 2), 10)])
        current_tree_bottom.append(
            [top_item, round(center_point - (constants.blocks[str(top_item)][0]) - distance_apart_extra, 10)])
        current_tree_bottom.append([top_item, round(center_point, 10)])
        current_tree_bottom.append(
            [top_item, round(center_point + (constants.blocks[str(top_item)][0]) + distance_apart_extra, 10)])
        current_tree_bottom.append(
            [top_item,
             round(center_point + (constants.blocks[str(top_item)][0] * 2.0) + (distance_apart_extra * 2), 10)])
    return current_tree_bottom
