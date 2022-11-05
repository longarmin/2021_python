#I consider every initial list item as the parent of big lanternfish "family", thus "sum_family"
def sum_family(a):
    d = [0 for i in range(9)]
    d[int(a)] +=1
    for i in range(256):
        temp = d[8]
        d[8] = d[0]
        for i in range(7):
            d[i] = d[i+1]
        d[6] = d[7] + d[8]
        d[7] = temp
    return(sum(d))

def main(inp):
    line = inp.readline()
    fishes= [int(a) for a in line.split(',')]
    fishes_sum = []
    for m in fishes:
        fishes_sum.append(sum_family(m))
    print(sum(fishes_sum))

if __name__=="__main__":
    import os
    with open("Day6/input.txt",'r',newline='\n') as inp:
        main(inp)