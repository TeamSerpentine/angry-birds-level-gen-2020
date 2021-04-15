from amaru.utilities import constants


def create_structure_square(complete_locations=None, final_platforms=None, final_pig_positions=None,
                            final_TNT_positions=None, ground=-3.5, pos_x=0, vr_bk=13):
    # if cor_struc is None:
    #     cor_struc = [0, absolute_ground]
    if complete_locations is None:
        complete_locations = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    if final_TNT_positions is None:
        final_TNT_positions = []

    cor_struc = [pos_x, ground]

    hr = constants.blocks["12"]
    hg_str = cor_struc[1]
    complete_locations.append([12, cor_struc[0], hg_str + hr[1] / 2])

    hg_str += hr[1]

    vr = constants.blocks[str(vr_bk)]
    complete_locations.append(
        [vr_bk, cor_struc[0] + hr[0] / 2 - vr[0] / 2, hg_str + vr[1] / 2]
    )
    complete_locations.append(
        [vr_bk, cor_struc[0] - hr[0] / 2 + vr[0] / 2, hg_str + vr[1] / 2]
    )

    hg_str += vr[1]
    complete_locations.append([12, cor_struc[0], hg_str + hr[1] / 2])

    hg_str += hr[1]

    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions
