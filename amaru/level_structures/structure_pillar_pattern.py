from amaru.utilities import constants


def create_structure_pillar_pattern(gr_cor, n_repeats=1, block_type_pattern=None):
    if block_type_pattern is None:
        block_type_pattern = ["1", "2"]
    pillar_list = []
    pat_wd = [constants.blocks[x][0] for x in block_type_pattern]
    pat_hg = [constants.blocks[x][1] for x in block_type_pattern]
    max_wd = max(pat_wd)
    height_pillar = gr_cor[1]

    for i in range(n_repeats):
        for j, block_type in enumerate(block_type_pattern):
            bl = constants.blocks[block_type]
            height_bl = bl[1]

            pillar_list.append([block_type, gr_cor[0], height_pillar + height_bl / 2.0])
            height_pillar += height_bl

    return pillar_list, max_wd, height_pillar
