import numpy as np

#hat-p-22-b
#RA: 155.68333
#Dec: 50.12833

r_planet = 1.08 * 0.102 *6.96e8 #meters
r_star = 1.04 * 6.96e8  #meters
G = 6.67e-11
sma = 0.0414 *1.5e11 #m

T = 3.2122 * 24 * 60 * 60

M_star = 0.916 * 1.99e30    #kg
M_planet = 2.147 * 1.9e27   #kg
M = M_star + M_planet

d = (2*r_planet) + (2*r_star) #m

v_theory = np.sqrt((G*M)/sma) #m/s

v = (2*np.pi*sma)/T
#v = d/t ---> t = d/v



t_theory = d/v_theory

t = d/v

print(t_theory/60/60)
print(t/60/60)