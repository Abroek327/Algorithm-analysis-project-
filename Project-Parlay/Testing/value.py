import random
import math
import itertools
from prettytable import PrettyTable
from hypoParlay import hypoParlay
import numpy as np
from valueSimulator import valueSim


optimals = []


def binFit():
    pass

def parlayBuilder(binWidth):
    pass

def sort_and_file(parlayList):
    pass

def main():
    binWidths = [3,5,7,9,10,11,13,15,20]
    AllParlays = []

    for x in binWidths:
        AllParlays.extend(parlayBuilder(x))


    for t in AllParlays:
        valueSim.simulate_practical(t) 
        valueSim.simulate_theoretical(t)

    sf = sort_and_file(AllParlays)

    for x in range(len(sf)):
        optimals[x] = valueSim.maxValue(sf[x])



main()