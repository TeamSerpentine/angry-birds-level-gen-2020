from random import randrange, randint

from amaru.gen.choose_structure import choose_structure
from amaru.utilities import constants
from amaru.utilities.choose_item import choose_item


def write_level_xml(complete_locations, selected_other, final_pig_positions, final_TNT_positions, final_platforms,
                    number_birds, current_level, restricted_combinations, nr_structures_we_have, structure_list):
    restricted_combinations_split = restricted_combinations
    loop_param = 1
    while loop_param == 1:
        in_list = []
        for i in complete_locations:
            j = 0
            material = constants.materials[randint(0, len(constants.materials) - 1)]  # material is chosen randomly
            while [material, constants.block_names[str(i[0])]] in restricted_combinations_split and j < 15:
                material = constants.materials[randint(0, len(constants.materials) - 1)]
                j += 1
            if j >= 15:
                in_list.append(False)

            else:
                in_list.append(True)

        if False in in_list:

            loop_param = 1

            random_idx = randrange(nr_structures_we_have)
            complete_locations, final_platforms, final_pig_positions, final_TNT_positions = choose_structure(random_idx,
                                                                                                             nr_structures_we_have,
                                                                                                             structure_list)
        else:
            loop_param = 0

            f = open("level-%s.xml" % current_level, "w")

            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<Level width ="2">\n')
            f.write('<Camera x="0" y="2" minWidth="20" maxWidth="30">\n')
            f.write('<Birds>\n')
            for i in range(number_birds):  # bird type is chosen using probability table
                f.write('<Bird type="%s"/>\n' % constants.bird_names[str(choose_item(constants.bird_probabilities))])
            f.write('</Birds>\n')
            f.write('<Slingshot x="-8" y="-2.5">\n')
            f.write('<GameObjects>\n')

            for i in complete_locations:
                rotation = 0
                if (i[0] in (3, 7, 9, 11, 13, 20)):
                    rotation = 90
                elif (i[0] == 18):
                    rotation = 225
                elif (i[0] == 19):
                    rotation = 45

                if len(i) == 3:
                    material = constants.materials[
                        randint(0, len(constants.materials) - 1)]  # material is chosen randomly
                if len(i) == 4:
                    material = i[3]  # this is a specific material chosen by us, Amaru/Serpentine designers
                if len(i) == 5:
                    material = i[3]
                    rotation = i[4]

                while [material, constants.block_names[
                    str(i[0])]] in restricted_combinations:  # if material not allowed for block type then pick again
                    material = constants.materials[randint(0, len(constants.materials) - 1)]

                f.write('<Block type="%s" material="%s" x="%s" y="%s" rotation="%s" />\n' % (
                constants.block_names[str(i[0])], material, str(i[1]), str(i[2]), str(rotation)))

            for i in selected_other:
                material = constants.materials[randint(0, len(constants.materials) - 1)]  # material is chosen randomly
                while [material, constants.additional_objects[
                    str(i[0])]] in restricted_combinations:  # if material if not allowed for block type then pick again
                    material = constants.materials[randint(0, len(constants.materials) - 1)]
                if i[0] == '2':
                    facing = randint(0, 1)
                    f.write('<Block type="%s" material="%s" x="%s" y="%s" rotation="%s" />\n' % (
                        constants.additional_objects[i[0]], material, str(i[1]), str(i[2]), str(facing * 90.0)))
                else:
                    f.write('<Block type="%s" material="%s" x="%s" y="%s" rotation="0" />\n' % (
                        constants.additional_objects[i[0]], material, str(i[1]), str(i[2])))

            for i in final_pig_positions:
                if len(i) == 2:
                    f.write(
                        '<Pig type="BasicSmall" material="" x="%s" y="%s" rotation="0" />\n' % (str(i[0]), str(i[1])))
                if len(i) == 3:
                    f.write('<Pig type="%s" material="" x="%s" y="%s" rotation="0" />\n' % (i[2], str(i[0]), str(i[1])))

            for i in final_platforms:
                for j in i:
                    f.write('<Platform type="Platform" material="" x="%s" y="%s" />\n' % (str(j[0]), str(j[1])))

            for i in final_TNT_positions:
                f.write('<TNT type="" material="" x="%s" y="%s" rotation="0" />\n' % (str(i[0]), str(i[1])))

            f.write('</GameObjects>\n')
            f.write('</Level>\n')

            f.close()
