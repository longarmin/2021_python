def process_inp(lines, cnt_oxy_or_co2, print_string):   
    i=0
    for i in range(12):
        if(len(lines) <= 1):
            break
        lines2 = del_lines(lines, i, cnt_oxy_or_co2)
        lines.clear()
        lines = lines2
    result = int(lines[0],2)
    lines.clear()
    print(print_string + str(result))
    return result

def del_lines(inp, i, mode): #does not work w/ gamma since list is modified each cycle
    if mode=='oxygen_cnt_major':
        focus_val = '1'
        nfocus_val = '0'
    elif mode=='co2scrubber_cnt_minor':
        focus_val = '0'
        nfocus_val = '1'
    outp=[]
    count1s = 0
    count0s = 0
    for line in inp:
        if line[i] == '0':
            count0s += 1
        elif line[i] == '1':
            count1s += 1
    if count0s <= count1s:
        for line in inp:
            if line[i] == focus_val:
                outp.append(line)
            else:
                pass
    if count1s < count0s:
        for line in inp:
            if line[i] == nfocus_val:
                outp.append(line)
            else:
                pass 
    return outp   

def main(inp):
    import copy
    lines = []
    for line in inp:
        lines.append(line)
    lines2 = copy.deepcopy(lines)
    
    oxy = process_inp(lines, 'oxygen_cnt_major', 'Oxygen Generator: ')
    co2 = process_inp(lines2, 'co2scrubber_cnt_minor', "CO2 scrubber: ")
    print("life support rating (oxygen rate * CO2 scrubber rate) = " + str(oxy * co2))

if __name__=="__main__":
    import os
    with open("Day3/input.txt",'r',newline='\n') as inp:
        main(inp)