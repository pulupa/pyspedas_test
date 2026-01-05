import pyspedas.projects.wind as wind
from pyspedas import tplot, tplot_names

# example time with a Type III radio burst

trange = ['2019-04-02/15:00', '2019-04-02/16:30']

# example of Wind 'qtnfit' data

trange = ['2005-01-01/00:00', '2005-01-02/00:00']

wind.waves(trange=trange, time_clip=True, datatype='rad2')
wind.waves(trange=trange, time_clip=True, datatype='rad1')
wind.waves(trange=trange, time_clip=True, datatype='tnr')

wind.waves(trange=trange, time_clip=True, datatype='qtnfit')
wind.waves(trange=trange, time_clip=True, datatype='qtnfit-filtered')

print(tplot_names())

tplot(['wi_l2_wav_rad?_PSD_V2_Z','wi_l2_wav_tnr_PSD_V2',
       'wi_l2_wav_qtnfit_fit_n_e','wi_l2_wav_qtnfit-filtered_fit_n_e'])
