import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import matplotlib.style as style

# Load data skipping the header row
data = np.loadtxt('section_4_5.csv', skiprows=1, delimiter=',')

i = 255

date_obs = data[:,0]
flux = data[:,1]
flux_err = data[:,2]
normalized_flux = data[:,3]
r = data[:,4]
r_err = data[:,5]
kep_norm = data[:,6]
kep_err = data[:,7]

transit_time_jd = 2460220.6600800115 # mid-transit JD

# Convert JD to hours since transit
hours_since_transit = (date_obs - transit_time_jd) * 24  # 1 JD = 24 hours

a = 87
b = 175

style.use('bmh')

plt.figure(figsize=(10, 6))

plt.errorbar(hours_since_transit[:a], kep_norm[:a], yerr=kep_err[:a], fmt='o', capsize=2)
plt.errorbar(hours_since_transit[a:b], kep_norm[a:b], yerr=kep_err[a:b], fmt='o', capsize=2)
plt.errorbar(hours_since_transit[b:i], kep_norm[b:i], yerr=kep_err[b:i], fmt='o', capsize=2,color='tab:blue')

#plt.vlines(x = hours_since_transit[129], ymin = .93, ymax = 1.06,color='red')
plt.title('Exoplanet Transit of TrES-2b')
plt.xlabel('Hours Since Mid-Transit')
plt.ylabel('Normalized Flux')

plt.tight_layout()
#plt.show()
plt.savefig('tres2b.png')
