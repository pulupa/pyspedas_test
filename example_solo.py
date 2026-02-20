import pyspedas.projects.solo as solo
from pyspedas import tplot, tplot_names, options

# example time with a Type III radio burst

trange = ['2021-10-28/15:00:00', '2021-10-28/18:00:00']

solo.rpw(trange=trange, time_clip=True, datatype='hfr-surv-flux', level = 'l3', prefix = 'solo_l3_rpw_hfr-surv-flux_')
solo.rpw(trange=trange, time_clip=True, datatype='tnr-surv-flux', level = 'l3', prefix = 'solo_l3_rpw_tnr-surv-flux_')

print(tplot_names())

options('solo_l3_rpw_hfr-surv-flux_PSD_SFU', 'ylog',1)
options('solo_l3_rpw_hfr-surv-flux_PSD_SFU', 'zlog',1)
options('solo_l3_rpw_tnr-surv-flux_PSD_SFU', 'ylog',1)
options('solo_l3_rpw_tnr-surv-flux_PSD_SFU', 'zlog',1)

tplot(['solo_l3_rpw_hfr-surv-flux_PSD_SFU', 'solo_l3_rpw_tnr-surv-flux_PSD_SFU'])