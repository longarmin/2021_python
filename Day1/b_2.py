def b2(inp):
    count=0
    lines=[]
    for line in inp:

        lines.append(int(line))
    for i in range (3, len(lines)):
        if lines[i-3] < lines[i]:
            count += 1
    print("No. of measurements are larger than the previous measurement:" + str(count))

if __name__=="__main__":
    import os
    with open("Day1/input.txt",'r',newline='\n') as inp:
        b2(inp)