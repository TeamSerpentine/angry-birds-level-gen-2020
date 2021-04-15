# blocks number and size
blocks = {'1': [0.84, 0.84], '2': [0.85, 0.43], '3': [0.43, 0.85], '4': [0.43, 0.43],
          '5': [0.22, 0.22], '6': [0.43, 0.22], '7': [0.22, 0.43], '8': [0.85, 0.22],
          '9': [0.22, 0.85], '10': [1.68, 0.22], '11': [0.22, 1.68],
          '12': [2.06, 0.22], '13': [0.22, 2.06],
          '14': [0.82, 0.82], '15': [0.82, 0.82], '16': [0.8, 0.8], '17': [0.45, 0.45],
          '18': [0.82, 0.82], '19': [0.82, 0.82], '20': [0.82, 0.82]}

block_names = {'1': "SquareHole", '2': "RectFat", '3': "RectFat", '4': "SquareSmall",
               '5': "SquareTiny", '6': "RectTiny", '7': "RectTiny", '8': "RectSmall",
               '9': "RectSmall", '10': "RectMedium", '11': "RectMedium",
               '12': "RectBig", '13': "RectBig",
               '14': "TriangleHole", '15': "Triangle", '16': "Circle", '17': "CircleSmall",
               '18': "Triangle", '19': "Triangle", '20': "Triangle"}

additional_objects = {'1': "TriangleHole", '2': "Triangle", '3': "Circle", '4': "CircleSmall"}

# additional objects number and size
additional_object_sizes = {'1': [0.82, 0.82], '2': [0.82, 0.82], '3': [0.8, 0.8], '4': [0.45, 0.45]}

# blocks number and probability of being selected
probability_table_blocks = {'1': 0.10, '2': 0.10, '3': 0.10, '4': 0.05,
                            '5': 0.02, '6': 0.05, '7': 0.05, '8': 0.10,
                            '9': 0.05, '10': 0.16, '11': 0.04,
                            '12': 0.16, '13': 0.02}

# materials that are available
materials = ["wood", "stone", "ice"]

# bird types number and name
bird_names = {'1': "BirdRed", '2': "BirdBlue", '3': "BirdYellow", '4': "BirdBlack", '5': "BirdWhite"}

# bird types number and probability of being selected
bird_probabilities = {'1': 0.35, '2': 0.2, '3': 0.2, '4': 0.15, '5': 0.1}

TNT_block_probability = 0.4  # 0.3

pig_size = [0.5, 0.5]  # size of pigs
# pig_size = [2.0, 2.0]  # bigger size of bigs to prevent overlap with pigs of type BasicBig (1.0 is an estimate by Bram)

platform_size = [0.62, 0.62]  # size of platform sections

edge_buffer = 0.11  # buffer uesd to push edge blocks further into the structure center (increases stability)

absolute_ground = -3.5  # the position of ground within level

max_peaks = 5  # maximum number of peaks a structure can have (up to 5)
min_peak_split = 10  # minimum distance between two peak blocks of structure
max_peak_split = 50  # maximum distance between two peak blocks of structure

minimum_height_gap = 3.5  # y distance min between platforms
platform_distance_buffer = 0.4  # x_distance min between platforms / y_distance min between platforms and ground structures

# defines the levels area (ie. space within which structures/platforms can be placed)
level_width_min = -3.0
level_width_max = 9.0
level_height_min = -2.0  # only used by platforms, ground structures use absolute_ground to determine their lowest point
level_height_max = 6.0

pig_precision = 0.01  # how precise to check for possible pig positions on ground

min_ground_width = 2.5  # minimum amount of space allocated to ground structure
ground_structure_height_limit = ((
                                         level_height_max - minimum_height_gap) - absolute_ground) / 1.5  # desired height limit of ground structures

max_attempts = 40  # number of times to attempt to place a platform before abandoning it
