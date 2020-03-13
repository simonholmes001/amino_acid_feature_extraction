one_letter_code = {"Ala":"A", "Arg":"R", "Asn":"N", "Asp":"D", "Cys":"C", "Gln":"Q", "Glu":"E", "Gly":"G", "His":"H",
    "Ile":"I", "Leu":"L", "Lys":"K", "Met":"M", "Phe":"F", "Pro":"P", "Ser":"S", "Thr":"T", "Trp":"W",
    "Tyr":"Y", "Val":"V"}

three_letter_code = {"Alanine":"Ala", "Arginine":"Arg", "Asparagine":"Asn", "Aspartic Acid":"Asp",
                     "Cysteine":"Cys","Glutamine":"Gln", "Glutamic Acid":"Glu", "Glycine":"Gly",
                     "Histidine":"His", "Isoleucine":"Ile", "Leucine":"Leu", "Lysine":"Lys",
                     "Methionine":"Met", "Phenylalanine":"Phe", "Proline":"Pro", "Serine":"Ser",
                     "Threonine":"Thr", "Tryptophan":"Trp", "Tyrosine":"Tyr", "Valine":"Val"}

pubchem_code = {"Ala":"5950", "Arg":"6322", "Asn":"6267", "Asp":"5960", "Cys":"5862", "Gln":"5961",
                "Glu":"33032", "Gly":"750", "His":"6274", "Ile":"6306", "Leu":"6106", "Lys":"5962",
                "Met":"6137", "Phe":"6140", "Pro":"614", "Ser":"5951", "Thr":"6288", "Trp":"6305",
                "Tyr":"6057", "Val":"6287"}

for key, value in one_letter_code.items():
    print(key)
    print(value)
for key, value in three_letter_code.items():
    print(key)
    print(value)
for key, value in pubchem_code.items():
    print(key)
    print(value)
