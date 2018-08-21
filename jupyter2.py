# exo10_06
"Exercice adapté du MOOC bioinformatique de François Rechenmann & Thierry Parmentelat (inria)"

# Table du code génétique (correspondance codon -> acide aminé)
lookup_table = {
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
    'UUA': 'L', 'UCA': 'S', 'UAA': '#', 'UGA': '#',
    'UUG': 'L', 'UCG': 'S', 'UAG': '#', 'UGG': 'W',
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G',
}


# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translate_rna_to_amino_acids(rna):
    """
    Traduction d'un brin d'ARN en une chaine encodant les acides aminés correspondants.
    L'ARN en entrée est découpé en groupes de 3 (codon) ; les lettres superflues en fin de chaine sont ignorées.
    """

    # initialisation : la variable 'offset' indique le début d'un codon
    offset = 0
    longueur = len(rna)
    resultat = ''
    # la boucle principale
    while offset <= longueur - 3:
        codon = rna[offset: offset + 3]
        resultat += lookup_table[codon]
        offset += 3  # groupe suivant
    return resultat


# Programme principal =========================================================
with open("../chapitre_10/indata_exo10_adn.txt", encoding='utf8') as f:
    dna = f.read()

rna = dna.replace('T', 'U')  # passage ADN => ARN

# affichages
print("dna :", dna)
print("rna :", rna)
print("\nTraduction en acides aminés :")
print(translate_rna_to_amino_acids(rna))
