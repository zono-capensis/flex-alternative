import sys
import os.path
sys.path.insert(0, os.path.abspath('../data'))
from  structures import Stack
from structures import Finite_automata
"""transitions
{q0:{a:[...], b[...]}, q1:{a:[...], b[...]}}
"""
class SubsetConstruction:
    def __init__(self, nfa: Finite_automata):
        self.nfa = nfa
    def calculeEpsClosure(self, T):
        stack = Stack(T)
        epsClosure = T
        while len(stack) != 0:
            t = stack.pop()
            if "eps" in self.nfa.transitions[t]:
                for u in self.nfa.transitions[t]["eps"]:
                    if u not in epsClosure:
                        epsClosure.append(u)
                        stack.push(u)
        return epsClosure

