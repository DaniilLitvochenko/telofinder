print("Starting...")
repeat_input = open("assembly_output.dat", "r")
repeat_output = open('output.txt', 'a+')
print("Proceed, please wait...")

repeat = repeat_input.readline()
repeat = repeat.split()
while True:
    if not repeat:
        break
    if "Sequence:" == repeat[0]:
        repeat_output.write((str(repeat[0]) + " " + str(repeat[1]) + "\n"))
        while True:
            repeat = repeat_input.readline()
            repeat = repeat.split()
            if not repeat:
                break
            if ("Sequence:" != repeat[0]) and ("TTAGGG"*4 in repeat[-1]):
                repeat_output.write((str(repeat[0]) + " " + str(repeat[1]) + "\n"))
            if "Sequence:" == repeat[0]:
                repeat_output.write("0 0\n")
                break
        
print("Done!")        
repeat_input.close()
repeat_output.close()
