import sys
#print("Number of arguments:" + str(len(sys.argv)))
if len(sys.argv) != 2:
    print("incorrect number of parameters \nusage: $ python tokenizer.py 'FILENAME' ")
    quit()

grammer = {
    chr(92): "LAMBDA",
    chr(46): "DOT",
    chr(32): "APPLICATION",
    chr(40): "L_PARENTHESIS",
    chr(41): "R_PARENTHESIS"
}
def fill_args (x , line):
    x.append(grammer[chr(92)])
    for c in line:
        if c == chr(46):
            x.append(grammer[chr(46)])
            return x
        else:
            x.append("ARG")

fileIn = open(sys.argv[1])
for line in fileIn:
    #print(line, end = '')
    x = []
    for c in line:
        if(c in grammer):
            x.append(grammer[c])
        elif(c == chr(10)):
            break
        else:
            x.append("IDENTIFIER")
    print(x)

#print(fileIn)
