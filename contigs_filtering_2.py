contig = open("assembly.fasta", "r")
output = open('contig_output.txt', 'a+')
print("Starting contigs filtering...")
i = 0
while True:
    i+=1
    print("In process: ", i)
    sequence = contig.readline()
    if not sequence:
        break
    if  sequence[0] != ">":
        while True:
            sequence = sequence.replace("\r","")
            sequence = sequence.replace("\n","")
            output.write("" + sequence)
            sequence = contig.readline()
            if not sequence:
                break
            if sequence[0] == ">":
                output.write("\n")
                break

print("Done!")
contig.close()
output.close()
