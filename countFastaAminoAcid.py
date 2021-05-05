import os
import sys

def countAminoAcid( fasta_list ):
    
    fasta_file = { }
    amino_acid_count = { }
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYZX*-"  

    for file_name in fasta_list:
        
        with open(file_name) as file:
            
            # sequence storage
            
            for line in file:
                if line[0] == ">" :
                    header_title = line.split("|")[1]
                    fasta_file[header_title] = ""
                else:
                    fasta_file[header_title] += line.strip( )

            # aminoacid count

            for header_title in fasta_file:
                amino_acid_count[header_title] = { }
                for char in fasta_file[header_title]:
                    if char not in alphabet:
                        print("Check your sequence! Character: " + str(char) + " from sequence: " + header_title)
                    for letter in alphabet:
                        amino_acid_count[header_title][letter] = 0            
            
            for header_title in fasta_file:
                for char in fasta_file[header_title]:
                    if char in amino_acid_count[header_title]:
                        amino_acid_count[header_title][char] += 1
                        
            # uncomment for computing aminoacid mean
            
            #count_alanin = 0
            #sum_alanin = 0
            
            #for header_title in amino_acid_count:
            #    sum_alanin += amino_acid_count[header_title]['A']
            #    count_alanin += 1
            #print(sum_alanin/count_alanin)
    
    # write to .csv file
    with open("output.csv", "w") as out_file:
        out_file.write("Name\t")
    
        header = ""
        for letter in alphabet:
            header += letter + '\t'

        out_file.write(header + "Total\n")
      
    
        for header_title in amino_acid_count:
            entry = ""
            counter = 0
            for char in amino_acid_count[header_title]:
                entry += str(amino_acid_count[header_title][char]).strip() + '\t'
                counter += amino_acid_count[header_title][char]
            out_file.write(header_title + '\t' + entry + '\t' + str(counter))
            out_file.write('\n')

# files to list

entries = os.listdir(sys.argv[1])

# filter for .fasta/.fa files

new_list = [ ]
for entry in entries:
    if ".fa" in entry:
        new_list.append(entry)
        
# execute func

countAminoAcid(new_list)

