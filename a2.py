def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    x = len(dna)
    a = dna.count('A')
    b = dna.count('G')
    c = dna.count('T')
    d = dna. count('C')
    return x == (a + b + c + d)

def insert_sequence(dna1, dna2, ind):
    return dna1[:ind] + dna2 + dna1[ind:]

def get_complement(dna1):
    dna2 = ""
    for i in range(0, len(dna1)):
        if dna1[i] == 'A':
            dna2 = dna2 + 'T'
        if dna1[i] == 'T':
            dna2 = dna2 + 'A'
        if dna1[i] == 'G':
            dna2 = dna2 + 'C'
        if dna1[i] == 'C':
            dna2 = dna2 + 'G'
    return dna2

def get_complementary_sequence(dna1):
    dna2 = ""
    for i in range(0, len(dna1)):
        if dna1[i] == 'A':
            dna2 = dna2 + 'T'
        if dna1[i] == 'T':
            dna2 = dna2 + 'A'
        if dna1[i] == 'G':
            dna2 = dna2 + 'C'
        if dna1[i] == 'C':
            dna2 = dna2 + 'G'
    return dna2


def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    return result

i = 1523
sum = 0
while i <=10503:
    sum = sum + i
    i = i + 2

print(sum)
