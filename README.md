Homemwork 8!

Team: Aahanaa, Lily Ewing

Pseudocode:

```
Algorithm GenDerangements(initialSet, currPerm)
    if currPerm’s length equals the length of initialSet then
        add currPerm to the set of other subsets (external to this algorithm)
    else
        for each element elem in initialSet do
            if elem is not in currPerm then
                append elem to the end of currPerm
                if pos of elem in initial is NOT same as curPerm
                    GenPermutations(initialSet, currPerm)
                remove elem from currPerm

```