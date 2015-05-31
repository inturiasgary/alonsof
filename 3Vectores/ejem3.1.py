from math import pi
from math import sqrt
from math import cos
from math import degrees
from math import radians
from math import atan2
from math import asin
from math import sin
import numpy as np


ma = 6	#Magnitud de vector a
anga = radians(36)	#vector a tienen angulo de 36 grados con respecto a x
mb = 7	#magnitud del vector b
b = np.array([-7,0])	#vector b

bx=b[0]
by=b[1]
angb = atan2(by,bx)	#angulo del vector b respecto a la abcisa
if ((bx <0)and(by<0)):
	angb = (angb*-1)+(pi/2)
	print angb
elif ((bx >=0)and(by<0)):
	angb = angb+(2*pi)

angc= angb - anga	#angulo entre el vector b y vector a
mc = sqrt(ma**2+mb**2+2*ma*mb*cos(angc))	#magnitud del vector c
print mc
print degrees(angb) 
#encrontramos el angulo entre c y a	
angaux = asin((7*sin(angc)/mc))
print abs(degrees(angaux))
