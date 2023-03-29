import os
import sys
import hashlib

#filename = "mixedData.tex"  # change to the name of your text file


#
#  Ignore suggested hases in .proofReadingIgnore
#
ignoreHashes = []
with open(".proofReadingIgnore","r") as file:
    for line in file:
        ignoreHashes.append(line.strip())
        

class check:

    def __init__(self, match, veto=None, hint=None):
        self.match = match
        self.veto = veto
        self.hint = hint
        
    def __call__(self, line, lineNumber, filename):
        if (self.match in line):

            if self.veto:
                if (self.veto in line): return

            hashID = hashlib.sha1((self.match+":"+line).encode("UTF-8")).hexdigest()[:10]

            if hashID in ignoreHashes: return
            
            print(f"\tWarning {self.match}:{lineNumber}\t{hashID}")
            #print(f'{filename}:{lineNumber}') 
            print(f"\t > {line}")
            if self.hint: print(f"\t\t {self.hint}\n")

    
checkList = [
    check("systematics", veto=":systematics"),
    check("kinematics"),
    check("dataset"),
    check("cut"),
    check("Monte Carlo"),
    check("statistics", hint='Do not use the term "statistics" as a substitute for "amount of data". Write "the larger sample of events" rather than "the higher statistics", and "improve the statistical precision" rather than "improve the statistics".'),
    check("due to", hint='try replacing "due to" by "caused by". If the sentence still works, then your use of "due to" is correct. However, if replacing "due to" by "because of" works even better, \n\t\t\tthen "due to" is not correct. Replace it with "because of.'),
    check("i.e."),
    check("e.g."),
    check("allows"),
    check("facilitates"),
    check("permits"),
    check("data is"),
    check("discriminator"),
    #check("which",veto="in which",hint='"Which" should be used for a nonrestrictive clause, i.e., a parenthetical comment that could be removed from the sentence without changing its meaning. A nonrestrictive clause is always offset in commas. In contrast, "that" should be used to introduce a restrictive clause, and there should be no comma(s). A restrictive clause qualifies the item discussed before it and thus changes the meaning of the sentence.')
]


noNos = ["evidences","informations","importances", "performances", "significances"]
for w in noNos:
    checkList.append(check(w))

#checks["dataset"] = warn
#checks["kinematics"] = warn
#checks["cut"] = warn
#checks["Monte Carlo"] = warn
#checks["statistics"] = warn
#checks["systematics"] = warn
#checks["due to"] = warn
#checks["i.e."] = warn
#checks["e.g."] = warn
#checks["allows"]= warn
#checks["facilitates"]= warn
#checks["permits"]= warn
#checks["data is"]= warn
#checks["discriminator"] = warn


noHyphens = []
with open("noHyphens.txt", "r") as file:
    for line in file:
        noHyphens.append(line.strip())
        #print(f"{line.strip()!r}")

with open("noHyphensTwoWords.txt", "r") as file:
    for line in file:
        noHyphens.append(line.strip())

        
def processFile(filename):
    print(f"{filename}\n")
    lineNumber = 0

    with open(filename, "r") as file:
        for line in file:
            lineNumber += 1 
            if line[0] == "%": continue

            
            for w in line.split():

                if "-" in w:
                    wNoHyphen = w.replace("-","") 
                    if wNoHyphen in noHyphens:
                        print(wNoHyphen)
                        warn("Should be no hyphen in "+w,line,lineNumber, filename)

            for c in checkList:
                c(line,lineNumber, filename)
                #if c in line:
                #    checks[c](c,line,lineNumber, filename)
                        
                
    


def print_file_contents(file_paths):
    for file_path in file_paths:
        processFile(file_path)
                
if __name__ == '__main__':
    file_paths = sys.argv[1:]
    print_file_contents(file_paths)

