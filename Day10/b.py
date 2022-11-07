def main(inp):
    exp_chars=dict([('(',')'),('[',']'),('[',']'),('{','}'),('<','>')])
    points = {'(':1,'[':2,'{':3,'<':4}
    sum_points = 0
    line_points = []
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
                    break
        else:        
            if brackets != []:
                sum_points = 0
                brackets.reverse()
                for bracket in brackets:
                    sum_points *= 5
                    sum_points += points[bracket]
                line_points.append(sum_points)
        brackets = []   
            

    print(str(sorted(line_points)[int(len(line_points)/2)]))

if __name__=="__main__":
    import os
    with open('Day10/input.txt','r',newline='\n') as inp:
        main(inp)