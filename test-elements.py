from periodictable import periodictable
#import periodictable

# Set periodic table element 
pt = periodictable()

for el_symb in pt.elements:
    print " symb %s mass %f "%(pt.elements[el_symb].symbol,  pt.elements[el_symb].mass)

find_mass = 12.0110
el = pt.getelementWithMass(find_mass)
print " Element with mass %f is %s "%(find_mass,el.symbol)
print " number ",el.number
print " mass",el.mass
print " cov_radii",el.cov_radii
print " vdw_radii",el.vdw_radii

atomic_symb = "S"
el = pt.getelementWithSymbol(atomic_symb)
print " Element with symbol %s is %s "%(atomic_symb,el.symbol)
print " number ",el.number
print " mass",el.mass
print " cov_radii",el.cov_radii
print " vdw_radii",el.vdw_radii





