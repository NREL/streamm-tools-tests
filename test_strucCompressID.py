#!/usr/bin/env python
import os, sys, math, random, time

from particles import Particle
from particles import ParticleContainer

from bonds import Bond
from bonds import BondContainer

from structureContainer import StructureContainer


def main():
    """
    This test shows how reorder (compress) global IDs for a StructureContainer
    """
    p1 = Particle( [0.2, 1.3,  33.0], "Si", 2.0, 1.23)
    p2 = Particle( [5.0, 2.3, -22.1], "C",  1.0, 2.34)
    p3 = Particle( [5.0, 2.3, -20.1], "C",  1.0, 2.34)

    b1 = Bond( 1, 2, 1.233, "hooke")
    b2 = Bond( 2, 3, 0.500, "hooke")

    atoms1   = ParticleContainer()
    atoms1.put(p1)
    atoms1.put(p2)
    atoms1.put(p3)

    bonds1   = BondContainer()
    bonds1.put(b1)
    bonds1.put(b2)

    polymer1 = StructureContainer(atoms1, bonds1)  # Complete structure 1

    p1other = Particle( [0.0, 2.3, -20.1], "C",  1.0, 2.34)
    p2other = Particle( [50.0, 0.3, -0.1], "Ar", 2.0, 2.34)
    p3other = Particle( [50.0, 0.3, -0.1], "Ar", 2.0, 2.34)

    b1other = Bond( 1, 3, 1.233, "hooke")    # Correct ptclIDs for second structure

    atoms2 = ParticleContainer()
    atoms2.put(p1other)
    atoms2.put(p2other)
    atoms2.put(p3other)

    del atoms2[2] # remove 2nd particle so ID's are non-consecutive

    bonds2   = BondContainer()
    bonds2.put(b1other)

    polymer2 = StructureContainer(atoms2, bonds2)  # Complete structure 1 completely

    del p1, p2, p3, p1other, p2other, b1, b2, b1other, atoms1, atoms2, bonds1, bonds2
    print "\n Cleaning memory for initial objects \n" 

    print "-------------------- Before adding --------------------"
    print "polymer1 = ", polymer1
    print "polymer2 = ", polymer2
    print " "

    print "-------------------- After adding --------------------"
    polymer2 += polymer1
    print "polymer2 = ", polymer2

    polymer2.compressPtclIDs()

    print "-------------------- After compressing --------------------"
    print "polymer2 = ", polymer2

if __name__ == '__main__':
    main()
