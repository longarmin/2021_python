class fishes:
    fishlife = []
    fish_age = []
    def next_day(self, i):
        if self.fishlife[i] > 0:
            self.fishlife[i] -= 1
        else:
            self.fishlife[i] = 6
            self.fishlife.append(8)

def a():
    import os
    with open('Day6/testinput.txt', 'r', newline='\n') as inp:
        f = fishes()
        line = inp.readline()
        f.fishlife = [int(a) for a in line.split(',')]
        for day in range(256):
            for i in range(len(f.fishlife)):
                f.next_day(i)
        print(len(f.fishlife))

a()