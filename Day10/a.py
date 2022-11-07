def main(inp):
    exp_chars=dict([('(',')'),('[',']'),('[',']'),('{','}'),('<','>')])
    points = {')':3,']':57,'}':1197,'>':25137}
    sum_points = 0
    brackets = []
    opening_brackets=['(','[','{','<']
    closing_brackets=[')',']','}','>']
    for line in inp:
        for char in line:
            if char in opening_brackets:
                brackets.append(char)
            if char in closing_brackets:
                pendant=brackets.pop()
                if char != exp_chars[pendant]:
                    sum_points += points[char]
    print(str(sum_points))

if __name__=="__main__":
    import os
    with open('Day10/input.txt','r',newline='\n') as inp:
        main(inp)