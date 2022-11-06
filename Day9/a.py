def main(inp):
    import copy
    risklevel = 0
    mat = [list(map(int,(list(line.strip())))) for line in inp]
    nines = [9 for i in mat[1]]
    mat_exp = copy.deepcopy(mat)
    mat_exp.append(copy.deepcopy(nines))
    mat_exp.insert(0, copy.deepcopy(nines))
    for i in mat_exp:
        i.insert(0,9)
        i.append(9)
    for i in range(1,len(mat_exp)-1):
        for j in range(1,len(mat_exp[i])-1):
            left  = mat_exp[i][j] - mat_exp[i][j-1]
            right = mat_exp[i][j] - mat_exp[i][j+1]
            up    = mat_exp[i][j] - mat_exp[i-1][j]
            down  = mat_exp[i][j] - mat_exp[i+1][j]
            if (left < 0) and (right < 0) and (up < 0) and (down < 0):
                risklevel += (mat_exp[i][j] + 1)
    print(risklevel)


if __name__=="__main__":
    import os
    with open("Day9/input.txt",'r',newline='\n') as inp:
        main(inp)