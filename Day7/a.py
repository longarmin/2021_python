def a():
    import os
    with open('Day7/input.txt', 'r', newline='\n') as inp:
        line = inp.readline()
        arr = [int(a) for a in line.split(',')]
        fuel_consumption = []
        avg = sum(arr)
        for i in range(0, max(arr)):
            fuel = 0
            for pos in arr:
                fuel+=abs(pos-i)
            fuel_consumption.append(fuel)
        # print(fuel_consumption.index(min(fuel_consumption)))
        print(min(fuel_consumption))