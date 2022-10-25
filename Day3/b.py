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
        count0s=[0,0,0,0,0,0,0,0,0,0,0,0]
        count1s=[0,0,0,0,0,0,0,0,0,0,0,0]
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
        gamma=[0,0,0,0,0,0,0,0,0,0,0,0]
        epsilon=[1,1,1,1,1,1,1,1,1,1,1,1]
        for i in range(len(gamma)):
            if count1s[i] > count0s[i]:
                gamma[i]=1
                epsilon[i]=0
        print("gamma = " + str(gamma) + "epsilon = " + str(epsilon))
        dec_gamma = 0
        dec_epsilon = 0
        for i in range(len(gamma)):
            dec_gamma   += pow(2, (len(gamma)  -1-i)) * gamma[i]
            dec_epsilon += pow(2, (len(epsilon)-1-i)) * epsilon[i]
        print("gamma decimal = " + str(dec_gamma))
        print("epsilon decimal = " + str(dec_epsilon))
        print("power consumption (gamma * epsilon) = " + str(dec_gamma*dec_epsilon))

    lines = []
    with open('Day3/input.txt', 'r', newline='\n') as inp:
        i=0
        for line in inp:
            lines.append(line)
        for i in range(12):
            if(len(lines) <= 1):
                break
            lines2 = del_lines(lines, i, 'oxygen_cnt_major')
            lines.clear()
            lines = lines2
        oxy = int(lines[0],2)
        print("oxygen generator:" + str(oxy))
        lines.clear()
    with open('Day3/input.txt', 'r', newline='\n') as inp:
        for line in inp:
            lines.append(line)
        for i in range(12):
            if(len(lines) <= 1):
                break
            lines2 = del_lines(lines, i, 'co2scrubber_cnt_minor')
            lines.clear()
            lines = lines2
        co2 = int(lines[0],2)
        print("CO2 scrubber: " + str(co2))
    print("life support rating (oxygen rate * CO2 scrubber rate) = " + str(oxy * co2))

b()