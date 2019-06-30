'''Neighbors.py:
        Code Challenge:     Define d-neighborhood Neighbors(Pattern, d) .
        Input:              A string Pattern (string = DNA - Text) and an integer d.
        Output:             The collection of strings Neighbors(Pattern, d).

        Checking out "Charging Station: Solving the Frequent Words with Mismatches Problem" to learn about a better
        approach that generalizes the algorithm for finding frequent words without mismatches.
        Goal is to generate the d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose Hamming distance from
        Pattern does not exceed d, to consider only those k-mers that are close to a k-mer in Text, those with Hamming
        distance at most d from this k-mer. calls Neighbors(Pattern, d), a function that generates the d-neighborhood
        of a k-mer Pattern. The function then will generate the d-neighborhood of a k-mer Pattern.

        EXAMPLE:

        To generate Neighbors(CAA,1), first form Neighbors(AA,1) = {AA, CA, GA, TA, AC, AG, AT}.
        The Hamming distance between AA and each of six of these neighbors is 1. Firstly, concatenating C with each of
        these patterns results in six patterns (CAA, CCA, CGA, CTA, CAC, CAG, CAT) that belong to Neighbors(CAA, 1).
        Secondly, concatenating any nucleotide with AA results in four patterns (AAA, CAA, GAA, and TAA) that belong
        to Neighbors(CAA, 1). Thus, Neighbors(CAA, 1) comprises ten patterns.
        '''


__author__      = "Filippo Bergeretti"
__date__        = "29 June 2019"


#pattern = "ACG"
#d = 1
## expected output = CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG




#===================================== MAIN FUNCTION ===========================================#

def Neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()                             # set = 0
    su_neighbors = Neighbors(Suffix(pattern), d)     # suffix sub-function
    for i in su_neighbors:
        if HamDist(pattern[1:], i) < d:
            for x in 'AGCT':
                neighborhood.add(x + i)
        else:
            neighborhood.add(pattern[0] + i)

    return neighborhood


#===================================== AUX FUNCTIONS ===========================================#

def Suffix (pattern):
    '''This function gives the (k-1)-mer obtained after the removal of the first char of the k-mer pattern'''
    pattern_length = len(pattern)
    su_pattern = pattern[1:pattern_length]                          # Sub-setting string without the first character
    return su_pattern

def HamDist(s1, s2):
    ''' Function returning the Hamming distance between equal-length sequences s1 and s2 (DNA, type: str) '''

    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")  # Error handling
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


#=====================================================================================================#
# Result with opening file function, line stripping and data assign:

with open('datasets/dataset_3014_4.txt', 'r+') as file:
    data = [line.rstrip() for line in file]
    pattern = data[0]
    d = int(data[1])
    result = Neighbors(pattern, d)
    resultlist = list(result)
    print("Generating the d-neighborhood of the k-mer Pattern ", pattern)
    print("Results stored in dir: outputs/neighbors_output.txt")
    with open('outputs/neighbors_output.txt', 'w') as out:
        for item in resultlist:
            out.write("%s\n" % item)
