from amaru.utilities import constants


def create_structure_pillar(gr_cor, n_blocks, block_type="1"):
    piller_list = []
    bl = constants.blocks[block_type]

    height_pillar = gr_cor[1]
    height_bl = bl[1]
    cor_width_pil = [gr_cor[0] - bl[0] / 2, gr_cor[0] + bl[0] / 2]
    for i in range(n_blocks):
        piller_list.append([block_type, gr_cor[0], height_pillar + height_bl / 2.0])
        height_pillar = height_pillar + height_bl

    return piller_list, cor_width_pil, height_pillar
