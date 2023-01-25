import numpy as np
import scipy
import matplotlib.pyplot as plt
from materials import SS304, Teflon

T_low=40
T_high=300

def Q(A, l, K):
    return (A/l)*K

def calc_SS_coax(cross_sections, length, number):
    #cross sections a tuple in order Jacket, outer, dielectric, center
    SS=SS304()
    Tef=Teflon()
    if T_low<4:
        print('Extrapolating NIST curve')
        Q_jacket=Q(cross_sections[0], length, Tef.integrate_TC_low(T_low, T_high))
        Q_outer=Q(cross_sections[1], length, SS.integrate_TC_low(T_low, T_high))
        Q_dielectric=Q(cross_sections[2], length, Tef.integrate_TC_low(T_low, T_high))
        Q_center=Q(cross_sections[3], length, SS.integrate_TC_low(T_low, T_high))

        Q_total=number_cables*(Q_jacket+Q_outer+Q_dielectric+Q_center)

        return Q_total
    else:
        print('Using NIST curve')
        Q_jacket=Q(cross_sections[0], length, Tef.integrate_TC(T_low, T_high))
        Q_outer=Q(cross_sections[1], length, SS.integrate_TC(T_low, T_high))
        Q_dielectric=Q(cross_sections[2], length, Tef.integrate_TC(T_low, T_high))
        Q_center=Q(cross_sections[3], length, SS.integrate_TC(T_low, T_high))

        Q_total=number_cables*(Q_jacket+Q_outer+Q_dielectric+Q_center)

        return Q_total


SS_microcoax_CS=(4.135e-7, 9.516e-8, 9.729e-8, 3.153e-8)
cable_length=100e-3
number_cables=1000

Q_tot=calc_SS_coax(SS_microcoax_CS, cable_length, number_cables)

print(Q_tot)

