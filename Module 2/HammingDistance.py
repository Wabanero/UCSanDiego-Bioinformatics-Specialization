'''HammingDistance.py:
        Code Challenge:     Compute the Hamming distance between two strings.
        Input:              Two strings of equal length.
        Output:             The Hamming distance between these strings.

        We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi.
        For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called
        the Hamming distance between these strings and is denoted HammingDistance(p, q).'''

__author__      = "Filippo Bergeretti"
__date__        = "09 June 2019"

# Function definition
def HamDist(s1, s2):
    ''' Function returning the Hamming distance between equal-length sequences s1 and s2 (DNA, type: str) '''

    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")  # Error handling
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# Opening file and line stripping
with open('HamDist.txt', 'r') as file:
    c = 1
    s = []
    for line in file:
        single_line = line.strip("\n")
        print("line {} contents {}".format(c, single_line))
        s.append(single_line)
        c += 1
# String setup
print(s,"\n")
s1 = s[0]
s2 = s[1]

# Function calling and printing output
print("The Hamming distance between:\n", str(s1), " and ", str(s2), " is:\t", HamDist(s1, s2))
