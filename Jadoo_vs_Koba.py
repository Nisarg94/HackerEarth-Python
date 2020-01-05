'''
    Problem:- Jadoo, the space alien has challenged Koba to a friendly duel. 
    He asks Koba to write a program to print out all numbers from 70 to 80. 
    Knowing perfectly well how easy the problem is, the Jadoo adds his own twist to the challenge. 
    He asks Koba to write the program without using a single number in his program and also restricts 
    the character limit to 100.
'''

#Solution
ch = ord('F')
while ch <= ord('P'):
    print(ch)
    ch += ord('B')-ord('A') ## B=65 & A= 64 => B-A=1

### One Liner code
# for i in range(ord('F'),ord('Q')):print(i)

