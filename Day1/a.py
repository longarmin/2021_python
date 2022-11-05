def main(inp):
    b = 0
    count = 0
        
    for line in inp:
        a = int(line)
        if (b == 0):
            print(str(a) + "(N/A - no previous number)")
        elif (a < b):
            print(str(a) + "(decreased)")
        elif (a > b):
            print(str(a) + "(increased)")
            count += 1
        b = a
    print("No. of measurements are larger than the previous measurement:" + str(count))

if __name__=="__main__":
    import os
    with open("Day1/input.txt",'r',newline='\n') as inp:
        main(inp)