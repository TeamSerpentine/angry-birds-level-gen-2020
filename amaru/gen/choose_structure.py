from amaru.utilities import constants


def choose_structure(structure_list, idx=0, location=None, complete_locations=None, final_platforms=None,
                     final_pig_positions=None, final_TNT_positions=None):
    nr_structures_we_have = len(structure_list)

    if location is None:
        location = [2, constants.absolute_ground]  # a standard location on the absolute ground
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []
    if idx >= nr_structures_we_have:
        idx = idx % nr_structures_we_have  # modulo to make sure we stay inside the list length
    return structure_list[idx](complete_locations=complete_locations, final_platforms=final_platforms,
                               final_pig_positions=final_pig_positions, final_TNT_positions=final_TNT_positions,
                               ground=location[1], pos_x=location[0])
