# ProofReading

## Usage

setup (only do once per session)
```
> source setup.sh
```

Do the proof reading
```
py proofRead.py ../*tex
```

To ignore a given suggestion, add the suggestion hash to the .prI

```
> prIgnore a74118c148
```

# Links

https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/PubGuidelines

https://docs.google.com/forms/d/e/1FAIpQLSc6fYKz6bnDXkWObLDc6bIjRYMrxTV5CZGc1lBlSmDQAdWhhg/viewform

# To do
   * Alow for a list of vetos
   * allow for and list
   * allow option to turn off hints
   * which /
   * If you are giving a number as a percentage with an uncertainty in the text, use parentheses around the number and its uncertainty. Example: "The muon efficiency is $(94.3 \pm 1.3)\%$."
   * If you are giving a range of percentages, use "2--3%" not "2%--3%". Notice the use of the double hyphen to indicate a range, as discussed in the section on hyphens.



Not added:
If there is no number to the left of the symbol, use curly braces around the symbol to obtain the correct spacing, e.g. "${>} 60\GeV$", ${\pm}3$", "${\approx}4$". The curly braces let LaTeX know that the normally binary operator is spaced as a unary operator. This will leave the correct spacing between the operator and the number.

Only use the equal symbol "=" with integer numbers, not with real numbers. It is correct to write $10 < \pt < 20\GeV$, $\abs{y} < 1.2$. It is incorrect to write "in two bins, $\abs{y} < 0.6$ and $0.6 \leq \abs{y} < 1.2$". It is mathematically impossible that an event has a particle with \abs{y} = 0.6; the rapidity being a real number, it will always be slightly larger or slightly smaller than 0.6 or any other specific number.

In ranges, do not apply the same number of digits unless they have a real meaning. Write, for instance, $0.9 < \abs{y} < 1.25$ and not $0.90 < \abs{y} < 1.25$. It does not make sense to write, for instance, $\abs{y} < 1.50$, because the edges of the bins are decided by the analysts and, hence, have "infinite precision"; they are not the result of a measurement and there is no information content in the number of "zeros". One could just as well write "1.25000000000". It is correct (and important) to write 80.0\invfb, for instance. It is useless and misleading to write "\pt bins of edges $10.0, 12.5, 15.0, 17.5 and 20.0\GeV$.

# Significant Digits:
In CMS papers, the standard is to use at most two significant digits for all quoted uncertainties, unless only one significant digit is appropriate.
The precision quoted for an uncertainty should match the precision quoted for the central value associated with it and the precision of any other associated quoted uncertainties.
Examples:

27.4 ± 0.1 (stat) ± 2.1 (syst): the measurement and the statistical uncertainty are given to only one digit after the decimal point to match the precision of the systematic uncertainty;
27.40 ± 0.14 (stat) ± 0.85 (syst): now the measurement and the statistical uncertainty are given to two digits after the decimal point to match the precision of the systematic uncertainty;
27.4 ± 1.3 (stat) ± 0.2 (syst): the systematic uncertainty is given with only 1 significant digit, to match the precision of the statistical uncertainty.

If an uncertainty is so small compared to the other uncertainties so that this guideline cannot be followed, do not quote the value of that uncertainty. Just say it is negligible compared to the other uncertainties. For example, if the statistical uncertainty in a measurement is ±0.001 and the systematic uncertainty is 2.2, we would quote the result as

Notice our convention for labeling the statistical and systematic uncertainties: "(stat)" and "(syst)", without a period at the end of each abbreviation and with a space before and after the parentheses.



# Acronyms

An acronym (excluding MC names) should not be defined unless the associated phrase is used at least three times in the text. An acronym should be separately defined in the abstract and in the main body of the text, and should be defined in the abstract only if it will be used at least two more times in the abstract. Same thing for the summary: all used acronyms should be redefined, and introduced only if they will be used at least twice more. The acronym should always directly follow the definition, be placed inside parentheses, and may have an "s" added (for example "PDFs") to match the defining phrase. If the "s" is added in the definition, then the acronym without an "s" does not have to be defined also. Similarly, if the acronym without an "s" is defined, then the acronym with an "s" can be used without also defining it.


Do not start a sentence with a symbol.


Refer to your result as a concrete observable
Do not use expressions like "Measurements of \ttbar production are obtained..." or "Limits on the pair production of squarks and gluinos are derived..." because "production" is not an observable. Instead, refer to a concrete observable such as a cross section, a polarization, etc. If it is appropriate to be more generic, you could refer to "properties." Thus, it would be correct to state "Measurements of \ttbar production properties are obtained ..." or "Limits on the cross sections for the pair production of gluinos and squarks are derived..."