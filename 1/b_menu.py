def b():
    import b_1
    import b_2

    inp_menu = input("please choose option:\n-first idea w/ output: press 1 + Enter\n-2nd idea for performance: press 2 + Enter\n")
    print("you chose option " + str(inp_menu))
    if(inp_menu == '1'):
        b_1.b1()
    if(inp_menu == '2'):
        b_2.b2()