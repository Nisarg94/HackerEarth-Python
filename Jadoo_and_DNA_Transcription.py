'''
Problem:- Jadoo, the Space Alien has befriended Koba upon landing on Earth. Since then, he wishes Koba to be more like him. 
In order to do so he decides to slowly transcribe Koba's DNA into RNA. But he has to write a very short code in order to do the 
transcription so as not to make Koba aware of the change.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
G --> C
C --> G
T --> A
A --> U
'''

def DNA_Transcription(self, arg1):
    if (arg1 == 'G'):
        return 'C'
    elif (arg1 == 'C'):
        return 'G'
    elif (arg1 == 'T'):
        return 'A'
    elif (arg1 == 'A'):
        return 'U'

if __name__ == "__main__":
    b = input()
    DNA_Transcription(b)