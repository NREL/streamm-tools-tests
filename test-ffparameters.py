#!/usr/bin/env python

from parameters import ParameterContainer
from parameters import BondtypesContainer
from parameters import AngletypesContainer
from parameters import DihtypesContainer
from parameters import ljtype
from parameters import bondtype
from parameters import angletype
from parameters import dihtype


def main():
    """
    TRAVIS document
    """
    # Create parameter container
    paramC =  ParameterContainer()

    ljtypC_p = paramC.ljtypC
    btypC_p = paramC.btypC
    atypC_p = paramC.atypC
    dtypC_p = paramC.dtypC

    # Create atom with Lennard Jones  parameters 
    ljObj_p = ljtype( "CA" ) 
    ljObj_p.setmass(12.0 )
    ljObj_p.setparam( 0.5,1.04 )
    ljtypC_p.put(ljObj_p)


    btype = "harmonic"
    btypObj_p = bondtype( "CA","CB", btype )
    if( btype == "harmonic" ):
        btypObj_p.setharmonic( 1.05 , 100.0  )
    btypC_p.put(btypObj_p)


    atype = "harmonic" 
    atypObj_p = angletype( "CC","CA","CB", atype )
    if( atype == "harmonic" ):
        theta0 = 0.0 
        kb  = 1.2
        atypObj_p.setharmonic(theta0, kb )
    atypC_p.put(atypObj_p)

    dtype =  "opls"
    dtypObj_p = dihtype( "CD","CA","CB","CC" , dtype )
    if( dtype== "opls" ):
        k1 = 3.3 
        k2 =  0.0 
        k3 = -2.3 
        k4 = 0.0 
        dtypObj_p.setopls(k1,k2,k3,k4)
    dtypC_p.put(dtypObj_p)


    dtype =  "harmonic"
    dtypObj_p = dihtype( "HD","CA","CB","HC" , dtype )
    if( dtype== "harmonic" ):
        d = 1.0
        mult = 0.0
        kb = 10.1
        theat_s = 90.0 
        dtypObj_p.setopls( d, mult, kb,theat_s )
    dtypC_p.put(dtypObj_p)


    dtype =  "harmonic"
    dtypObj_p = dihtype( "HD","CA","CB","S" , dtype )        
    if( dtype== "rb" ):
        C0= 0.2
        C1= 9.2
        C2= 4.1
        C3= 2.3
        C4= 6.2
        C5 = 1.0
        dtypObj_p.setrb(C0,C1,C2,C3,C4,C5 )
    dtypC_p.put(dtypObj_p)


    print " LJ paramters have been read in "
    for  ljid, ljtypObj in paramC.ljtypC:
        print ljtypObj

    print " Bonds have been read in "
    for  bid, btypObj in paramC.btypC:
        print btypObj


    print " Angles have been read in "
    for  aid, atypObj in paramC.atypC:
        print atypObj

    print " Dihedrals have been read in "
    for  did, dtypObj in paramC.dtypC:
        print dtypObj

if __name__ == '__main__':
    main()
