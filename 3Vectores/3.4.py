import numpy as np
from math import atan2
from math import pi
from math import degrees
from math import sqrt
from math import cos

a = np.array([1,3])
b = np.array([-4,6])

ma = sqrt((a[0])**2+(a[1])**2)
mb = sqrt((b[0])**2+(b[1])**2)

 
anga = atan2(a[1],a[0])
angb = atan2(b[1],b[0])

angr = anga - angb
mr = sqrt((ma**2)+(mb**2)+(2*ma*mb*cos(angr)))

print a,b
print "angulo entre los dos vectores %.2f"%degrees(angr)
print "magnitud de vector a %.2f"%ma
print "magnitud de vector b %.2f"%mb
print "magnitud de vector resultante %.2f"%mr

#degrees  = angulo*(180/pi)
print anga
print angb
c = a + b
print type(c)
print c

