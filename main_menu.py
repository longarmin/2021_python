import sys
import os
# sys.path.append(os.path.abspath("./one"))
scriptpath = "./1"
sys.path.append(os.path.abspath(scriptpath))
import a as quest1a
import b_menu as quest1b
inp_menu = input("please type in quest number. Synatx:\n(Quest no.(1-25))+(Part no.(a or b))\n")
print("you chose option " + str(inp_menu))
if(inp_menu == '1a'):
    quest1a.a()
if(inp_menu == '1b'):
    quest1b.b()