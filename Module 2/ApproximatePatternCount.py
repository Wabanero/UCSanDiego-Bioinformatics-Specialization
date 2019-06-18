'''ApproximatePatternCount.py:
        Code Challenge:     Implement ApproximatePatternCount.
        Input:              Strings Pattern and Text (both DNA sequences) as well as an integer d.
        Output:             Countd(Text, Pattern): it simply requires us to compute the Hamming distance between Pattern
                            and every k-mer substring of Text, which is achieved by the following pseudocode.

        We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer
        substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern')
        ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization
        of the Pattern Matching Problem.'''

__author__      = "Filippo Bergeretti"
__date__        = "17 June 2019"

# Sample Input:
#
# pattern = "ATA"
# text = "ATA"
# d = 0


# Main function
def Countd(text, pattern, d):
    slider = len(text) - len(pattern)
    i = 0
    count = 0
    for i in range(0,slider + 1):                           # + 1 after debugging by printing sub-steps in the for loop
        pattern_loop = text[i:(i + len(pattern))]
        print("scrolling frame: ", str(pattern_loop))       # Debugging purposes
        if HamDist(pattern, pattern_loop) <= d:
            count += 1
    i += 1
    return count

# Hamming Distance sub-function
def HamDist(pattern, pattern_loop):
    if len(pattern) != len(pattern_loop):
        raise ValueError("Undefined for sequences of unequal length")  # Error handling
    dist = sum(ch1 != ch2 for ch1, ch2 in zip(pattern, pattern_loop))
    return dist


# Result with opening file function, line stripping and data assign:
with open('datasets/dataset_9_6.txt', 'r+') as file:
    data = [line.rstrip() for line in file]
    text = data[1]
    pattern = data[0]
    d = int(data[2])

    result = Countd(text, pattern, d)
    print("\n\nDna sequence: \n", text)
    print("Pattern: \n", pattern)
    print("Mismatch limit: \n", d)
    print("\n=================================================================")
    print("Number of occurrences of ", str(pattern), " in ",str(text) ," with at most ", str(d), " mismatches is: ", result)
