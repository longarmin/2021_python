def cmp(a, b):
    return (a > b) - (a < b)

class basin_check:
    mat = []
    basin_size = 0
    basin_area = []
    def __init__(self, mat):
        self.mat = mat
    def search(self, i, j, last_height):
        current_height = self.mat[i][j]
        #search left of current point:
        if current_height < last_height or current_height == 9 or ((i,j) in self.basin_area):
            return
        self.basin_area.append((i,j))
        self.basin_size += 1
        self.search(i,j-1, current_height)
        #search right of current point:
        self.search(i,j+1, current_height)
        #search upwards of current point:
        self.search(i-1,j, current_height)
        #search downwards of current point:
        self.search(i+1,j, current_height) 


def main(inp):
    import copy
    first = 0
    second = 0
    third = 0
    risklevel = 0
    mat = [list(map(int,(list(line.strip())))) for line in inp]
    nines = [9 for i in mat[1]]
    mat_exp = copy.deepcopy(mat)
    mat_exp.append(copy.deepcopy(nines))
    mat_exp.insert(0, copy.deepcopy(nines))
    for i in mat_exp:
        i.insert(0,9)
        i.append(9)
    basin = basin_check(mat_exp)
    for i in range(1,len(mat_exp)-1):
        for j in range(1,len(mat_exp[i])-1):
            basin.search(i, j, 0)
            if basin.basin_size >= third:
                if basin.basin_size >= second:
                    third = copy.deepcopy(second)
                    if basin.basin_size >= first:
                        second = copy.deepcopy(first)
                        first = copy.deepcopy(basin.basin_size)
                    else:
                        second = copy.deepcopy(basin.basin_size)
                else:
                    third = copy.deepcopy(basin.basin_size)
            basin.basin_size = 0
            basin.basin_area = []
#   1234567890
# 1 2199943210
# 2 3987894921
# 3 9856789892
# 4 8767896789
# 6 9899965678
    print(third)
    print(second)
    print(first)
    print(third * second * first)


if __name__=="__main__":
    import os
    with open("Day9/input.txt",'r',newline='\n') as inp:
        main(inp)