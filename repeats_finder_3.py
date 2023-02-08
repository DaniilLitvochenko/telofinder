coord = open("output.txt", "r")
contig = open("contig_output.txt", "r")
result = open("result.txt", "a+")

print("Starting...")
coordinate = coord.readline().split()
while True:
    if coordinate[0] == "Sequence:":
        result.write(coordinate[1]+"\n")
        coordinate = coord.readline().split()
        seq = contig.readline()
        if not seq:
            break
        if not coordinate:
            break
        if coordinate[0] != "0" and coordinate[1] !="0":
            while True:
                if coordinate[0] == "Sequence:":
                    break           
                c1 = int(coordinate[0])
                c2 = int(coordinate[1])
                seq = seq.replace(seq[c1:c2], seq[c1:c2].lower())
                coordinate = coord.readline().split()
                if not coordinate:
                    break
            result.write(""+seq)
        else:
           coordinate = coord.readline().split() 
print("Done!")

coord.close()
contig.close()
result.close()
