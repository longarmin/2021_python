def b2():
    count=0
    lines=[]
    with open('Day1/input.txt', 'r', newline='\n') as inp:
        for line in inp:

            lines.append(int(line))
        for i in range (3, len(lines)):
            if lines[i-3] < lines[i]:
                count += 1
        print("No. of measurements are larger than the previous measurement:" + str(count))