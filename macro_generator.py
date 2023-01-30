from macros import *

fossils = input("How many fossils?: ")
check_box = input("Automate box-checking at the end? (y/n): ")
if check_box.lower == "Y":
    box_num = input("What box # to check? ")
else:
    box_num = -1

# macro_string represents
macro_string = ""
macro_string += launch_title

main_loop = """
LOOP {fossils}
"""
xd = walk_to_counter.split('\n')
print(xd)
