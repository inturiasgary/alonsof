"""
masa de carga = 1500 kg.
mas de canastilla   = 20 kg.
altura de alzada =  10 m.
tiempo de ascenso = 4 min.
potencia 2 hp.
revoluciones del motor =    1750 rpm.
revoluciones de salida =    56 rpm.
relacion de reduccion =     31,25 / 1

Variables:
    i = relacion reduccion
"""
from math import radians, sin, tan, cos, degrees, pi
#Primer tren (calculo en sistema metrico)
plg_a_milimetros = 25.4

def diap(z=0, alfa=0, m=0):
    return (z*m/cos(alfa))

def pasoAxial(z=0, diametrop=0, alfa=0):
    return (pi*diametrop*(1/tan(alfa))/z)

def parTorsional(potencia=0, rpm=0):
    return (63025*(potencia/rpm))
i = 6.2
rpm_motor = 1750.0
alfa = 10.0#15
potencia = 2.0 #en hp
dp = 20.0
z_pinon1 = 63.0#19
z_engranaje1 = 118

alfa = radians(alfa)
#modulo = (25.4/dp)
modulo = 5.0
ht = modulo*2.25


print "alfa %.2f"%degrees(alfa)
print "modulo %.2f"%modulo
print "dientes pinon %.2f"%z_pinon1
print "diametro primitivo del pinon %.2f mm."%diap(z_pinon1, alfa, modulo)
print "altura de diente %.2f mm."%ht
print "paso axial %.2f mm."%pasoAxial(z_pinon1, diap(z_pinon1, alfa, modulo), alfa)
print "ancho de cara %.2f mm."%(2*pasoAxial(z_pinon1, diap(z_pinon1, alfa, modulo), alfa))
print "ancho de cara 2 --> %.2f mm."%((modulo*pi/cos(alfa)*4.5))
print "par torsional %.2f lb./plg."%parTorsional(potencia, rpm_motor) 

print "=== Cargas pinon  ==="
print "carga tangencial %.2f kg."%((parTorsional(potencia, rpm_motor)/((diap(z_pinon1, alfa, modulo)/25.4)/2.0))*0.45359237)
print "carga radial %.2f kg."%(((parTorsional(potencia, rpm_motor)/((diap(z_pinon1, alfa, modulo)/25.4)/2.0))*0.45359237)*tan(radians(20))*(1/cos(alfa)))
print "carga axial %.2f kg."%(((parTorsional(potencia, rpm_motor)/((diap(z_pinon1, alfa, modulo)/25.4/2.0))*0.45359237))*tan(alfa))
