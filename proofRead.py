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

        self.veto = veto
        self.hint = hint
        self.regexAND = []
        
        if isinstance(match, list):
            self.matchName = " ".join(match)
        
            for m in match:

                if ignoreCase: self.regexAND.append(re.compile(m, flags=re.IGNORECASE))
                else:          self.regexAND.append(re.compile(m))
                    
        else:
            self.matchName = match
            if ignoreCase: self.regexAND.append(re.compile(match, flags=re.IGNORECASE))
            else:          self.regexAND.append(re.compile(match))

    def foundMatch(self,line):

        allTrue = True
        for re in self.regexAND:
            if not re.findall(line):
                allTrue = False

        
        if self.veto:
            if (self.veto in line):
                allTrue = False



        return allTrue
        
        
    def __call__(self, line, lineNumber, filename, quiet = False):

        foundIssue = False

        if self.foundMatch(line):
        #if self.regex.findall(line):         
        #
        #    if self.veto:
        #        if (self.veto in line): return

            hashID = hashlib.sha1((self.matchName+":"+line).encode("UTF-8")).hexdigest()[:10]

            if hashID in ignoreHashes: return

            if not quiet:
                print(f"\tWarning {self.matchName}:{lineNumber}\t{hashID}")
                #print(f'{filename}:{lineNumber}') 
                print(f"\t > {line}")
                if self.hint: print(f"\t\t {self.hint}\n")
            foundIssue = True
            
        return foundIssue

            
acronym_regex = r'\b[A-Z]{2,}\b'
#capital_word_regex = r'\b[A-Z][a-z]*\b'
capital_word_regex_not_start_of_line = r'(?!^)\b([A-Z][a-z]\w+)'
#               capital_word_regex_3 = r'(?!^)\b([A-Z][a-z]\w+)'

GeVTwice = r'\b\\GeV+[<>]+\\GeV'

checkList = [
    check("systematics", veto=":systematics"),
    check("kinematics"),
    check("dataset"),
    check("uncertainty on"),
    check("cut"),
    check("[ $]pp[ $]", ignoreCase=False),
    check("Monte Carlo", ignoreCase=False),
    check("Standard Model", ignoreCase=False),
    check("gaussian", ignoreCase=False),
    check("lagrangian", ignoreCase=False),
    check("Fermion",ignoreCase=False),
    check("Boson", ignoreCase=False),
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
    #check(r"\\section"),
    check("cross section times branching fraction"),
    #check(r'(\b[A-Z]+\b)'),
    check([acronym_regex,capital_word_regex_not_start_of_line], ignoreCase=False),
    check(r"(?<!^)Figure",ignoreCase=False),
    check(r"(?<!^)Equation",ignoreCase=False),
    check(r'(?<!\\)TeV',ignoreCase=False, hint="Use \TeV"),
    #check("Figure"),
    check("discriminator", hint='While both words mean "a distinguishing characteristic", “discriminant” is more commonly used in a scientific or mathematical context, and “discriminator” is used in more general parlance. Thus, we should definitely use the former in CMS publications.'),
    check(r" [ZWHb] "),
    check(r" \\GeV"),
    check(r" \\MeV"),
    check(r" \\%"),
    #check("which",veto="in which",hint='"Which" should be used for a nonrestrictive clause, i.e., a parenthetical comment that could be removed from the sentence without changing its meaning. A nonrestrictive clause is always offset in commas. In contrast, "that" should be used to introduce a restrictive clause, and there should be no comma(s). A restrictive clause qualifies the item discussed before it and thus changes the meaning of the sentence.')
]


noNos = ["evidences","informations","importances", "performances", "significances", "It's", "it's","associated to", "stat\.", "sys\.","syst\.","C\.L\."
         "let's", "don't", "can't", "won't", "it's", "shouldn't","data is","data was","Compact Muon Solenoid","Large Hadron Collider"
         ]
for w in noNos:
    checkList.append(check(w))


noHyphens = []
with open("noHyphens.txt", "r") as file:
    for line in file:
        noHyphens.append(line.strip())

noHyphensTwoWords = []
with open("noHyphensTwoWords.txt", "r") as file:
    for line in file:
        noHyphensTwoWords.append(line.strip())

hyphens = []
hyphensTest = []
with open("hyphens.txt", "r") as file:
    for line in file:
        hyphens    .append(line.strip())
        hyphensTest.append(line.strip().replace("-"," "))

        
        
def processLine(line,lineNumber, filename, quiet=False):

    foundIssue = False

    for hyphenWord, hyphenWordTest in zip(hyphens, hyphensTest):                
        if hyphenWordTest in line:
            hashID = hashlib.sha1((hyphenWord+":"+line).encode("UTF-8")).hexdigest()[:10]
            if hashID not in ignoreHashes: 
                if not quiet:
                    print(f"\tWarning {hyphenWord}:{lineNumber}\t{hashID}")
                    print(f"\t\tShould be a hyphen(s) in line \n\t\t {line} ")
                foundIssue = True


    for w in line.split():


        #
        #  IF word has hyphen check if OK
        #
        if "-" in w:
            wNoHyphen = w.replace("-","")
            wNoHyphenTwoWords = w.replace("-"," ")                     
            #print(w,wNoHyphen)
            if wNoHyphen in noHyphens:
                hashID = hashlib.sha1((wNoHyphen+":"+line).encode("UTF-8")).hexdigest()[:10]
                if hashID not in ignoreHashes: 
                    if not quiet:
                        print(f"\tWarning {w}:{lineNumber}\t{hashID}")
                        print(f"\t\tShould be no hyphen in {w} ")
                    foundIssue = True
                    
            if wNoHyphenTwoWords in noHyphensTwoWords:
                hashID = hashlib.sha1((wNoHyphen+":"+line).encode("UTF-8")).hexdigest()[:10]
                if hashID not in ignoreHashes: 
                    if not quiet:
                        print(f"\tWarning {w}:{lineNumber}\t{hashID}")
                        print(f"\t\{line}")
                        print(f"\t\tShould be no hyphen in {w} ")
                    foundIssue = True
                    
            
    for c in checkList:
        val = c(line,lineNumber, filename, quiet=quiet)

        if val:
            foundIssue = True
        #if c in line:
        #    checks[c](c,line,lineNumber, filename)


    return foundIssue
    
    

        

def processFile(filename):
    print(f"{filename}\n")
    lineNumber = 0

    with open(filename, "r") as file:
        for line in file:
            lineNumber += 1 
            if line[0] == "%": continue
            processLine(line, lineNumber, filename)


                
    


def print_file_contents(file_paths):
    for file_path in file_paths:
        processFile(file_path)
                
if __name__ == '__main__':
    file_paths = sys.argv[1:]
    print_file_contents(file_paths)

