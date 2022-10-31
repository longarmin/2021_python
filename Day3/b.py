def process_inp(cnt_oxy_or_co2, print_string):   
    lines = []
    with open('Day3/input.txt', 'r', newline='\n') as inp:
        i=0
        for line in inp:
            lines.append(line)
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

def b():
    import os
    with open('Day3/input.txt', 'r', newline='\n') as inp:
        count0s=[0 for _ in range(12)]
        count1s=[0 for _ in range(12)]
        temp=[]
        i=0
        for line in inp:
            i=0
            while (line[i] != '\n'):
                if line[i]=='1':
                    count1s[i]+=1
                elif line[i]=='0':
                    count0s[i]+=1
                else:
                    print("Failed to interpret sign in line: " + str(line[i]))
                    break
                i+=1
                if i>=len(line):
                    break

        print("Final count of 1s: " + str(count1s))
        gamma=''
        epsilon=''
        for i in range(len(count1s)):
            if count1s[i] > count0s[i]:
                gamma+='1'
                epsilon+='0'
            else:
                gamma+='0'
                epsilon+='1'
        print("gamma = " + str(gamma) + " epsilon = " + str(epsilon))
        dec_gamma = int(gamma,2)
        dec_epsilon = int(epsilon,2)
        print("gamma decimal = " + str(dec_gamma))
        print("epsilon decimal = " + str(dec_epsilon))
        print("power consumption (gamma * epsilon) = " + str(dec_gamma * dec_epsilon))

    oxy = process_inp('oxygen_cnt_major', "Oxygen Generator: ")
    co2 = process_inp('co2scrubber_cnt_minor', "CO2 scrubber: ")
    print("life support rating (oxygen rate * CO2 scrubber rate) = " + str(oxy * co2))
