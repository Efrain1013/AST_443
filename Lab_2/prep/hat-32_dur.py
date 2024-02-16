import numpy as np

#RA: 31.04176
#Dec: 46.68778

#hat-p-32-b

r_planet = 1.789 * 0.102 *6.96e8 #meters
r_star = 1.387 * 6.96e8  #meters
G = 6.67e-11
sma = 0.03427 *1.5e11 #m
T = 2.15 * 24 * 60 * 60

M_star = 1.176 * 1.99e30    #kg
M_planet = 0.75 * 1.9e27   #kg
M = M_star + M_planet

d = (2*r_planet) + (2*r_star) #m

v_theory = np.sqrt((G*M)/sma) #m/s

v = (2*np.pi*sma)/T
#v = d/t ---> t = d/v



t_theory = d/v_theory

t = d/v

print(t_theory/60/60)
print(t/60/60)