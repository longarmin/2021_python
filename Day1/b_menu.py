def main(inp):
    import b_1
    import b_2

    inp_menu = input("please choose option:\n-first idea w/ output: press 1 + Enter\n-2nd idea for performance: press 2 + Enter\n")
    print("you chose option " + str(inp_menu))
    if(inp_menu == '1'):
        b_1.b1(inp)
    if(inp_menu == '2'):
        b_2.b2(inp)

if __name__=="__main__":
    import os
    with open("Day1/input.txt",'r',newline='\n') as inp:
        main(inp)