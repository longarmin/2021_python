def b():
    import os
    with open('Day7/input.txt', 'r', newline='\n') as inp:
        line = inp.readline()
        arr = [int(a) for a in line.split(',')]
        fca = [pos for pos in range(max(arr)+1)]
        fuel_consumption = []
        avg = sum(arr)
        for i in range(0, max(arr)):
            fuel = 0
            for pos in arr:
                fuel+=sum(fca[0:abs(pos-i)+1])
            fuel_consumption.append(fuel)
        print(min(fuel_consumption))