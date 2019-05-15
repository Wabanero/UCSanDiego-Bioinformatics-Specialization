"""PatternCount.py:
        Code Challenge, implement PatternCount algorithm(reproduced below).
        Input: Strings Text and Pattern.
        Output: Count(Text, Pattern)."""

__author__      = "Filippo Bergeretti"
__date__        = "14 May 2019"

# No import function, *.txt file is generated each session, here i just copypaste the DNA sequences (not FASTA format)

text     = 'ATTGGACAGTAAGACAGTAGACAGTAGCCATTCGACAGTACTGTTGACAGTAACCATAGACAGTAGACAGTAACGACAGTAGACAGTACATTATGACAGTATATTCGACAGACAGTACAAGACAGTAGGAGCGACAGTAGCGACAGTAGACAGTAGACAGTACTGACAGTAGACAGTAGTGACAGTAGACAGTAGACAGTAGACAGTAGACAGTATCATGACAGTAGACAGTAGACAGTAGAGGTGTCTGACAGTAGACAGTATTAGACAGTAGACAGTATTCAGAGGACAGTAATCGTCCATTGACAGTAGACAGTAGACAGTACGACAGTAGACAGTAGACAGTAGCGACAGTAGACAGTACGACAGTACAAATGGATCGGACAGTACGACAGTACAAGACAGTAGACAGTACTTGGGCTCCGGGCGACAGTACATTGGATGGGGGACAGTAGGCGACAGTAGACAGTAGACAGTAGACAGTAGACAGTACCTATAGACAGTAAGACAGTAGTGGTGACAGTAGACAGTAGACAGTACTCCTGACAGTAGCAGACAGTAGCTACGTTCACTGACAGTATGACAGTACCATTGACAGTACACAAACGACAGTAGACAGTAGGACAGTAACATGAGGACAGTAGACAGTAAGAGAAGACAGTAGTAGGCGCATAAATACGACAGTAGGACAGTACATGACAGTAGACAGTAAGACAGTAAGACAGTATCGACAGTAGACAGTAGACAGTACCGACAGTACCGGACAGTAACAACTCTAGGACAGTACGGACAGTAGTCTGCGGAGGACAGTAATGGACAGTAGAGACAGTATAAGACAGTATTAATCGTGCCGACAGTATGACAGTATTGACAGTAGACAGACAGTATCAGACAGTAGACAGTAAAGACAGTACGACAGTAGGCGACAGTATCAGAAGAAGACAGTACCGACAGTATCGACAGTAGACAGTACTTGGACAGTACGACAGTATTATTGCAATA'
pattern  = 'GACAGTAGA'
i        = int(0)                                                     # initial position


# k-mer = text (i, k) : k-mer starting at position i of text.
# text begins at 0, ending at |text| - 1
# |text| : number of characters for the string text.

pattern_length  = int(len(pattern))
text_length     = int(len(text))
position        = int(i + pattern_length + 1)                             # looping position


# checking, string iteration trough a for loop control structure
count = int(0)
for i in range(text_length) :
    if text [ i : i+pattern_length ] == pattern :
        count += 1
    print("Counting pattern " + pattern + " in the text at position " + str(i) + " = " + str(count))

print("Pattern Count = " + str(count))
