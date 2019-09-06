import sys
#print("Number of arguments:" + str(len(sys.argv)))
if len(sys.argv) != 2:
    print("incorrect number of parameters \nusage: $ python tokenizer.py 'FILENAME' ")
    quit()

grammer = {
    chr(92): "LAMBDA",
    chr(46): "DOT",
    chr(32): "APPLICATION"
}


fileIn = open(sys.argv[1])
for line in fileIn:
    #print(line, end = '')
    x = []
    for c in line:
        if (c in grammer):
            x.append(grammer[c])
        elif(x[-1] == "LAMBDA"):
            x.append("IDENTIFIER")
        elif(x[-1] == "IDENTIFIER"):
            x.append("IDENTIFIER")
        elif(x[-1] == "DOT"):
            x.append("FUNCTION BODY")
        else:
            continue
    print(x)
    
#print(fileIn)
