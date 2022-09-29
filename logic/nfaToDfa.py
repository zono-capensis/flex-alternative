from inspect import stack
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
        if not hasattr(T, "__len__"):
            T = [T]
        stack = Stack(T)
        epsClosure = T
        while len(stack) != 0:
            t = stack.pop()
            if "" in self.nfa.transitions[t]:
                for u in self.nfa.transitions[t][""]:
                    if u not in epsClosure:
                        epsClosure.append(u)
                        stack.push(u)
        return epsClosure
    def move(self, T, a):
        states = set()
        for t in T:
            if a in self.nfa.transitions[t]:
                states.update(self.nfa.transitions[t][a])
        return list(states)
    def setAsInt(self, list):
        rep = [0]*len(self.nfa.states)
        for i in list:
            rep[i] = 1
        return int("".join(map(str, rep)),2)
    def intAsSet(self, num):
        setRep = []
        binRep = "{0:b}".format(num).zfill(len(self.nfa.states))
        for i in range(len(binRep)):
            if binRep[i] == "1":
                setRep.append(i)
        return setRep
    def prettyStates(self, list):
        pass
    def isAccepting(self, list):
        for state in list:
            if state in self.nfa.accepting_states:
                return True
        return False
    def calculeSubsetConstruction(self):
        unmarked = Stack()
        dStates = [self.setAsInt(self.calculeEpsClosure(self.nfa.initial_state))]
        startState = dStates[0]
        acceptingStates = []
        unmarked.push(0)
        dTran = {}
        while len(unmarked) > 0:
            TN = unmarked.pop()
            T = self.intAsSet(dStates[TN])
            for a in self.nfa.alphabet:
                U = self.calculeEpsClosure(self.move(T, a))
                aliasU = self.setAsInt(U)
                if aliasU not in dStates:
                    if self.isAccepting(U):
                        acceptingStates.append(aliasU)
                    dStates.append(aliasU)
                    unmarked.push(len(dStates) - 1)
                if not dStates[TN] in dTran:
                    dTran[dStates[TN]]={}
                if not a in dTran[dStates[TN]]:
                    dTran[dStates[TN]][a]=[]
                dTran[dStates[TN]][a].append(self.setAsInt(U))
        return Finite_automata(self.nfa.alphabet, dStates, startState, acceptingStates, dTran)