'''
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols.
Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s

corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''

dna = 'ACGT'
rna = 'ACGU'
# mrna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
# mrna ='AUGGAAUUCCAUAAUAGCGGAACCGUCAGAGGUUUUGAGAUCGGACUGCGUCGUAAUACAGCUACUGAUGCCCACAUCUCCAGAUGGAACCUUCUGGCCAUAGGACGCGUUCGUAGAGGGAUUAACCUCCCGCCUAUACGUACUUCUUACCAAGUCAUGCAGAGCCGACGACCAAUAACACAGUCGGGCCGAUCGACGUGUGGUUUGCCGGCGGUCCGACGUCUCGUUACGACCGCCUUCGCGUUCGUAGGCUGGAUUUCAACGCCAGAACAGCUACGACCUCGGAUUUAUGGGUUAGAGCGCUCCAACCUGGUCAUUCUGCGGUUAGAUGUACAUUUAGUCGUGAGGGUCGAGCACGAUCUUCCCAAGGUCGAGCUGCUACACUGGAGGCCACUGCCUGUGUUGGUGGUACUUGGGAAGGUGGGGCAUUCAAAUCGGAUGUCGACCGGUAGACCUGUUUCACUAGAUACCAUGGCGGCACACAUGCUCCAAACCCUGCCUAUCAUCGCAACUCUUGGCGCCUGGUCACCAAGCACCCUCGCACGUGUAAGUCGGCGGAAUAUGACACCCUACAUUCGCAGUCAGUCUACUCGGCAGCGUGGCGCAGGCCUCAAGGCACGUCCUGACGGACCUGGACGCCCAGCUGCAGGUACGCAAAUAUUAAGAGUCGGUUGUGUGGCCGGUGCUAUAGGGAGCUCUCGACUUAUAGCAACUCCCCUUUUGGCGCUAGGCGCUGUCAAGAAGUUAGGACUCAUACCUCUAAUUUGCAGAGCCCUUCGACCUCUGGUAAAGGCUAAUUUCGGGGGUUUAGAUCCGCUUAUGAUGGCAGGUUCGGUGUGCCAAGGGCCUAGGUCCCCGAGUAGUACACCGGCGAUCGGUCACCUUUCCGGUGGGACGCGCUCGAUCCUCAUAGCUGCGGAAAAAACGUCAACAAUGUUAACAGCCGAAUAUCAAAAAAGUAAAAAGUGUACUCCAGGAAAUCGAACCGAGGAGGAUUUGCUGGGCAAUGGAUGCUUGGAUACGAAAAAGUCAACGUUGGGUCAUAAGGAUUAUAUCAGAGUUUCGCUCCCUAUGCCCCUGGAAGCGAGGGCGCCCCCUUCACAACGGCGAUUGUUUGGGGGACUUAAUGGACUGGCACUCUAUCACGCUAGUUCACAACACGAGUUGUACAACAUUCUCCCAAUACGUCUAAGUAGUACCAUAGCACCCCAUCGGGAUGAAACCGGGUCCCCGGUGGUAAGUGUCCACUUCGGCGGUAGCUUUCAAAUAGAGAUUAGCUAUCGUUGCAGUCGUUGGUUUGUCUCAAGGGGCGAACAGCCUACAGCAGCGCUGUGUGCGUUGGCCUACAGAUUAACUUCAACGCCUAAUUGGUUAGGCAUGUCAAUCAACCCUCAAAACGGUAAAGAGUGUUCCAAAUCUAUUUUGCCCGGCCAUACCAUGCAACAGGCCUUUCAUUGGGGCCCUGCUUGUGUGUCACUUCUUAUGUUCAUCCCCACCCACACUGAACGCCACCGCAGGCUGGAGAGGUUUUACCUUCGAUCGAACUUCUUUAGUCUGUCUGCAAUGCUGUCGAUUGAAUACUCUGAUUGUGGUGAAUGUACUACAGAACCACUUUUCCACUUAUUACCGAGAAUCGCUCGUGUUAUCCAGGCUACAUGUUCAACGAGUGUUACAGGUCGCUCCACGGAUACUGUAAUGUGCAGGGCUCAUACUGUCCAAAAGUCUCCGACAGGACCCACGACGAACUUUCAGUUUCAGCAGAGCUUGAGUGGGUACUGUUUUGCUUGGAGUGGGAAGCUUGCCUGCCUGAAGAGGAGAUACCUGGACUGUACCGUCACCCGAUUCGGUUUUGUCCAAGAGUAUAUGCGCAGGGGGCGGCAACGCGCGCGAUUUUCUGCUAUAAACCUUCCCUUCGGAACCUUGCUGCUUAUCUCGCGAAAGUCGGGAGUUAUGCAGUCCGCAACGCUACUCUCGCGUACAAGAGUACUCAUUGGUUACACAGUUACCGAUAUUGGAAUUAGGACUUUUACGCGUAUUUUUCCCCGUUGCCGUAUACGGCGGUUUUGGGUUAAAGAGCAGAGAGGAAUAUCUGUCCCGGUCCGCCACCGAAUCCGAGGACCAGGAGCAAUUAUCCGUGACGAAUUAACUUUAGAUAGAGCCAAACGUUUAAUUGGCUCCCACCGUGAUAUACAGCGCAGGCUUCGUUUUGAGCGUAGUACGUAUCAAAACUACGUUACACGUAUGUAUUCCAUUUACGUUGUGGCCUUAUGUACAGGAAAUAUUACACGUUUAGUAAUGAGGUUUACUAGAUCUGAAACCCUUUUUUUGCCCUCACAGGCCAAUACACCUCUAAAGAGGCAACGGUCAAUAUCUCAGGUGAGGAUGGACUACCGUUUGCUAGGGACCGUUCUCUGGGGACUAUCGCCGACGCCUUGCUUUUAUACGCCAUUCCGACGUUUGCGUUUCGGCGGGUCACUUAGCCGGGGUACCCUCAAGGGAGCGUGUUUCGGAAUCCUUUUCGAUUGCGGCAACGGCCGGAGUCUCAGCCGCGACGCGAGUCGCGUUCUCCGGACAUCCUCACGCUGCGAACGGGCCAAACUGCUUUCUGCGUCCUCACAUCCUCGCGCACUUCAGCGUUCCGCAGUCCGCGUGCUCCUCGACCAUGAAGGACAGGCGGUCCGUAUAACUGUCGAUGGCCAAAGUGAGACCGCAUAUUAUAUAGACCCGACCAUUCCCAACACGUCCUCGCGGUCGCUUUACGUGACGCCGCAAUAUCUAACCCAGUUGCAGGGGAUGCAGGUGUACACACUGGUCGAACGCAGUCCUAAAUCACACCCGCGCUCGGUCGGCAUCAACAAACAAGCGAUUGAAGCGCCCUGCUUUGGUAUUCGCACAACACGCACUGCUUUGGUGUUUCCGAUGCGUUUCAGCCCCGCACGUCGGAUCAAAAUCUUUAGGCAGGGCCUGCGAAACGAUGCUGGCAACGUAUGCACGCGGGCUCAGGUCGGCGACCAGCAGGUUAAAAUCAAAGCUUGCGGUGAAGGCCUCGACGUAAAGGGCGCAGUUGCUUCCGCUGAAGCACCGAGCGAGGGCCCCGGUAGGUCGUGCACGGAGAUGCGAGACUCUACUCCCAGUAGAGGAGUAAUCCACACCAGGCUCGCCUCCUGGCUGUGCAACUUCAAUAUAAGGGUCGGACACCCAUUCCACCCGGAACGUCUGGAUCCAACUCCCUUACGUCGGCCUGGCUGUCACGCGAAAGGAACACAAAUUCCUUCUCUGCUUACCCUUACGACUACCUGCAAACACACUUUAGUGACGCCCGUCAUAGACGAGAGCGCAACUUUGCAAAUAGUGUGCACUCUGUGCUCCGCAAACACGGGGUAUAUCCUACACGUCUUGCGAUUUACCGGAAGUCAUCGUAGCCUCCUUGCCAUAUGCGGUAAACUAAAAGAUCCGUCUGGGAAGCGACAACUGUGUCUGCCAGUUCUAUGCUCGAAGCCUCUAUUAGCACCUAUCCUAACGGGACAGCAGCUGGAAGGUUCCGAAUAUGGCCCACAAACGCGUUGGUUAUCUCGAUCCGACUUGUCGUAUAUACUUUUCUUCUUUGGCUCUGCGGAUCAAGUGGCUAGAGUUACGGAUGAUCUGUCGGCUACCGAGGCCGCUGUCCCAGUCCAGUUGACCUCAGUAUUACAUGCGACAAUGGAGGAUGUCCACAGCAUACAGUUCAUCAGUCGUAAAGGUAGUCUUCAGUGGUCUAAAAGCAUCUUCGGCACUGGUAACACACCUCGUUCAAACAUAGAUUAUGGUACUAGCGCGCGUAAUCAAACACGUAGUCGACAAGUGAUCGUAUACCCCACCACUCACAAGUGCCUGCAAGAGACUGUCUGUUCUAAGCCCGGCGACAUCUGUCGCUCGCUCUACCACUAUCUAGUUGGCUGGGGCCGAGGACGAGAAGGUGGCCUCAAUAAGAGUCUCGGUCUCUUAAGCAUAGAAAAGGGAAGUUCCCUGGGGCCCUUACCUCGUCCAGUAGCCUGUAGGUUCUUCGUACACGCCGUACGUGCUCUUGUGGAGCGAGAGCGAGCAUCUUCGGUCAGGUUAGGUAACACUCUAUCUUUCGGGCUUAGCUUAGGAAACCAAAGCUUCGAAAAGGGCUUGGGUUGGGAUAAGCUUUUUCUGAAAGCAUCCAUGUGUGGGCGUAGGUUAACUUCCCUAAGCAUCACAAUAGAUGCCCGUCGCUCCGGUAAAGCGUAUCAUCGACGGUGGGGCCACCAGCUAUGGGCGAAUCAGCGGAUAAGGGGUCUCAUUCAUCAAAGGUCUCAAUGCCGCAGGCGAAGAGAGCCCAAGUUACCCGAUACUAGUCGCCCCUACCGACAGUCGAUGUUGACGGUUAUAGGGUCGAUUCUUCACCGUGAAACGUUGCGCGAGUCCACAAAGGCCUCCGCGGAAUUUUUGCUACUGCGAAACGCACCCCAUAUUAGGGGCGGCGCCUCACCAGAGGGUUCCCUGAUCUUGAGAGGUGAAACAACUGCCUCGAGUUCCUCUCCGAUGAAGGCUCAUUGCCUCACUAUUCAAGGCGAGGAAUGUAGUAGUACGGGGAAAGAGCCAUCCAGAUUGAAGACAGGUAAUUGCAACAAUUCUUGUUUACAUGAUUUACAGAUAACGAACACACGAGGCAUACGGUGCCUUCCCACUGGUGAAGACGGAUAUGUGCCCCUCAUGUUGCCUAAGUUAGUCACAGACUUUUCUUCCAAGAGACGUUUUUAUCCAACUUCGGAGACCUUCGCCUCGUUUCCGGAAUAUGAGGUACACCUGUUCUUUAGACGUUUUGUGGGUUACCAAGAAAGGAAGUCGAAUCAUGGUAACAUCACGAUAACUGUGGGGCAACUCUUCGAGGAAAACCAGCCCGAACUUAAAAAAUUAACAGGAGUGGUGAAGCAACAUCAACGCACCAAUCGGGCCAUUAGUGUGUUGGAGAAGGGCUUUCGCAAUAGGGCCCGUGACAUGCAUCACCCUAUGCAUAAGCUGCAUUUGAUCAUCAAUGUCCGGCCGCCUUAUACGUCAUUGUCUGAGAGACUAGCUCAGCUGGCACAGACUAAUUUGAGUUCCGUACCCAUCAUCGGUCGCAACAAGUGUAUGGGGCGGAUACCUGUUAGUAGUAAAAACAUUGGGUGGCGGGUUGUCUCUCCCACAGCACACGUCAGUGGGACUUCCGGCGUUGACUCACGAGCCCACCGCUUGACAAAUGUAGUCCACGCUACGGGAAGGCGACCUAUCAAUGCUCAUCUCAAUGAUCAGGGCCAAUUGACCCCUGACCAGACGAUGUUUCGAUCAAAUAGAGAGAGAAGAAGUUGUUCCGAGGAGCUUCCAGCGCUCAGUAUGCACAGAAUUGUAAGAGGGGAUGCUCCGUUAGCCAAUGCAAGCGUGUGCAGCACCAGUGACGGUGGCCGGUACCUGGCCGAGUACCUUAGCCCUCCACACGGUCAUCACCCCGCAAGCUGCGCUUGCGAGGGUACUCACUCGAUCCGUGGGAGCAAACUCUUCUACCAGACAGUGUUCUUGGCAACCAACAGUAGAAGUAAUGCUUUACGUCGCUGGCCGCAUAGGGGAGCACUUGAUACCAGGUGGUUCCGCAAACUGCUGUUCCGACGGCCUUCAGAAAGCGCUGACGUUGAAGUGGGGGUAAAAUGGUACCGCAAUUCCUCUCUCUCGGAAUCAGCUCGGGAUCACAUCAUUAGGCUAUUCCUUAAUUUCUACAAAGACUUGCAUGCCGCGGUUCCAACGCAGCCAAUAUUGUGCCCUCAUAAGCACGUACCGACAAUAGUCGGAAGGAAGCCCCCGUUGAGGACGCGGUGCUGUUGCGAGGUAAGAUACCUAGUUCGCUUAUGUGAAACCGUGCCCACCGUAGUCAACCGCCGAUCGCUCUAUGGGAUUCCCACAGGGAUGACGCGCAAUCGUCCAAUGGAUAUGACAAGUGACAGCAAGACAUGUCCGAAAUCAUACCGCAUGACCAUUUUCUCGGAGAUACUACCACCGCGUGACAAACUCUGGUUGCACCUGCCAAUCCUUAAGCUGAUACGCUUGCUGGGCGGAGUAAUUGUUACUUCCUCGCUUUUUCGGAGACGUAGUAUCGUAGACAUACCCGCUCCAGAGAGAAAUCUAGCAGCCGAUGUUCUCUCCUUGUGCGCUUGUGGCAUGGCGCUCUCCCCUGCAGAUAGCGAUCUGGCCUGUGGUCGCUGUUGCGGGUGUCUCGAGGAUAUCAUUGCAACGGUGCAUGACUUGACUAAUGGUGCAGUGUCGCAUGGUUCAAGACAACCGCAAGACCGAUGCGGACUGCAUCGCUCCGCACCCCGUAUGAAAGUCGGGGGCCCAACAGUAGCGAUUGGGACGAUAUGGUCCUUCGAAUACCCUAUUCGGCGGGUCCGUCUUGUCGGUACGCCACUACUUUGGUCGAAGUCCUACGUGAUCGUAGUUUUGCAUAUCCGGUCCAGACUCCAUGUUUGGUCUUUGGACUCGAUUACGGCACCUGUGACGAGGGCCGACCGCGGGCUUGUGAGCGUUACAAUCACUCAUCCACUCUUUCGAAGCCCCAGCUGUGAUACUACUAUACUUCCUGUGGCUCUCCGGGUCCGCAAGAACAAGUCGAAGCGUGUUGGCGUGUGGGCACGACCAAAUAAUUUGAGCACUUGCUUAGCGUUGUUAUCUGGGCCUAUUUGGACCGGGUGUAAUGAUCUAUCGUGGAGUUCUCCCUUGGUUCUGGAACAUGUCCCCGCACUAUCUGCAUCAAUUGGGUCCGCGUUCCCUCGAAAGGCUAAGGCGACGUUCAACUAUCUUGCUAGGCAUAGUCGUAGCGCUCGAUUGACUUCGCCGGAAGUCAACAGACCGUAUCCUAGGAUAUAUCCCCAUUCGAGGCUUAACUUGAUACUGGAAGGCCACGAAGAGCGUCUGGAGGCUUCCUUUCGGGUGGAGGAUCCUAGGUUGUAUGAUACCCCGACGCUCCAACGAACCCCCGCUUCUAGACACAACCACACAGCACACUUAGUGGCGAUUCUCCUUGUCGUCUUUUGCUUGUCUGGCGUCUAUGAGUCUCGCCCGCGUGUUACGCACAAGUUUAAUGCAACCCCGCUGGAUAAAGUCAUAGAUAUCCAGUUUUGCUUGCAAUCACAUGGGCCCGUGUCUAGCAAACACGCGAUGGUAUGUCGACCCCAUCACUGCCCCACAACGCGUGGUGAAUCCCUGACACGAGUUCGGGCGUACCACCCAUCUUACAUCACCAUGGCAGAACGGUGUUUAGGAAUCAACCAAUUUCACAAGGAUCGCGGAAAGCUUGGUCGUCCAAUCAGAUUGUAUGCCAGUAAACCUUGGCAGGACAGAGUGAUGAGAACUCCUGGACUUACCAAUCGUCAGUAUUCUUCCCACUUUAGGAGCGCCCGAAUACGCAUGAUUCGAAGGGCGUAUUCCUGCACAGUCCAGGUUGACGCAUGCCACCAUGUAGGAUUUCUCUCACCCAUUAGGGUCAACAACGAAUCGUGCUGCAGAGAGACCAGCUUAAAGUCCUUCAAUAAGGCUAAGAGGCGCAUUAUGAGUACGCGCUGCUUUAGAAACUGGCUUCUUGUGGGCCUGGCUUUGACGAUGCGCGAUCCGGGGGUGAACUGUGCUAUUUCUCAUGUGCUCGUAAUAGAUUCCCGCGCCUGCCACCUGUUAGCUCGGCGCCUGGUGUCAAAGGGGCAGUGGGAACGCUGGGUGCGGUUCGGAGGUCGGACUUGCAGUAUGCGAAUUUUGAAGUGGGUUUGGGACAGUUCCCCCCUAAUGUUGCUCACCCGAAACUUCAAUGGCUCUGAGGAACCCUGGUCGGAGUCGCCUUUUUCUGGGACACUGCGACAAAUAAACCCCAUGCAAAUCAUCUUGAGUUCGACAAAACGAGUUAUGGGGGGAAGAUUAUUGGGAGCUUGUUCCUUGUACUCUGGGGAGUCUGUAUUCAAUGUGCGUUAUUGCUUAGAUAUAGAGUUGGGCAAAUACAAAGGGUAUCUAUGCUAUUUUAUCGAUGCGGUAAAGAUCCAUCCGUUGUUAUUUUAUGAGGCGUGCGGAAGGAGUCCCUGGAAUAGAGCUUAUGUGGCGCGAUGUAGCUGCGCAGGAGGCUUACGUGCAGUCAAGACCCGACGCCGGAGCUGGCGACCAAUUUAUCAAAAUCCCACGUGCGGCGACGGCUAUGGGUACGGGUACGGCUUGAGCCAUUUUAGUCCAGAAGUUACUACGACUGUCGGCCGAUCUGCAUCGUCUUUUCUAUUUGAGUUUAUAGUGAUGUUGGUUUACAGGGAAGAGAUAUUGAUGAGAACUCCACAGCCCAGUGGGAUAGUGUUACCCGAAUUCGUUGAUUUGCGCUUUACUUCAUUUCACCGCGAAUUGGUCUUUCGUGAAUUCCGCUUAUCAAAUAACCUCAAUUGGCCACCCAGUCCGGAACUCAUUGGCAUCAUUUUCGAAGGGAGAAUUGACCCUUACAGGCUCCAAUCGUCAGCUAACGCAAUCCAUGAACUGUUCAUGACUCUCUCUAGGAACCGACUUCCUUGCCCGCUCGGCAGGGGUGUCCUUUAUCGGGAACUACUCGACAUGAGAGUAGGAGACGCAAACGACGGCUCCAGAUACCUUGCGAGACCAAUUUGA'
# step codon
step = 3
# codon dictionary
codons = {
    'AGG': 'R', 'AGA': 'R', 'AGC': 'S', 'AGU': 'S',
    'AAG': 'K', 'AAA': 'K', 'AAC': 'N', 'AAU': 'N',
    'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACU': 'T',
    'AUG': 'M', 'AUA': 'I', 'AUC': 'I', 'AUU': 'I',

    'CGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGU': 'R',
    'CAG': 'Q', 'CAA': 'Q', 'CAC': 'H', 'CAU': 'H',
    'CCG': 'P', 'CCA': 'P', 'CCC': 'P', 'CCU': 'P',
    'CUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUU': 'L',

    'UGG': 'W', 'UGA': '', 'UGC': 'C', 'UGU': 'C',
    'UAG': '', 'UAA': '', 'UAC': 'Y', 'UAU': 'Y',
    'UCG': 'S', 'UCA': 'S', 'UCC': 'S', 'UCU': 'S',
    'UUG': 'L', 'UUA': 'L', 'UUC': 'F', 'UUU': 'F',

    'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GGU': 'G',
    'GAG': 'E', 'GAA': 'E', 'GAC': 'D', 'GAU': 'D',
    'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCU': 'A',
    'GUG': 'V', 'GUA': 'V', 'GUC': 'V', 'GUU': 'V',
}


def translating(s):
    amino = ''
    for i in range(0, len(s), step):
        amino = amino+codons[s[i:i + 3]]
    return amino


seq = open("dataset/rosalind_prot.txt").read()
print(translating(seq))