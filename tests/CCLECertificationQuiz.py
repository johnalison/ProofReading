import os
import sys

#CCLECertificationQuiz.tex

current_dir = os.path.dirname(__file__)
module_dir = os.path.join(current_dir, '../')

sys.path.append(module_dir)

from proofRead import processLine
#from proofRead import processLine


questions = []
answers = []

def addQA(Qs,As):
    assert len(Qs) == len(As)
    questions.append(Qs)
    answers  .append(As)

addQA([
"The non-perturbative process is controlled by the Long Distance Matrix Element (LDME).",
"The process is controlled by the Long Distance Matrix Element (LDME)."                ,
"The non-perturbative process is controlled by the long distance matrix element (LDME).",
"The nonperturbative process is controlled by the long distance matrix element (LDME).",
],
  [0,0,0,1])

addQA([
"CMS Detector"     ,
"CMS detector"     ,                                             
"The CMS detector" ,                                                        
"Event Selection"  ,                                                   
"Event selection"  ,          
],
 [0,0,1,0,1])

addQA([
"Prompt production cross sections are measured in $pp$ collisions at 13\TeV."    ,
"Prompt production cross sections are measured in pp collisions at 13\TeV."      ,
"Prompt production cross sections are measured in $\Pp\Pp$ collisions at 13~TeV.",
"Prompt production cross sections are measured in $\Pp\Pp$ collisions at 13\TeV.",
"Prompt production cross-sections are measured in $\Pp\Pp$ collisions at 13\TeV.",
],
[0,0,0,1,0])

addQA([
    "The data were collected with the Compact Muon Solenoid (CMS) detector at the Large Hadron Collider (LHC) at CERN.",
    "The data were collected with the CMS detector at the CERN LHC.",
    "The data was collected with the CMS detector at the CERN LHC.",
],
[0,1,0])

addQA([
    "Datasets",
    "Data sets",
    "$150\GeV < \ptmiss < 350\GeV$",
    "$150 < \ptmiss < 350\GeV$",
    ],
[0,1,0,1])

addQA([
    "We present results based on a data sample of proton-proton collisions at $\sqrt{s}=13\TeV$.",
    "Results are presented based on a sample of proton-proton collisions at $\sqrt{s}=13\TeV$."  ,
    "The data were collected with the CMS detector at the LHC."                                  ,
    "The data were collected with CMS at the LHC."                                               ,
],
      [0,1,1,0]) 

addQA([
    "Measurements of $t\overline{t}$ production cross sections are obtained in proton-proton collisions at 13 TeV with a data sample corresponding to an integrated luminosity of 35.9 $fb^{-1}$.",
    "Measurements of \ttbar production cross sections are obtained in proton-proton collisions at 13\TeV with a data sample corresponding to an integrated luminosity of 35.9\fbinv.",
    ],
 [0,1])


# WHich are incorrect
addQA([
    "The invariant mass of the oppositely-charged leptons is calculated.",
    "Nonrelativistic QCD is an effective theory which assumes factorization of the production process...",
    "Nonrelativistic QCD is an effective theory that assumes factorization of the production process...",
    "The statistical uncertainty, that dominates the overall uncertainty, is indicated by the vertical bars..",
    "The statistical uncertainty, which dominates the overall uncertainty, is indicated by the vertical bars...",
],
 [1,1,0,1,0])

addQA([
    "The cross sections are computed using Eqn. 1.",
    "The DY cross sections are computed using Eq. (1).",                         
    "The cross sections are computed using eq. (1).",
],
      [0,1,0])

addQA([
    "The fitting procedure is presented in [11]."          ,         
    "The fitting procedure is presented in Ref. [11]."      ,        
    "The full fitting procedure is presented in ref. [11]."         ,
    ],
 [0,1,0])  

addQA([
"The results are shown in Figure~1."    ,
"The results are shown in Fig.~1."      ,
"Figure~1 shows the results of the fit.",
"Fig.~1 shows the results of the fit."  ,
],
[0,1,1,0])

addQA([
"The results are presented in Table~1."    ,
"The results are presented in Tab.~1."     ,
"Table~1 presents the results of the fit." ,
"Tab.~1 presents the results of the fit."  ,
],
[1,0,1,0])

addQA([
    "The results are presented in Section 7.",
    "The results are presented in Sec. 7",
    "The results are presented in Sect. 7",
    "Section 7 contains a presentation of the results.",
    ],
 [1,0,0,1])

addQA([
    "... with two opposite charge leptons ...",
    "... with two opposite-charge leptons ...",
    "... with two oppositely charged leptons ...",
    "... with two oppositely-charged leptons ...",
    ],
[0,0,1,0]) 

addQA([
    "The 95\% confidence level upper limits on the product $\sigma \times {\mathcal{B}} \times A$ are evaluated...",
    "The 95\% confidence level upper limits on the product of cross section, branching fraction, and acceptance ($\sigma \times {\mathcal{B}} \times A$) are evaluated...",
    "The 95\% confidence level upper limits on the product of cross section, branching fraction, and acceptance ($\sigma {\mathcal{B}} A$) are evaluated...",
    ],
[0,0,1])


addQA([
"The ATLAS and CMS collaborations have...",
"The ATLAS and CMS Collaborations have...",
"The Tevatron and LHC collaborations have...",
"The Tevatron and LHC Collaborations have...",
],
 [0,1,1,0])

addQA([
"...collected at different center-of-mass energies of 7 and 8\TeV." ,
"...collected at center-of-mass energies of 7 and 8\TeV."           ,
"...collected at center-of-mass energies of 7\TeV and 8\TeV."       ,
    ],
 [0,1,0])

# Which of the following is correct
#It is acceptable to use jargon and specialized terms like "compressed SUSY scenarios," "sparticles," "irreducible backgrounds", or "fake leptons" without first defining them, so long as the paper will not be submitted to a journal meant for general readers, like PRL.
#Jargon and specialized terms should be avoided if used only a few times, but otherwise they always need to be defined on first usage, for all papers.
#Symbols do not need to be defined if they are commonly used in the literature or if their meaning should be clear from the context.
#Symbols should always be defined.
#  [0,1,0,1] 


addQA([
    "The data are integrated over the kinematic variables due to the limited number of events.",
    "The data are integrated over the kinematic variables because of the limited number of events.",
    "Due to this subtraction, the resulting difference is sometimes negative.",
    "Because of this subtraction, the resulting difference is sometimes negative.",
    "To evaluate the background due to events with a hadronically decaying tau lepton...",
    "To evaluate the background because of events with a hadronically decaying tau lepton...",
    ],
[0,1,0,1,1,0])

addQA([
    "Measurements of top quark pair production are obtained...",
    "Measurements of top quark pair production properties are obtained...",
    "Limits on the pair production of squarks and gluinos are derived...",
    "Limits on the cross sections for the pair production of squarks and gluinos are derived...",
    ],
[0,1,0,1])

addQA([
    "The final state contains jets and missing transverse energy \MET.",
    "The final state contains jets and missing transverse momentum \MET",
    "The final state contains jets and missing transverse momentum \ptmiss.",
    "The final-state contains jets and missing transverse momentum \ptmiss.",
    ],
[0,0,1,0])

addQA([
    "...are fundamental tests of perturbative QCD (pQCD).",
    "...are fundamental tests of perturbative quantum chromodynamics (pQCD).",
    "...are fundamental tests of perturbative Quantum Chromodynamics (pQCD).",
],
[0,1,0])

addQA([
"...the angular distance between the {\PW} boson and the nearest jet."    ,
"...the angular distance between the W and the nearest jet."              ,
"...the angular distance between the W boson and the nearest jet."        ,
"The Higgs is reconstructed in its decay to four charged leptons."        ,
"The Higgs boson is reconstructed in its decay to four charged leptons."  ,
"Background from events with two tops is evaluated..."                    ,
"Background from events with two top quarks is evaluated..."              ,
],
 [1,0,0,0,1,0,1])

# Final section with out info beyond the body of the paper
# [SUmmary]

# Which of the following hold for the summary section
#   Redefine all acronyms if needed more than twice: otherwise spell them out, e.g., "standard model."
#   Redefine all symbols.
#   Cite all ATLAS papers published before January 2015.
#   Avoid the active ("we") voice.
#  [1,1,0,1]

addQA([
    "According to heavy quark effective theory (HQET), ...",
    "According to Heavy Quark Effective Theory (HQET), ...",
],
      [  1,0])

addQA([
    "The Higgs boson branching fractions to fermions...",
    "The Higgs boson branching ratios to fermions...",],
      [1,0])

#
#The terms "branching ratio" and "branching fraction" are interchangable.
#"Branching fraction" refers to the probability for a certain decay channel, while "branching ratio" is the ratio of branching fractions.
#[0,1]

#
# The data are compared to an NLO calculation interfaced with parton showering and a fixed-order calculation at NNLO.
# The data are compared to an NLO calculation interfaced with parton showering and to a fixed-order calculation at NNLO.
# [0,1]

# Better Style?
#Despite the incredibly broad successes of the standard model, the absence of answers to the hierarchy problem and naturalness among other model shortcomings has led to many theories that go beyond the standard model.
#Despite the success of the standard model (SM), it suffers from the hierarchy problem and has no explanation for phenomena like dark matter. Numerous theories beyond the SM have been proposed to address these shortcomings.
#[0,1]

addQA([
    "This procedure allows to evaluate the isolation efficiency.",
    "This procedure allows the evaluation of the isolation efficiency.",
    "This procedure allows the isolation efficiency to be evaluated.",
    "This identification allows to calibrate the cluster energies more accurately.",
    "This identification allows a more accurate calibration of the cluster energies.",
    ],
      [0,0,1,0,0])
#      [0,0,1,0,0] -> [?,?,Y,?,?]
#      [0,0,1,0,1] -> [?,?,Y,?,Y]
#      [0,1,1,0,1] 

#A sample of events is selected with two isolated same-sign leptons, missing transverse momentum and jets.
#A sample of events is selected with two isolated same-sign leptons, missing transverse momentum, and jets.
#[0,1]

# 
#We exclude at 95\% confidence level excited quarks with masses between 1.0 and 4.4 TeV.
#Excited quarks with masses between 1.0 and 4.4 TeV are excluded at 95\% confidence level.
#Excited quarks with masses between 1.0 and 4.4 TeV are excluded at 95\% CL.
#[0,1,0]

#Photons with $\abs{\eta} < 1.4442$ are selected...
#Photons with $\abs{\eta} < 1.44$ are selected....
# [0,1]

addQA([
    "The 95\% CL upper limit on $\sigma\times {\mathcal{B}}$ for $q^\prime$ production...",
    "The 95\% CL upper limit on the product of cross section and branching fraction ($\sigma{\mathcal{B}}$) for excited quark production...",
    "The 95\% CL upper limit on the product of cross section and branching fraction ($\sigma\times{\mathcal{B}}$) for excited quark production...",
],
      [0,1,0])

addQA([
    "... final states with jets, at least one of which is b-tagged.",
    "... final states with jets, at least one of which is b tagged.",
    "... final states with jets, at least one of which is identified as arising from a bottom quark (b tagged).",
    "... final states with jets, at least one of which is tagged as a bottom quark jet (b tagged).",
    ],
    [0,0,1,1])


addQA([
    "Excited b quarks with mass below 1.6\TeV are excluded...",
    "Excited b-quarks with mass below 1.6\TeV are excluded...",
    ],
      [1,0])

# Horizontal Error bars
#[0,0,1]

#Although the SM has been remarkably successful in describing experimental observations so far, there are still fundamental questions which it leaves unanswered, and...
#Although the SM has been remarkably successful in describing experimental observations, there are fundamental questions that it leaves unanswered, and...
#[0,1]


#We present a search for new physics beyond the standard model in events with...
# We present a search for new physics in events with...
#We present a search for physics beyond the standard model in events with...
# [1,0,0]

#Upper limits at 95% confidence level are set on the resonance production cross-sections.
#Upper limits at 95% confidence level are set on the resonance production cross sections.
#[0,1]

#Search for beyond the standard model physics in events with two leptons
#Search for beyond-the-standard-model physics in events with two leptons
#Search for physics beyond the standard model in events with two leptons
# [0,0,1]

The magnitude \ptmiss of the missing transverse momentum vector \ptvecmiss...
 The magnitude \MET of the missing transverse momentum vector \ptvecmiss...
The magnitude \ETslash of the missing transverse momentum vector \ptvecmiss..
[1,0,0]

addQA([
    "The new physics models probed by this search...",
    "The new-physics models probed by this search...",
    ],
      [0,1])

addQA([
    "...representing a widely-studied extension of the SM.",
    "To search for new-physics, we select a sample of ...",
    "...or from an out-of-acceptance charged lepton.",
    "...from initial- and final-state radiation.",
    "The production cross-section is determined by..."],
      [0,0,1,1,0])

Corrections of 5-12\% are applied.... [one hyphen]
Corrections of 5--12\% are applied.... [two hyphens, i.e., an "en dash" (width on an "n")]
Corrections of 5---12\% are applied... [three hyphens, i.e., an "em dash" (width of an "m")]
Corrections of 5\%--12\% are applied ... [two hyphens, i.e, an "en dash"]
The electron---once identified---is combined... [three hyphens, i.e., an "em dash"]
# [0,1,0,0,1]

Non-prompt Leptons .
Nonprompt Leptons .
Nonprompt leptons .
nonprompt leptons .
[0,0,1,0]

The background due to fake leptons...
The background due to objects erroneously identified as an electron or muon...
[0,1]

The uncertainty in the scale factor...
 The uncertainty on the scale factor...
The uncertainty of the scale factor...
The scale factor uncertainty...
[1,0,0,1]

The modelling of certain quantities, i.e., the flavour composition, depends on the centre-of-mass energy.
The modeling of certain quantities, i.e., the flavor composition, depends on the centre-of-mass energy.
The modelling of certain quantities, i.e. the flavour composition, depends on the centre-of-mass energy.
The modeling of certain quantities, i.e., the flavor composition, depends on the center-of-mass energy.
[0,0,1,1]

...and are required to lie within 24 cm of the beam axis.
...and are required to lie within 24\unit{cm} of the beam axis.
 ...and are required to lie within 24~cm of the beam axis.
A cylindrical superconducting solenoid with an inner diameter of 6\unit{m} provides a 3.8\unit{T} axial magnetic field. 
A cylindrical superconducting solenoid with an inner diameter of 6~m provides a 3.8~T axial magnetic field.
A cylindrical superconducting solenoid with an inner diameter of $6\,$m provides a $3.8\,$T axial magnetic field.
[0,1,0,1,0,0]

Table captions go above the table and figure captions go below the figure.
Table and figure captions both go below the table or figure.
Table and figure captions both go above the table or figure.
[1,0,0]

The observed number $N_{obs}$ of events... .
The observed number $N_{\mathrm{obs}}$ of events... .
The observed number $N_{\text{obs}}$ of events... .
The observed number $N_{\text{observed}}$ of events... .
The observed number $n_{\text{obs}}$ of events... .
[0,0,1,0,0]

The gluino mass $M_{\text{gluino}}$ is ... .
The gluino mass $m_{\text{gluino}}$ is... .
The gluino mass $m_{\~{g}}$ is... .
The gluino mass $m_{\PSg}$ is... .
The gluino mass $M_{\PSg}}$ is... .
 [0,1,0,1,0]

lineNumber = 0
for iq, qList in enumerate(questions):
    print(f"Question {iq}\n")
    for line in qList:
        lineNumber += 1 
        if line[0] == "%": continue
        foundProblem = processLine(line, lineNumber, "Test", quiet=True)
    
        if foundProblem:
            print("\tERROR:",line)
            #processLine(line, lineNumber, "Test", quiet=False)
        else: print(f"\tOK: {line}")

    print(f"\n\n")        






#
Correct answers:


The observed number $N_{\text{obs}}$ of events... .


The gluino mass $m_{\text{gluino}}$ is... .


# Wrong answers:

... final states with jets, at least one of which is b-tagged.
... final states with jets, at least one of which is b tagged.
X ... final states with jets, at least one of which is identified as arising from a bottom quark (b tagged).
 ... final states with jets, at least one of which is tagged as a bottom quark jet (b tagged).


 This procedure allows to evaluate the isolation efficiency.
This procedure allows the evaluation of the isolation efficiency.
X This procedure allows the isolation efficiency to be evaluated. 
This identification allows to calibrate the cluster energies more accurately.
This identification allows a more accurate calibration of the cluster energies.


X Redefine all acronyms if needed more than twice: otherwise spell them out, e.g., "standard model." 
Redefine all symbols.
Cite all ATLAS papers published before January 2015.
X Avoid the active ("we") voice.


It is acceptable to use jargon and specialized terms like "compressed SUSY scenarios," "sparticles," "irreducible backgrounds", or "fake leptons" without first defining them, so long as the paper will not be submitted to a journal meant for general readers, like PRL.
Jargon and specialized terms should be avoided if used only a few times, but otherwise they always need to be defined on first usage, for all papers.
 
X Symbols do not need to be defined if they are commonly used in the literature or if their meaning should be clear from the context.
Symbols should always be defined.
