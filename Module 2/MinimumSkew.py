'''MinimumSkew.py:
        Code Challenge:     Solve the Minimum Skew Problem.
        Input:              A DNA string Genome.
        Output:             All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

        Since we don't know the location of ori in a circular genome, let's linearize it (i.e., select an arbitrary
        position and pretend that the genome begins here), resulting in a linear string Genome. We define Skewi(Genome)
        as the difference between the total number of occurrences of G and the total number of occurrences of C in the
        first i nucleotides of Genome. The skew diagram is defined by plotting Skewi (Genome) (as i ranges from 0 to
        |Genome|), where Skew0 (Genome) is set equal to zero. Note that we can compute Skewi+1(Genome) from
        Skewi(Genome) according to the nucleotide in position i of Genome.
        If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1;
        if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1;
        otherwise, Skewi+1(Genome) = Skewi(Genome).
        An insight for a new algorithm for locating ori: it should be found where the skew attains a minimum.'''

# Function definition
def Min_skew(sequence):
    c = 0
    g = 0
    minimum_skew = 0
    skew_list = []
    index = 0
    for i in sequence:  # Looping i nucleotides in sequence
        index += 1
        if i == 'C':    # if this nucleotide is C, add 1 to C counter
            c += 1
        if i == 'G':    # If this nucleotide is G, add 1 to G counter
            g += 1

        skew = g - c    # Skewi(Genome)is the difference between the total number of Gs and Cs
                        # in the first i nucleotides of Genome.

        if skew < minimum_skew:                                 # If n(Gs) > n(Cs) due to citosine deamination
            skew_list = [index]
            minimum_skew = skew
        if skew == minimum_skew and index not in skew_list:     # Where the skew attains a minimum.
            skew_list.append(index)
    return skew_list


# Opening data file (*.txt / *.fasta)
with open('dataset_7_6.txt', 'r') as in_file:
    sequence = in_file.readline()
    result = Min_skew(sequence)
    print(result)                                               # Result as list
