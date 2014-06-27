#!/usr/bin/env python
"""
Class data structures for atomic data
"""

import copy

diagramBefore="""
1--'b1'---2
 -        |
  -       'b2'
   'b4'   |
     -    |
       -  3---'b3'---4
"""

diagramAfter="""
5--'b1'---2
 -        |
  -       'b2'
   'b4'   |
     -    |
       -  3---'b3'---4
"""


import os, sys, math, random, time

from particles import Particle
from particles import ParticleContainer

from bonds import Bond
from bonds import BondContainer

from structureContainer import StructureContainer

print "************************************************************************************"
print " This test shows how to set up Structure container with Particle/Bond-Containers \n"
print " Shows how ID changed in Structure propagate to values set in BondContainer for its "
print "    held particle ID values \n"
print " Illustrates how a substructure method could return subgroup"
print "************************************************************************************ \n"

p1 = Particle( [0.2, 1.3,  33.0], "Si", 2.0, 1.23)
p2 = Particle( [5.0, 2.3, -22.1], "C",  1.0, 2.34)
p3 = Particle( [5.0, 2.3, -20.1], "C",  1.0, 2.34)
p4 = Particle( [0.0, 2.3, -20.1], "C",  1.0, 2.34)

b1 = Bond( 1, 2, 1.233, "hooke")
b2 = Bond( 2, 3, 0.500, "hooke")
b3 = Bond( 3, 4, 2.301, "hooke")
b4 = Bond( 1, 3, 0.828, "hooke")

atoms1 = ParticleContainer()
atoms1.put(p1)
atoms1.put(p2)
atoms1.put(p3)
atoms1.put(p4)

bonds = BondContainer()
bonds.put(b1)
bonds.put(b2)
bonds.put(b3)
bonds.put(b4)

del p1, p2, p3, p4, b1, b2, b3, b4
polymer1 = StructureContainer(atoms1, bonds)
del atoms1, bonds


print "********************************************************** \n"
print polymer1
print diagramBefore
polymer1.replacePtclIDs(1,5)
print "Testing ID changing with 'polymer1.replacePtclIDs(1,5)' "
print  polymer1
print diagramAfter
print "********************************************************** \n"

print "********************************************************** \n"
print "Testing polymer1.getSubStructure([5,2])"
print " currently ID's are reassigned in substructure \n"
subpolymer = polymer1.getSubStructure([5,2])
print subpolymer
subpolymer.ptclC[1].position = [12.0, -3838.0, 1.0]
print "Substructure contains (Bonds re-assign not set yet)", subpolymer
print "********************************************************** \n"

print "********************************************************** \n"
print "polymer1 Struture after returning sub-structure"
print polymer1
print "********************************************************** \n"
