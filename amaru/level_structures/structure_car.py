from amaru.level_structures import structure_pillar
from amaru.utilities import constants


def create_structure_car(complete_locations=None, final_platforms=None, final_pig_positions=None,
                         final_TNT_positions=None, ground=-3.5, width=12, height=5, pos_x=2, pil_block="5"):
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    cor_struc = [pos_x, ground]
    wh_id = "16"

    # frame
    fr_id = "12"

    # roof
    rf_id = "10"

    # place wheels
    fr_sz = constants.blocks[fr_id]
    wh_x = [cor_struc[0] + fr_sz[0] / 2.0, cor_struc[0] - fr_sz[0] / 2.0]

    fr_wh = [wh_id, wh_x[0], cor_struc[1] + constants.blocks[wh_id][1] / 2]
    bk_wh = [wh_id, wh_x[1], cor_struc[1] + constants.blocks[wh_id][1] / 2]
    complete_locations.extend([fr_wh, bk_wh])

    # place frame
    cor_fr = [
        fr_id,
        cor_struc[0],
        cor_struc[1] + constants.blocks[wh_id][1] + fr_sz[1] / 2.0,
    ]
    complete_locations.extend([cor_fr])
    # keep room for pig
    fr_cor_pil = [
        cor_struc[0] - constants.blocks[pil_block][0] / 2 - 0.25,
        cor_fr[2] + fr_sz[1] / 2.0,
    ]
    bk_cor_pil = [
        cor_struc[0] + constants.blocks[pil_block][0] / 2 + 0.25,
        cor_fr[2] + fr_sz[1] / 2.0,
    ]

    # place pillars car
    pil_l_fr, pil_width_fr, pil_height_fr = structure_pillar.create_structure_pillar(
        fr_cor_pil, 3, block_type=pil_block
    )
    pil_l_bk, pil_width_bk, pil_height_bk = structure_pillar.create_structure_pillar(
        bk_cor_pil, 3, block_type=pil_block
    )

    complete_locations.extend(pil_l_fr)
    complete_locations.extend(pil_l_bk)

    # place roof
    complete_locations.extend(
        [[rf_id, cor_struc[0], pil_height_fr + constants.blocks[rf_id][1] / 2]]
    )

    # place driver pig
    pig_locations = [cor_struc[0], cor_fr[2] + fr_sz[1] / 2.0]
    final_pig_positions += [pig_locations]

    ground_width = fr_sz[0] + 0.1  # safety for circles as wheels
    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
