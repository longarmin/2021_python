import math
class pipes:
    dots_mat = []
    def cmp(self, a, b):
        return (a > b) - (a < b)
    def drawpath(self, x1, y1, x2, y2):
        x = int(x1)
        y = int(y1)
        self.dots_mat[y][x] += 1
        while(True):
            y += int(self.cmp(y2, y1))
            x += int(self.cmp(x2, x1))
            self.dots_mat[y][x] += 1
            if (y == y2) and (x == x2):
                break

    def b(self, inp):
        vec = []
        allp = []
        for line in inp:
            line = line.strip()
            vec = line.split(' -> ')
            x1, y1 = vec[0].split(',')
            x2, y2 = vec[1].split(',')
            pos=[int(x1), int(y1), int(x2), int(y2)]
            allp.append(pos)
        maxim = int(max([item for list in allp for item in list]))
        self.dots_mat = [[0 for i in range(maxim+1)] for j in range(maxim+1)]
        for pos in allp:
            self.drawpath(pos[0],pos[1],pos[2],pos[3])
        s = 0
        for line_list in self.dots_mat:
            for point in line_list:
                if point >1:
                    s+=1
        print("Result 5b: " + str(s))

def main(inp):
    inst = pipes()
    inst.b(inp)

if __name__=="__main__":
    import os
    with open("Day5/input.txt",'r',newline='\n') as inp:
        main(inp)