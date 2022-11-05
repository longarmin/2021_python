import sys
import os

import Day1.a
import Day1.b_menu
import Day2.a
import Day2.b
import Day3.a
import Day3.b
import Day4.a
import Day4.b
import Day5.a
import Day5.b
import Day6.a
import Day6.b
import Day7.a
import Day7.b
import Day8.a
import Day8.b

inp_menu = input("please type in quest number. Synatx:\n(Quest no.(1-25))+(Part no.(a or b))\n\
    examples: 1a, 1b, 12a, 24b, ...\n")
print("you chose option " + str(inp_menu))
if(inp_menu == '1a'):
    Day1.a.a()
if(inp_menu == '1b'):
    Day1.b_menu.b()
if(inp_menu == '2a'):
    Day2.a.a()
if(inp_menu == '2b'):
    Day2.b.b()
if(inp_menu == '3a'):
    Day3.a.a()
if(inp_menu == '3b'):
    Day3.b.b()
if(inp_menu == '4a'):
    Day4.a.a()
if(inp_menu == '4b'):
    Day4.b.b()
if(inp_menu == '5a'):
    Day5.a.a()
if(inp_menu == '5b'):
    Day5.b.b()
if(inp_menu == '6a'):
    Day6.a.a()
if(inp_menu == '6b'):
    Day6.b.b()
if(inp_menu == '7a'):
    Day7.a.a()
if(inp_menu == '7b'):
    Day7.b.b()
if(inp_menu == '8a'):
    Day8.a.a()
if(inp_menu == '8b'):
    Day8.b.b()