class pipes:
    dots_mat = []
    def drawpath(self, x1, y1, x2, y2):
        if x1 == x2:
            for i in range(min(y1,y2),max(y1,y2)+1):
                self.dots_mat[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1,x2),max(x1,x2)+1):
                self.dots_mat[y1][i] += 1
        
            
    def a(self, inp):
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
        print("Result 5a: " + str(s))

def main(inp):
    inst = pipes()
    inst.a(inp)

if __name__=="__main__":
    import os
    with open("Day5/input.txt",'r',newline='\n') as inp:
        main(inp)