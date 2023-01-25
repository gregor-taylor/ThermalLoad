from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class SS304():
    def __init__(self):
        #define material here
        self.thermal_conductivity={'a':-1.4087, 
                                   'b':1.3982, 
                                   'c':0.2543, 
                                   'd':-0.6260,
                                   'e':0.2334,
                                   'f':0.4256,
                                   'g':-0.4658,
                                   'h':0.1650,
                                   'i':-0.0199}
                                   
    def heatConductivity(self, T):
        return 10**(self.thermal_conductivity['a']+self.thermal_conductivity['b']*(np.log10(T))+self.thermal_conductivity['c']*((np.log10(T))**2)
                +self.thermal_conductivity['d']*((np.log10(T))**3)+self.thermal_conductivity['e']*((np.log10(T))**4)
                +self.thermal_conductivity['f']*((np.log10(T))**5)+self.thermal_conductivity['g']*((np.log10(T))**6)
                +self.thermal_conductivity['h']*((np.log10(T))**7)+self.thermal_conductivity['i']*((np.log10(T))**8))
    def extrapolate_low_temp(self):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T)
        T_low=T[:10]
        y_low=y[:10]
        func_lowtemp=interp1d(T_low, y_low, fill_value='extrapolate')
        return func_lowtemp
    def plot_Tcond(self):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T)
        func_lowtemp=self.extrapolate_low_temp()
        T_low=np.linspace(0,4,100)
        y_low=func_lowtemp(T_low)
        plt.plot(T, y)
        plt.plot(T_low,y_low)
        plt.show()
    def integrate_TC(self, Tlow, Thigh):    
        lamb, _=quad(self.heatConductivity, Tlow, Thigh)
        return lamb
    def integrate_TC_low(self, Tlow, Thigh):  
        func=self.extrapolate_low_temp()  
        lamb, _=quad(func, Tlow, Thigh)
        return lamb

class Teflon():
    def __init__(self):
        #define material here
        self.thermal_conductivity={'a':2.7380, 
                                   'b':-30.677, 
                                   'c':89.430, 
                                   'd':-136.99,
                                   'e':124.69,
                                   'f':-69.556,
                                   'g':23.320,
                                   'h':-4.3135,
                                   'i':0.33829}
                                   
    def heatConductivity(self, T):
        return 10**(self.thermal_conductivity['a']+self.thermal_conductivity['b']*(np.log10(T))+self.thermal_conductivity['c']*((np.log10(T))**2)
                +self.thermal_conductivity['d']*((np.log10(T))**3)+self.thermal_conductivity['e']*((np.log10(T))**4)
                +self.thermal_conductivity['f']*((np.log10(T))**5)+self.thermal_conductivity['g']*((np.log10(T))**6)
                +self.thermal_conductivity['h']*((np.log10(T))**7)+self.thermal_conductivity['i']*((np.log10(T))**8))
    def extrapolate_low_temp(self):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T)
        T_low=T[:10]
        y_low=y[:10]
        func_lowtemp=interp1d(T_low, y_low, fill_value='extrapolate')
        return func_lowtemp
    def plot_Tcond(self):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T)
        func_lowtemp=self.extrapolate_low_temp()
        T_low=np.linspace(0,4,100)
        y_low=func_lowtemp(T_low)
        plt.plot(T, y)
        plt.plot(T_low,y_low)
        plt.show()
    def integrate_TC(self, Tlow, Thigh):    
        lamb, _=quad(self.heatConductivity, Tlow, Thigh)
        return lamb
    def integrate_TC_low(self, Tlow, Thigh):  
        func=self.extrapolate_low_temp()  
        lamb, _=quad(func, Tlow, Thigh)
        return lamb

if __name__=='__main__':
    mat=SS304()
    mat.plot_Tcond()

#TODO
#NIST have data to 4 k so, extrapolate down to 0K, fit that func, use that for the cold stages.






