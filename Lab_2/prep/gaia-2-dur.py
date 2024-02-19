import numpy as np

#Gaia-2-b
#RA: 110.73533
#Dec: 67.25266

r_planet = 1.327 * 0.102 *6.96e8 #meters
r_star = 1.064 * 6.96e8  #meters
sma = 0.0467 *1.5e11 #m

T = 3.69152 * 24 * 60 * 60


d = (2*r_planet) + (2*r_star) #m


v = (2*np.pi*sma)/T
#v = d/t ---> t = d/v




t = d/v

print(t/60/60)