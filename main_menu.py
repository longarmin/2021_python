import sys
import os
# sys.path.append(os.path.abspath("./one"))
import Day1.a
import Day1.b_menu
import Day2.a
import Day2.b

# scriptpath = "./1"
# sys.path.append(os.path.abspath(scriptpath))
# import a as quest1a
# import b_menu as quest1b
# scriptpath = "./2"
# sys.path.append(os.path.abspath(scriptpath))
# import a as quest2a
inp_menu = input("please type in quest number. Synatx:\n(Quest no.(1-25))+(Part no.(a or b))\n\
    examples: 1a, 1b, 12a, 24b, ...")
print("you chose option " + str(inp_menu))
if(inp_menu == '1a'):
    Day1.a.a()
if(inp_menu == '1b'):
    Day1.b_menu.b()
if(inp_menu == '2a'):
    Day2.a.a()
if(inp_menu == '2b'):
    Day2.b.b()