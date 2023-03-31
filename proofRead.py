import os
import sys
import hashlib
import re

#filename = "mixedData.tex"  # change to the name of your text file


#
#  Ignore suggested hases in .proofReadingIgnore
#
ignoreHashes = []
with open(".proofReadingIgnore","r") as file:
    for line in file:
        ignoreHashes.append(line.strip())
        

class check:

    def __init__(self, match, veto=None, hint=None, ignoreCase=True):
        self.match = match
        self.veto = veto
        self.hint = hint
        if ignoreCase:
            self.regex = re.compile(self.match, flags=re.IGNORECASE)
        else:
            self.regex = re.compile(self.match)

        
    def __call__(self, line, lineNumber, filename):

        if self.regex.findall(line):         
        #if (self.match in line):

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
    check("uncertainty on"),
    check("cut"),
    check("Monte Carlo"),
    check("statistics", hint='Do not use the term "statistics" as a substitute for "amount of data". Write "the larger sample of events" rather than "the higher statistics", and "improve the statistical precision" rather than "improve the statistics".'),
    check("due to", hint='try replacing "due to" by "caused by". If the sentence still works, then your use of "due to" is correct. However, if replacing "due to" by "because of" works even better, \n\t\t\tthen "due to" is not correct. Replace it with "because of.'),
    check(r"i\.e\."),
    check(r"e\.g\."),
    check("allows", hint='The phrases "allows to do something" and "allows to use" are incorrect. Alternative phrasings with the intended meaning are "allows something to be accomplished" or "allows the use of".'),
    check("facilitates"),
    check("charged tracks"),
    check("permits"),
    check("fake"),
    check("error"),
    check("cross section times branching fraction"),
    #check("higgs"),
    check("data is"),
    check(r"(?<!^)Figure",ignoreCase=False),
    check(r"(?<!^)Equation",ignoreCase=False),
    #check("Figure"),
    check("discriminator", hint='While both words mean "a distinguishing characteristic", “discriminant” is more commonly used in a scientific or mathematical context, and “discriminator” is used in more general parlance. Thus, we should definitely use the former in CMS publications.'),
    check(r" [ZWHb] "),
    check(r" \\GeV"),
    check(r" \\MeV"),
    check(r" \\%"),
    #check("which",veto="in which",hint='"Which" should be used for a nonrestrictive clause, i.e., a parenthetical comment that could be removed from the sentence without changing its meaning. A nonrestrictive clause is always offset in commas. In contrast, "that" should be used to introduce a restrictive clause, and there should be no comma(s). A restrictive clause qualifies the item discussed before it and thus changes the meaning of the sentence.')
]


noNos = ["evidences","informations","importances", "performances", "significances", "It's", "it's","associated to", "stat\.", "sys\.","syst\.","C\.L\."
         "let's", "don't", "can't", "won't", "it's", "shouldn't",
         ]
for w in noNos:
    checkList.append(check(w))


noHyphens = []
with open("noHyphens.txt", "r") as file:
    for line in file:
        noHyphens.append(line.strip())


with open("noHyphensTwoWords.txt", "r") as file:
    for line in file:
        noHyphens.append(line.strip())

hyphens = []
hyphensTest = []
with open("hyphens.txt", "r") as file:
    for line in file:
        hyphens    .append(line.strip())
        hyphensTest.append(line.strip().replace("-"," "))

        
        
def processFile(filename):
    print(f"{filename}\n")
    lineNumber = 0

    with open(filename, "r") as file:
        for line in file:
            lineNumber += 1 
            if line[0] == "%": continue

            for hyphenWord, hyphenWordTest in zip(hyphens, hyphensTest):                
                if hyphenWordTest in line:
                    hashID = hashlib.sha1((hyphenWord+":"+line).encode("UTF-8")).hexdigest()[:10]
                    if hashID not in ignoreHashes: 
                        print(f"\tWarning {hyphenWord}:{lineNumber}\t{hashID}")
                        print(f"\t\tShould be a hyphen(s) in line \n\t\t {line} ")


                    #print(hyphenWord)
                    #warn("Should be a hyphen in "+


            for w in line.split():


                #
                #  IF word has hyphen check if OK
                #
                if "-" in w:
                    wNoHyphen = w.replace("-","") 
                    if wNoHyphen in noHyphens:
                        hashID = hashlib.sha1((wNoHyphen+":"+line).encode("UTF-8")).hexdigest()[:10]
                        if hashID not in ignoreHashes: 
                            print(f"\tWarning {w}:{lineNumber}\t{hashID}")
                            print(f"\t\tShould be no hyphen in {w} ")

                    
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

