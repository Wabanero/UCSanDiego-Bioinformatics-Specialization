"""FrequentWords.py:
        Code Challenge: Solve the Frequent Words Problem.
        Input: A string Text and an integer k from a txt file generated each session
        Output: All most frequent k-mers in Text"""

__author__      = "Filippo Bergeretti"
__date__        = "15 May 2019"

# Frequent Word is the most frequent k-mer in the Text string.
# FrequentWords() function is below along with the subroutines needed.
# dataset_2_10.txt was downloaded in the script directory

# Defining functions Count AND Frequent words

def Count(text, pattern):
    count = 0
    text_length = int(len(text))
    position = int(i + k + 1)
    for i in range(tl):
        if text[i: i + k] == pattern:
            count += 1
    return count

def FrequentWords(text,k):
    return list_kmers
    
