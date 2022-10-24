import os
import copy

def b1():
    a = 0
    b = 1
    c = 3
    sum_old=0
    sum=0
    count = 0
    count_loops = 0
    lines=[]
    with open('Day1/input.txt', 'r', newline='\n') as inp:
        for line in inp:
            c = b
            b = a
            a = int(line)
            sum_old = copy.deepcopy(sum)
            sum = a + b + c
            if (count_loops < 2):
                pass
            elif (count_loops == 2):
                print(str(sum) + "(N/A - no previous number)")
            elif (sum < sum_old):
                print(str(sum) + "(decreased)")
            elif (sum > sum_old):
                print(str(sum) + "(increased)")
                count += 1
            count_loops += 1
        print("No. of measurements are larger than the previous measurement:" + str(count))