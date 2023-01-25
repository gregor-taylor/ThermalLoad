from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class SS304():
    def __init__(self):
        #Valid 4-300 K
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
        plt.ylabel("Thermal Conductivity W/m.K")
        plt.xlabel("Temp (K)")
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
        #Valid 4-300 K
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
        plt.ylabel("Thermal Conductivity W/m.K")
        plt.xlabel("Temp (K)")
        plt.show()
    def integrate_TC(self, Tlow, Thigh):    
        lamb, _=quad(self.heatConductivity, Tlow, Thigh)
        return lamb
    def integrate_TC_low(self, Tlow, Thigh):  
        func=self.extrapolate_low_temp()  
        lamb, _=quad(func, Tlow, Thigh)
        return lamb

class OFHC_Cu():
    def __init__(self):
        #Valid 4-300 K
        self.thermal_conductivity={'RRR50':
                                   {'a':1.8743, 
                                    'b':-0.41538, 
                                    'c':-0.6018, 
                                    'd':0.13294,
                                    'e':0.26426,
                                    'f':-0.0219,
                                    'g':-0.051276,
                                    'h':0.0014871,
                                    'i':0.003723},
                                   'RRR100':
                                   {'a':2.2154, 
                                    'b':-0.47461, 
                                    'c':-0.88068, 
                                    'd':0.13871,
                                    'e':0.29505,
                                    'f':-0.02043,
                                    'g':-0.04831,
                                    'h':0.001281,
                                    'i':0.003207},
                                   'RRR150':
                                   {'a':2.3797, 
                                    'b':-0.4918, 
                                    'c':-0.98615, 
                                    'd':0.13942,
                                    'e':0.30475,
                                    'f':-0.019713,
                                    'g':-0.046897,
                                    'h':0.0011969,
                                    'i':0.0029988},
                                   'RRR300':
                                   {'a':1.357, 
                                    'b':0.3981, 
                                    'c':2.669, 
                                    'd':-0.1346,
                                    'e':-0.6683,
                                    'f':0.01342,
                                    'g':0.05773,
                                    'h':0.0002147,
                                    'i':0.0},
                                   'RRR500':
                                   {'a':2.8075, 
                                    'b':-0.54074, 
                                    'c':-1.2777, 
                                    'd':0.15362,
                                    'e':0.36444,
                                    'f':-0.02105,
                                    'g':-0.051727,
                                    'h':0.0012226,
                                    'i':0.0030964}
                                   }

                                   
    def heatConductivity(self, T, RRR):
        return 10**(((self.thermal_conductivity[RRR]['a'])+(self.thermal_conductivity[RRR]['c']*(T**0.5))+
            (self.thermal_conductivity[RRR]['e']*(T))+(self.thermal_conductivity[RRR]['g']*(T**1.5))+
            (self.thermal_conductivity[RRR]['i']*(T**2)))
            /
            ((1)+(self.thermal_conductivity[RRR]['b']*(T**0.5))+
            (self.thermal_conductivity[RRR]['d']*(T))+(self.thermal_conductivity[RRR]['f']*(T**1.5))+
            (self.thermal_conductivity[RRR]['h']*(T**2))))
    def extrapolate_low_temp(self, RRR):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T, RRR)
        T_low=T[:10]
        y_low=y[:10]
        func_lowtemp=interp1d(T_low, y_low, fill_value='extrapolate')
        return func_lowtemp
    def plot_Tcond(self, RRR):
        T=np.linspace(4,300,2000)
        y=self.heatConductivity(T, RRR)
        func_lowtemp=self.extrapolate_low_temp(RRR)
        T_low=np.linspace(0,4,100)
        y_low=func_lowtemp(T_low)
        plt.plot(T, y)
        plt.plot(T_low,y_low)
        plt.ylabel("Thermal Conductivity W/m.K")
        plt.xlabel("Temp (K)")
        plt.show()
    def plot_all_RRRs(self):
        RRRs=['RRR50', 'RRR100', 'RRR150', 'RRR300', 'RRR500']
        T=np.linspace(4,300,2000)
        for r in RRRs:
            y=self.heatConductivity(T, r)
            func_lowtemp=self.extrapolate_low_temp(r)
            T_low=np.linspace(0,4,100)
            y_low=func_lowtemp(T_low)
            plt.plot(T, y)
            plt.plot(T_low,y_low)
        plt.legend(['RRR50','RRR50_ext','RRR100','RRR100_ext','RRR150','RR150_ext','RRR300','RR300_ext','RRR500','RRR500_ext'])
        plt.ylabel("Thermal Conductivity W/m.K")
        plt.xlabel("Temp (K)")
        plt.show()
    def integrate_TC(self, Tlow, Thigh):    
        lamb, _=quad(self.heatConductivity, Tlow, Thigh)
        return lamb
    def integrate_TC_low(self, Tlow, Thigh):  
        func=self.extrapolate_low_temp()  
        lamb, _=quad(func, Tlow, Thigh)
        return lamb

class BeCu():
    def __init__(self):
        #Valid 1-120 K
        self.thermal_conductivity={'a':-0.50015, 
                                   'b':1.93190, 
                                   'c':-1.69540, 
                                   'd':0.71218,
                                   'e':1.27880,
                                   'f':-1.61450,
                                   'g':0.68722,
                                   'h':-0.10501,
                                   'i':0.0}
                                   
    def heatConductivity(self, T):
        return 10**(self.thermal_conductivity['a']+self.thermal_conductivity['b']*(np.log10(T))+self.thermal_conductivity['c']*((np.log10(T))**2)
                +self.thermal_conductivity['d']*((np.log10(T))**3)+self.thermal_conductivity['e']*((np.log10(T))**4)
                +self.thermal_conductivity['f']*((np.log10(T))**5)+self.thermal_conductivity['g']*((np.log10(T))**6)
                +self.thermal_conductivity['h']*((np.log10(T))**7)+self.thermal_conductivity['i']*((np.log10(T))**8))
    def extrapolate_low_temp(self):
        T=np.linspace(1,120,2000)
        y=self.heatConductivity(T)
        T_low=T[:10]
        y_low=y[:10]
        func_lowtemp=interp1d(T_low, y_low, fill_value='extrapolate')
        return func_lowtemp
    def plot_Tcond(self):
        T=np.linspace(1,120,2000)
        y=self.heatConductivity(T)
        func_lowtemp=self.extrapolate_low_temp()
        T_low=np.linspace(0,1,100)
        y_low=func_lowtemp(T_low)
        plt.plot(T, y)
        plt.plot(T_low,y_low)
        plt.ylabel("Thermal Conductivity W/m.K")
        plt.xlabel("Temp (K)")
        plt.show()
    def integrate_TC(self, Tlow, Thigh):    
        lamb, _=quad(self.heatConductivity, Tlow, Thigh)
        return lamb
    def integrate_TC_low(self, Tlow, Thigh):  
        func=self.extrapolate_low_temp()  
        lamb, _=quad(func, Tlow, Thigh)
        return lamb


if __name__=='__main__':
    mat=BeCu()
    mat.plot_Tcond()



#TODO
#NIST have data to 4 k so, extrapolate down to 0K, fit that func, use that for the cold stages.






