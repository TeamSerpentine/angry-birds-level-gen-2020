from random import uniform


def choose_item(table):
    ran_num = uniform(0.0, 1.0)
    selected_num = 0
    while ran_num > 0:
        selected_num = selected_num + 1
        ran_num = ran_num - table[str(selected_num)]
    return selected_num
