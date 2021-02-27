# area calculator
# to determine the number of cans of paint required to cover a wall.
# 1 can of paint can cover 5 square meters

import math


def paint_cans_required(height, width, cover):
    # cans_needed = (height * width) / cover
    cans_needed = math.ceil((height * width) / cover)
    print(f"paint cans required = {round(cans_needed)}")


test_h = int(input("Height of the wall:  "))
test_w = int(input("Width of the wall:  "))
coverage = 5
paint_cans_required(height=test_h, width=test_w, cover=coverage)
