
import h5py
import numpy as np
import matplotlib.pyplot as plt

from os import environ 

file = '/Users/' + environ.get('USER') + \
  '/Desktop/40_T2_03MHz_Q150709_215542_ch1_d_008.h5'

f = h5py.File(file, 'r')
list(f.keys())

time_series = np.array(f['ch1'])

plt.plot(time_series[0:10000])

plt.show()