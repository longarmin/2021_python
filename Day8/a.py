def a():
    import os
    import numpy as np

    with open('Day8/input.txt', 'r', newline='\n') as inp:
        a = []
        b = []
        count = 0
        for line in inp:
            a.append(line.split('|'))
        b = [l[1].strip().split() for l in a]
        # flat_list = [item for sublist in b for item in sublist if len(item) in [1, 2, 3, 4, 7]]
        count = len([item for sublist in b for item in sublist if len(item) in [2, 3, 4, 7]])
        print(count)
