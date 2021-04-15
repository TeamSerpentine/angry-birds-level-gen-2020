from amaru.level_structures import structure_chair_small
from amaru.level_structures import structure_small_table
from amaru.utilities import constants


def make_dinner_small(complete_locations=None, final_platforms=None, final_pig_positions=None, final_TNT_positions=None,
                      ground=-3.5, pos_x=1):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    chair_table_distance = 1.30
    complete_locations, final_platforms, final_pig_positions, final_TNT_positions = structure_small_table.make_table_small(
        complete_locations, final_platforms, final_pig_positions, final_TNT_positions, ground, pos_x, material="ice")
    complete_locations, final_platforms, final_pig_positions, final_TNT_positions = structure_chair_small.make_chair_small(
        complete_locations, final_platforms, final_pig_positions, final_TNT_positions, ground,
        pos_x - chair_table_distance, facing="right")
    complete_locations, final_platforms, final_pig_positions, final_TNT_positions = structure_chair_small.make_chair_small(
        complete_locations, final_platforms, final_pig_positions, final_TNT_positions, ground,
        pos_x + chair_table_distance, facing="left")

    ground_width = (chair_table_distance + constants.blocks['8'][0] / 2) * 2
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
