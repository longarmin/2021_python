wins = []
win_nums = []
def strtoint(instr):
    if len(instr) != 15:
        print('wrong str len...\n')
    else:
        outstr = []
        for i in range(0,15,3):
            outstr.append(int(instr[i]+instr[i+1]))
    return outstr

def calc_result(currentset, num):
    for line in currentset:
        for i,x in enumerate(line):
            if x == 100:
                line[i]=0
    sum_left_nums = sum([sum(x) for x in currentset])
    solution = sum_left_nums * num
    print("Solution Day 4b: " + str(solution))

def calc_col_win(currentset, num):
    colsum = [0 for x in range(5)]
    for j in range(5):
        for line in currentset:
            colsum[j] += line[j]
            if colsum[j] == 500:
                return True
    return False


def main(inp):
    import copy
    draw = 0
    draw_str = ''
    global last_win
    global win_nums

    draw_str = inp.readline() 
    draw = list(map(int,draw_str.split(',')))
    i = 0
    sets = []
    for line in inp:
        if line == '\n':
            sets.append([])
        else:
            sets[-1].append(strtoint(line))
    for num in draw:
        for k, currentset in enumerate(sets):
            if k in wins:
                continue
            for line in currentset:
                for i,x in enumerate(line):
                    if x == num:
                        line[i] = 100
                if (sum(line) == 500):
                    wins.append(k)
                    win_nums.append(num)
                    break
                elif calc_col_win(currentset, num) == True:
                    wins.append(k)
                    win_nums.append(num)
                    break
                else:
                    continue
                break
                                    
    calc_result(sets[wins[-1]], win_nums[-1])

if __name__=="__main__":
    import os
    with open("Day4/input.txt",'r',newline='\n') as inp:
        main(inp)