#!/usr/bin/env python
import os, sys, math, random, time

from particles import Particle
from particles import ParticleContainer

from bonds import Bond
from bonds import BondContainer

from angles import Angle
from angles import AngleContainer

from structureContainer import StructureContainer

def main():
    """
    This test shows compressing IDs when structureContainer has angles included
    """

    p1 = Particle( [1.1, 1.1, 1.1], "Si", 2.0, 1.23)
    p2 = Particle( [2.2, 2.2, 2.2], "Si",  1.0, 2.34)
    p3 = Particle( [3.3, 3.3, 3.3], "Si",  1.0, 2.34)
    p4 = Particle( [0.0, 0.0, 0.0], "Si",  1.0, 2.34)
    #
    p5 = Particle( [4.4, 4.4, 4.4], "C",  1.0, 2.34)   # 1
    p6 = Particle( [5.5, 5.5, 5.5], "C",  1.0, 2.34)   # 2
    p7 = Particle( [6.6, 6.6, 6.6], "C",  1.0, 2.34)   # 3

    b1 = Bond( 1, 3, 1.11, "hooke")
    b2 = Bond( 3, 4, 2.22, "hooke")
    #
    b3 = Bond( 1, 2, 3.33, "hooke")
    b4 = Bond( 2, 3, 4.44, "hooke")

    a1 = Angle(1, 3, 4, 1.11, "harmonic")
    #
    a2 = Angle(1, 2, 3, 2.22, "harmonic")

    atoms1 = ParticleContainer()
    atoms2 = ParticleContainer()
    atoms1.put(p1)
    atoms1.put(p2)
    atoms1.put(p3)
    atoms1.put(p4)
    #
    atoms2.put(p5)
    atoms2.put(p6)
    atoms2.put(p7)

    del atoms1[2] # remove 2nd particle so ID's are non-consecutive

    bonds1 = BondContainer()
    bonds2 = BondContainer()
    bonds1.put(b1)
    bonds1.put(b2)
    bonds2.put(b3)
    bonds2.put(b4)

    angles1 = AngleContainer()
    angles2 = AngleContainer()
    angles1.put(a1)
    angles2.put(a2)

    polymer1 = StructureContainer(atoms1, bonds1, angles1)
    polymer2 = StructureContainer(atoms2, bonds2, angles2)


    del p1, p2, p3, p4, p5, p6, b1, b2, b3, b4, a1, a2
    del atoms1, atoms2, bonds1, bonds2, angles1, angles2
    print "\n Cleaning memory for initial objects \n" 

    print "-------------------- Initial structures --------------------"
    print "polymer1 = ", polymer1
    print "polymer2 = ", polymer2
    print " "

    print "-------------- After adding  (polymer2 += polymer1) ----------------"
    polymer2 += polymer1
    print "polymer2 = ", polymer2

    polymer2.compressPtclIDs()

    print "-------------------- After compressing --------------------"
    print "polymer2 = ", polymer2


if __name__ == '__main__':
    main()
