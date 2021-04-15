from amaru.level_structures import structure_pillar
from amaru.utilities import constants


def create_structure_tank(complete_locations=None, final_platforms=None, final_pig_positions=None,
                          final_TNT_positions=None, ground=-3.5, pos_x=2, n_wh=4, sz_frame=2):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    cor_struc = [pos_x, ground]
    hg_obj = cor_struc[1]
    wh_sz = constants.blocks["16"]
    wh_cor_start = cor_struc[0] - 2 * wh_sz[0]

    for i in range(n_wh):
        complete_locations.append(["16", wh_cor_start + wh_sz[0] / 2, hg_obj + wh_sz[1] / 2])
        wh_cor_start += wh_sz[0]

    # place frame
    hg_obj += wh_sz[1]
    piller_list, _, hg_obj = structure_pillar.create_structure_pillar(
        [cor_struc[0], hg_obj], sz_frame, block_type="12"
    )

    complete_locations.extend(piller_list)
    pig_locations = [cor_struc[0], hg_obj + 0.25]
    # place canon
    cn_sz = constants.blocks["12"]
    complete_locations.append(["12", cor_struc[0] - cn_sz[0] / 2 - 0.25, hg_obj])

    piller_list, _, _ = structure_pillar.create_structure_pillar(
        [cor_struc[0] - 0.40, hg_obj + cn_sz[1]], 2, block_type="6"
    )

    complete_locations.extend(piller_list)
    # place pillar back
    piller_list, _, hg_obj = structure_pillar.create_structure_pillar(
        [cor_struc[0] + 0.40, hg_obj], 3, block_type="6"
    )
    complete_locations.extend(piller_list)

    # place roof
    rf_sz = constants.blocks["10"]
    complete_locations.append(["10", cor_struc[0], hg_obj + rf_sz[1] / 2])

    # place driver pig

    final_pig_positions += [pig_locations]

    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
