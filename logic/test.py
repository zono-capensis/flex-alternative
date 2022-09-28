import os
import sys
sys.path.insert(0, os.path.abspath('../data'))
from structures import Finite_automata
import nfaToDfa
nfa = Finite_automata(["a", "b"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, [10],
    {
        0: {"":[1,7]},
        1: {"":[2,4]},
        2: {"a":[3]},
        3: {"":[6]},
        4: {"b":[5]},
        5: {"":[6]},
        6: {"":[1,7]},
        7: {"a":[8]},
        8: {"b":[9]},
        9: {"b":[10]},
        10: {}
     }
)
trans = nfaToDfa.SubsetConstruction(nfa)
print(trans.calculeSubsetConstruction())
