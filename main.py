from coronavirus import coronavirus


def prepare_data(dna: str) -> str:
    corona = coronavirus
    for a in ' \n123456789':
        corona = corona.replace(a, '')

    print('Length: ', len(corona))
    return corona


def translation(dna: str):
    protein = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
               "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
               "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
               "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
               "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
               "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
               "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
               "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
               "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
               "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
               "TAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
               "TAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
               "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
               "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
               "TGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
               "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
               }


corona = prepare_data(coronavirus)
print('DNA sequence: ', corona)

protein_sequence = translation(corona)
print('Protein sequence: ', protein_sequence)
