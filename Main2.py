import csv
from datetime import datetime
import sys

user_title = ''
date = ''

amino_acids = []
codons = []
user_codons = []

amino_acid_translated_sequence = []
output_amino_acid_sequence = ''

three_letter_amino_acid_translated_sequence = []
output_three_letter_amino_acid_sequence = ''

one_letter_amino_acid_translated_sequence = []
output_one_letter_amino_acid_sequence = ''

user_DNA_sequence = input("Please enter your DNA sequence for translation: ")

class DNAProcessing:
    """This class processes the user inputted DNA sequence into three nucleotides sequences (codons)"""

    def __init__(self, user_DNA_sequence):
        
        self.user_DNA_sequence = user_DNA_sequence

    def segmentation(self): 
        
        if len(user_DNA_sequence) % 3 == 0:
            triplets = []
            for i in range(0, len(user_DNA_sequence), 3):
                triplets.append(user_DNA_sequence[i: i+3])
            return(triplets)
        else:
            print("ERROR: This sequence contains a partially filled codon (not divisable by 3)")
            exit()
        

class Translation:
    """This class takes the output from the DNAProcessing class to convert the user sequence into the amino acid sequence"""

    def __init__(self, user_codons):
        
        self.user_codons = user_codons

    def processing(self):
        
        amino_acids = []
        codons = []
        three_letter_amino_acids = []
        one_letter_amino_acids = []

        filename = 'Amino Acid Complementary Sequences CSV.csv'
        with open(filename) as f:
            reader = csv.reader(f)

            for row in reader:
        
                    amino_acid = str(row[0])
                    codon = str(row[1])
                    three_letter_amino_acid = str(row[2])
                    one_letter_amino_acid = str(row[3])

                    amino_acids.append(amino_acid)
                    codons.append(codon)
                    three_letter_amino_acids.append(three_letter_amino_acid)
                    one_letter_amino_acids.append(one_letter_amino_acid)


        for current_codon in user_codons[:]:
            try:
                locate_codon = codons.index(current_codon)
            
            except:
                print("This sequence is not found")
                exit()
        
            else:
                amino_acid_translated_sequence.append(amino_acids[locate_codon])
                output_amino_acid_sequence = amino_acid_translated_sequence

                three_letter_amino_acid_translated_sequence.append(three_letter_amino_acids[locate_codon])
                output_three_letter_amino_acid_sequence = three_letter_amino_acid_translated_sequence

                one_letter_amino_acid_translated_sequence.append(one_letter_amino_acids[locate_codon])
                output_one_letter_amino_acid_sequence = one_letter_amino_acid_translated_sequence
            
        return(output_amino_acid_sequence, output_three_letter_amino_acid_sequence, output_one_letter_amino_acid_sequence)

class Filing:
    """The filing class generates a file with the translated sequence"""

    def writing(user_DNA_sequence, output_amino_acid_sequence, output_three_letter_amino_acid_sequence, output_one_letter_amino_acid_sequence):
    
        user_title = input("Give the file a title: ")
        date = str(datetime.now().strftime("%H-%M-%S %d-%m-%Y"))
        
        filename = (f"{user_title}{date}.txt")
    
        with open(filename, "w") as f:
            f.write("User DNA Sequence:\n>{}\n\nComplementary Amino Acid Sequence:\n>{}\n\nThree Letter Amino Acid Sequence:\n>{}\n\nOne Letter Amino Acid Sequence:\n>{}".format(user_DNA_sequence, ', '.join(output_amino_acid_sequence), ', '.join(output_three_letter_amino_acid_sequence), ', '.join(output_one_letter_amino_acid_sequence)))

user_codons = DNAProcessing.segmentation(user_DNA_sequence)
output_amino_acid_sequence, output_three_letter_amino_acid_sequence, output_one_letter_amino_acid_sequence = Translation.processing(user_codons)
Filing.writing(user_DNA_sequence, output_amino_acid_sequence, output_three_letter_amino_acid_sequence, output_one_letter_amino_acid_sequence)

print("Translation Complete\nThe translated sequence may be found as a .txt file in the same folder as this programme")
exit()

















