from macros import *
from util import *

fossils = int(input("How many fossils?: "))
check_box_input = input("Automate box-checking at the end? (y/n): ")
if check_box_input.lower() == "y":
    box_num = int(input("What box # to check? "))
else:
    box_num = -1

# var to represent entire macro result in a list.
main_loop = []

# title launch does not need to be looped and therefore not indented.
# some strange nxbt things happen after waiting a while - more stability if
# the macro is just run at the right place and not from the menu.
# main_loop += macro_to_list(launch_title)

# drop off first fossil (counter -> drop off -> outside)
main_loop += macro_to_list(walk_to_counter)
main_loop += macro_to_list(drop_off_fossil_text)
main_loop += macro_to_list(walk_outside)

# based on the number of fossils inputted, start a loop.
# counter -> pick up -> drop off -> outside
loop_str = "LOOP {}".format(fossils-1)
main_loop.append(loop_str)

# in-loop pieces
counter = add_indent_to_macro(walk_to_counter)
drop = add_indent_to_macro(drop_off_fossil_text)
pick = add_indent_to_macro(pick_up_fossil_text)
outside = add_indent_to_macro(walk_outside)

# order loop pieces
in_loop = [counter, pick, drop, outside]
for mcro in in_loop:
    main_loop += mcro

# once loop is done, pick up last fossil (no drop off!)
main_loop += macro_to_list(walk_to_counter)
main_loop += macro_to_list(pick_up_fossil_text)

# add box checking if desired from previous input
if box_num != -1:
    main_loop += macro_to_list(check_box)
    # check which box to go to. If it's not box 1, loop. Otherwise just let it go.
    if box_num > 1:
        box_loop = ["LOOP {}".format(box_num-1), "    R 0.1s", "    0.3s"]
        main_loop += box_loop

# add delay at last line
main_loop += ["0.5s"]

# place contents of main_loop into a text file for easy copy/pasting into NXBT.
with open('bdsp_macro.txt', 'w') as f:
    for line in main_loop:
        f.write(f"{line}\n")
