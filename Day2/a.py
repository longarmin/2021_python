class position:
    x = 0
    y = 0
    def product(self):
        return (self.x*self.y)
def a():
    import os
    with open('Day2/input.txt', 'r', newline='\n') as inp:
        temp=[]
        pos = position()
        for line in inp:
            temp = line.split()
            if temp[0]=="up":
                pos.y-=int(temp[1])
            if temp[0]=="down":
                pos.y+=int(temp[1])
            if temp[0]=="forward":
                pos.x+=int(temp[1])
        print("Final Position: (" + str(pos.x) + ", " + str(pos.y) + "),\nProduct x * y = " + str(pos.product()))