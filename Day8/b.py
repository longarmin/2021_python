class decoder:
    codes = []
    decoded_digits = []
    decoded_digits_int = 0
    letter_count = {}
    letters=['a','b','c','d','e','f','g']
    def check_input(self, inp, digits):
        self.letter_count = {}
        self.codes = inp
        self.digits = digits
        self.count_letters()
        self.decode_digits()
        self.decoded_digits_int=0
        self.decoded_digits.reverse()
        for i,num in enumerate(self.decoded_digits):
            self.decoded_digits_int += pow(10,i)*num
        return self.decoded_digits_int
    def letter_cnt_sum(self, code):
        letter_cnt_sum = 0
        for letter in code:
            letter_cnt_sum += self.letter_count[letter]
        return letter_cnt_sum
    def count_letters(self):
        for letter in self.letters:
            self.letter_count[letter]=0
            for code in self.codes:
                if (letter in code):
                    self.letter_count[letter]+=1
    def decode_digits(self):
        self.decoded_digits = []
#                            binary codes of segments
#===================================================================
# Number	No of Segments	|a	b	c	d	e	f	g|		Dec	|letter_cnt_sum(=no of letter occurence * binary code of segment)
#   1             2	        |0	1	1	0	0	0	0|		48	|17
#   7             3	        |1	1	1	0	0	0	0|		112	|25
#   4             4	        |0	1	1	0	0	1	1|		51	|30
#   5             5	        |1	0	1	1	0	1	1|		91	|37
#   2             5	        |1	1	0	1	1	0	1|		109	|34
#   3             5	        |1	1	1	1	0	0	1|		121	|39
#   6             6	        |1	0	1	1	1	1	1|		95	|41
#   9             6	        |1	1	1	1	0	1	1|		123	|45
#   0             6	        |1	1	1	1	1	1	0|		126	|42
#   8             7	        |1	1	1	1	1	1	1|		127	|49
#	=================================================================
#no of letter occurences:	|8	8	9	7	4	6	7|	
        for code in self.digits:
            letter_cnt_sum = self.letter_cnt_sum(code)
            if len(code) == 2:
                self.decoded_digits.append(1)
            elif len(code) == 3:
                self.decoded_digits.append(7)
            elif len(code) == 4:
                self.decoded_digits.append(4)
            elif len(code) == 7:
                self.decoded_digits.append(8)
            elif letter_cnt_sum == 34:
                    self.decoded_digits.append(2)
            elif letter_cnt_sum == 37:
                    self.decoded_digits.append(5)
            elif letter_cnt_sum == 39:
                    self.decoded_digits.append(3)
            elif letter_cnt_sum == 41:
                    self.decoded_digits.append(6)
            elif letter_cnt_sum == 42:
                    self.decoded_digits.append(0)
            elif letter_cnt_sum == 45:
                    self.decoded_digits.append(9)
		
def b():
    import os
    import numpy as np

    with open('Day8/input.txt', 'r', newline='\n') as inp:
        a = []
        m = decoder()
        res = 0
        for line in inp:
            a.append(line.split('|'))
        for l in a:
            l[0]=l[0].split()
            l[1]=l[1].strip().split()
        for i in range(len(a)):
            res += m.check_input(a[i][0],a[i][1])  
        print(res)