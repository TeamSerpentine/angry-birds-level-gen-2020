from amaru.level_structures import structure_square


def create_structure_func(
        struct_func=structure_square.create_structure_square, cor_struc=None, complete_locations=None,
        final_platforms=None, final_pig_positions=None, final_TNT_positions=None, n_rep=5, pig_locations=[]
):
    if complete_locations is None:
        complete_locations = []
    if cor_struc is None:
        cor_struc = [0, 0]
    if final_TNT_positions is None:
        final_TNT_positions = []
    if final_platforms is None:
        final_platforms = []
    if final_pig_positions is None:
        final_pig_positions = []
    x, y = cor_struc
    for i in range(n_rep):
        complete_locations, pig_locations, top_cor = struct_func([x, y], complete_locations)
        y = top_cor

    return complete_locations, final_platforms, final_pig_positions, final_TNT_positions, top_cor
