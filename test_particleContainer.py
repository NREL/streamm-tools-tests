#!/usr/bin/env python

import os, sys, math, random, time

from particles import Particle
from particles import ParticleContainer

def main():
    """
    This test shows various operators within Particle and ParticleContainer classes.
    Shows memory management structure and access methods.
    """
    p1 = Particle( [0.2, 1.3,  33.0], "Si", 2.0, 1.23)
    p2 = Particle( [5.0, 2.3, -22.1], "C",  1.0, 2.34)
    p3 = Particle( [5.0, 2.3, -20.1], "C",  1.0, 2.34)
    p4 = Particle( [0.0, 2.3, -20.1], "C",  1.0, 2.34)

    atoms1 = ParticleContainer()
    atoms2 = ParticleContainer()

    atoms1.put(p1)
    atoms1.put(p2)
    #
    atoms2.put(p3)
    atoms2.put(p4)

    del p1, p2, p3, p4
    print "\n Cleaning memory for initial objects \n" 

    print "x = atoms1[1] returns x as an effective 'reference' \n"
    x = atoms1[1]
    print "x = ", x.__dict__, "\n"
    x.position=[1.0, 1.0, 1.0]
    print "after changing with x.position = [1.0, 1.0, 1.0]"
    print "x = ", x.__dict__, "\n"

    # This value has been changed by code above
    print "atoms1 has been changed"
    print atoms1

    print "before, atoms1--> ", atoms1, "\n"
    del atoms1[2]
    print "after 'del atoms1[2]' atoms1 --> ", atoms1, "\n"

    print "Testing 'in' operator (1 in atoms1)"
    if (1 in atoms1):
        print "atoms1 contains gid 1"
    else:
        print "key not found in atoms1"

    print "Testing 'in' operator (5 in atoms1)"
    if (5 in atoms1):
        print "atoms1 contains gid 5"
    else:
        print "key not found in atoms1"

    print " "
    atoms1 += atoms2
    print "Will print the new atoms1 after adding atoms1 += atoms2"
    print atoms1

if __name__ == '__main__':
    main()
