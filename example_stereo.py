import pyspedas.projects.stereo as stereo
from pyspedas import tplot_names, tplot, options, get_data

# example of a Type III radio burst

trange = ['2019-04-02/15:00', '2019-04-02/16:30']

stereo.waves(trange=trange, time_clip=True, datatype='hfr', probe = 'a', prefix = 'sta_swaves_hfr_')
stereo.waves(trange=trange, time_clip=True, datatype='lfr', probe = 'a', prefix = 'sta_swaves_lfr_')

print(tplot_names())

tplot('sta_swaves_?fr_PSD_FLUX')

