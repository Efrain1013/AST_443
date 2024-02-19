import numpy as np 
from astropy.time import Time

#XO_2N_b: T = 2.61584, JD = 2.454148e6
#TOI-3807-b: T = 2.89897, JD = 2.459218e6
#Gaia_2_b: T = 3.69152, JD = 2.458844e6


transit = 0
T =  # enter period
JD =  #enter Julian date of mid-transit observation

file_name=input(print('Enter file name'))

observed = Time(JD, format='jd')

with open(file_name, 'w') as file:
    for N in range(0, 3300):
        transit = observed + N * T
        file.write(str(Time(transit,format='datetime')) + '\n')

        
