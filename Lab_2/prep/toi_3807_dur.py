import numpy as np

#TOI-3807-b

#RA: 139.1125
#Dec: 69.07417

r_planet = 2. * 0.102 *6.96e8 #meters
r_star = 1.468 * 6.96e8  #meters
sma = 0.0421 *1.5e11 #m

T = 2.89897 * 24 * 60 * 60

depth = (r_planet/r_star)**2
d = (2*r_planet) + (2*r_star) #m


v = (2*np.pi*sma)/T
#v = d/t ---> t = d/v




t = d/v

print(t/60/60)