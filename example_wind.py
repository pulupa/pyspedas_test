import pyspedas.projects.wind as wind
from pyspedas import tplot, tnames

# example of a Type III radio burst

trange = ['2019-04-02/15:00', '2019-04-02/16:30']

wind.waves(trange=trange, time_clip=True, datatype='rad2')
wind.waves(trange=trange, time_clip=True, datatype='rad1')

print(tnames('*'))

tplot('wi_l2_wav_rad?_PSD_V2_Z')
