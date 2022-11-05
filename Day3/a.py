def main(inp):
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

    gamma=[0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon=[1,1,1,1,1,1,1,1,1,1,1,1]
    for i in range(len(gamma)):
        if count1s[i] > count0s[i]:
            gamma[i]=1
            epsilon[i]=0
    dec_gamma = 0
    dec_epsilon = 0
    for i in range(len(gamma)):
        dec_gamma   += pow(2, (len(gamma)  -1-i)) * gamma[i]
        dec_epsilon += pow(2, (len(epsilon)-1-i)) * epsilon[i]
    print("power consumption (gamma * epsilon) = " + str(dec_gamma*dec_epsilon))

if __name__=="__main__":
    import os
    with open("Day3/input.txt",'r',newline='\n') as inp:
        main(inp)