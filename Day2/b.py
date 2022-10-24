class position:
    x = 0
    y = 0
    aim = 0
    def product(self):
        return (self.x*self.y)
    def calc_delta_depth(self, dx):
        return (dx*self.aim)
def b():
    import os
    with open('Day2/input.txt', 'r', newline='\n') as inp:
        temp=[]
        pos = position()
        for line in inp:
            temp = line.split()
            if temp[0]=="up":
                pos.aim-=int(temp[1])
            if temp[0]=="down":
                pos.aim+=int(temp[1])
            if temp[0]=="forward":
                pos.x+=int(temp[1])
                pos.y+=int(pos.calc_delta_depth(int(temp[1])))
        print("Final Position: (" + str(pos.x) + ", " + str(pos.y) + "),\nProduct x * y = " + str(pos.product()))

b()