import numpy as np

#XO-2N

#RA: 117.02917
#Dec: 50.22583

r_planet = 0.973 * 0.102 *6.96e8 #meters
r_star = 0.964 * 6.96e8  #meters
sma = 0.0369 *1.5e11 #m

T = 2.61584 * 24 * 60 * 60

depth = (r_planet/r_star)**2
d = (2*r_planet) + (2*r_star) #m


v = (2*np.pi*sma)/T
#v = d/t ---> t = d/v




t = d/v

print(t/60/60)