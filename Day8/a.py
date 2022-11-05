def main(inp):
    a = []
    b = []
    count = 0
    for line in inp:
        a.append(line.split('|'))
    b = [l[1].strip().split() for l in a]
    count = len([item for sublist in b for item in sublist if len(item) in [2, 3, 4, 7]])
    print(count)

if __name__=="__main__":
    import os
    with open("Day8/input.txt",'r',newline='\n') as inp:
        main(inp)