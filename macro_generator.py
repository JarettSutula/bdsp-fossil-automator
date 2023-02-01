from macros import *
from util import *

fossils = input("How many fossils?: ")
check_box = input("Automate box-checking at the end? (y/n): ")
if check_box.lower == "Y":
    box_num = input("What box # to check? ")
else:
    box_num = -1

# var to represent entire macro result in a list.
main_loop = []

# title launch does not need to be looped and therefore not indented.
main_loop += macro_to_list(launch_title)

# based on the number of fossils inputted, start a loop.
# counter -> drop off -> outside -> counter -> pick up -> drop off -> outside
loop_str = "LOOP {}".format(fossils)
main_loop.append(loop_str)


