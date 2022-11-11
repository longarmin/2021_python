class flashing_oct:
    mat = []
    mat_flags = []
    count = 0

    def adjacent_8(self, x: int, y: int):
        yield x - 1, y + 1
        yield x - 1, y
        yield x -1, y - 1
        yield x, y -1
        yield x + 1, y - 1
        yield x + 1, y
        yield x + 1, y + 1
        yield x, y + 1

    def blink(self, i, j):
        self.mat[i][j] = 0
        self.mat_flags[i][j] = 1
        self.count += 1
        for x, y in self.adjacent_8(i, j):
            try:
                if x < 0 or y < 0:
                    continue
                elif self.mat_flags[x][y] == 0:
                    self.mat[x][y] += 1
                    if self.mat[x][y] > 9:
                        self.blink(x, y)
            except IndexError:
                pass

    def step1(self):
        for line in self.mat:
            for i in range(len(line)):
                line[i] += 1
    
    def step2(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j] > 9:
                    self.blink(i, j)
    
    def check_sync(self):
        last_val = self.mat[-1][-1]
        for i in self.mat:
            for j in i:
                if j != last_val:
                    return False
        return True

def main(inp):
    count_steps = 0
    o = flashing_oct()
    o.mat = [list(map(int,(list(line.strip())))) for line in inp]
    o.mat_flags = [[0 for j in range(len(o.mat))] for i in range(len(o.mat[0]))]
    while True:
        o.step1()
        o.step2()
        o.mat_flags = [[0 for i in line] for line in o.mat_flags]
        count_steps += 1
        if o.check_sync():
            print(count_steps)
            break

if __name__ == "__main__":
    import os 
    with open("Day11/input.txt",'r',newline='\n') as inp:
        main(inp)