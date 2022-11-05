import sys
import os
import importlib

inp_menu = input("please type in quest number. Synatx:\n(Quest no.(1-25))+(Part no.(a or b))\n\
    examples: 1a, 1b, 12a, 24b, ...\n")
print("you chose option " + str(inp_menu))
temp = list(inp_menu)
d = "Day" + temp[0] + "." + temp[1]
day_module = importlib.import_module(d)
# inp_file="day" 
with open("Day"+temp[0]+"/input.txt", 'r',newline='\n') as inp:
    day_module.main(inp)