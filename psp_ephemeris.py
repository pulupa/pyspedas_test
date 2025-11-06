
import numpy as np
import cdflib as cdf
import astropy.coordinates as apc
import astropy.units as apu
import astropy.time as apt

''''

How to run at IPython terminal:
-------------------------------


import psp as psp

l2_file = '/home/user/psp_fld_l2_rfs_hfr_20240129_v03.cdf'
l3_file = '/home/user/psp_fld_l3_rfs_hfr_20240129_v03.cdf'

out = psp.load_psp_data(l2_file, l3_file)

HAE_sun_t = out['HAE_sun_t']
etc...


'''










def compute_stokes(auto_V1V2, auto_V3V4, cross_re, cross_im):
    I = auto_V1V2 + auto_V3V4
    Q = auto_V1V2 - auto_V3V4
    U = 2 * cross_re
    V = 2 * cross_im
    return I, Q, U, V
    


def HAE_sun_mercury_venus(t_array):
    '''    
    t_array   = dt.datetime(2024,1,1,10,10,10)
       
    '''
    t_astropy = apt.Time(t_array, format='datetime64', scale='utc')
    coords_HTE_cart_all = {}
    
    for body in ['sun', 'mercury', 'venus']:
    
        coords_GCRS = apc.get_body(body, t_astropy)
        #
        # Using "HeliocentricMeanEcliptic" from Astropy following the definition in "stereo_spice.pdf":
        # 
        # "HAE: Heliocentric Aries Ecliptic. X is in the direction of the first point of Aries, and Z is the ecliptic North Pole. This can be realized with either the J2000 ecliptic (default), or the ecliptic of date"
        #
        # According to the above, the "default" seems to be constant and from J2000. For this reason, below we use "HeliocentricMeanEcliptic".
        #
        # If, instead, the data used "the ecliptic of date", then we should use "HeliocentricTrueEcliptic" from Astropy.
        # 
        
        coords_HTE  = coords_GCRS.transform_to(apc.HeliocentricMeanEcliptic)
        
        x = coords_HTE.cartesian.x.to(apu.km).value
        y = coords_HTE.cartesian.y.to(apu.km).value
        z = coords_HTE.cartesian.z.to(apu.km).value
        
        xyzT = np.array([x,y,z])
        coords_HTE_cart = xyzT.T
        coords_HTE_cart_all[body] = coords_HTE_cart
        
    return coords_HTE_cart_all['sun'], coords_HTE_cart_all['mercury'], coords_HTE_cart_all['venus']



def load_psp_data(l2_file, l3_file):
    '''
    https://research.ssl.berkeley.edu/data/psp/data/sci/fields/
    
    Example of level 2 file:
    l2_file = '/home/user/psp_fld_l2_rfs_hfr_20240129_v03.cdf'
    
    Corresponding level 3 file:
    l3_file = '/home/user/psp_fld_l3_rfs_hfr_20240129_v03.cdf' 
    
    '''
    
    # Objects containing the variable names and data from the L2 and L3 files
    # -----------------------------------------------------------------------
    cdf_l2 = cdf.CDF(l2_file)
    cdf_l3 = cdf.CDF(l3_file)
    
    

    # Variable names
    # --------------
    autov12_var = "psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2"
    autov34_var = "psp_fld_l2_rfs_hfr_auto_averages_ch1_V3V4"
    crossv12v34_re_var = "psp_fld_l2_rfs_hfr_cross_re_V1V2_V3V4"
    crossv12v34_im_var = "psp_fld_l2_rfs_hfr_cross_im_V1V2_V3V4"
    
    freq_var  = "frequency_hfr_auto_averages_ch0_V1V2"
    epoch_var = "epoch_hfr_auto_averages_ch0_V1V2"
    j2000_var = "psp_fld_l3_rfs_hfr_ch0_V1V2_J2000"

    temp_epoch_var = "epoch_hfr_temperature"
    temp1234_var = [
        "psp_fld_l3_rfs_hfr_temperature_PA1",
        "psp_fld_l3_rfs_hfr_temperature_PA2",
        "psp_fld_l3_rfs_hfr_temperature_PA3",
        "psp_fld_l3_rfs_hfr_temperature_PA4",
    ]

    pos_epoch_var = "epoch_hfr_position"
    pos_HAE_var   = "psp_fld_l3_rfs_hfr_position_HAE"
    
    
    
    
    

    # Loading data
    # ------------
    
    # Radio data
    autov12 = np.array(cdf_l2.varget(autov12_var))
    autov34 = np.array(cdf_l2.varget(autov34_var))
    crossv12v34_re = np.array(cdf_l2.varget(crossv12v34_re_var))
    crossv12v34_im = np.array(cdf_l2.varget(crossv12v34_im_var))
    
    # Frequency and time
    f     = np.array(cdf_l2.varget(freq_var))
    epoch = np.array(cdf_l2.varget(epoch_var))
    
    # ICRS coordinates of V1 antenna
    j2000 = np.array(cdf_l3.varget(j2000_var))

    # Temperatures
    temp       = np.stack([np.array(cdf_l3.varget(v)) for v in temp1234_var], axis=-1)
    temp_epoch = np.array(cdf_l3.varget(temp_epoch_var))

    # PSP HAE coordinates
    HAE_psp       = np.array(cdf_l3.varget(pos_HAE_var))  # PSP coordinates in HAE frame
    HAE_psp_epoch = np.array(cdf_l3.varget(pos_epoch_var))
   





    # Computations
    # ------------

    # Stokes parameters
    I, Q, U, V = compute_stokes(autov12, autov34, crossv12v34_re, crossv12v34_im)


    # Conversion of time to datetime64
    t         = cdf.cdfepoch.to_datetime(epoch)
    temp_t    = cdf.cdfepoch.to_datetime(temp_epoch)
    HAE_psp_t = cdf.cdfepoch.to_datetime(HAE_psp_epoch)


    # HAE coordinates for the Sun, Mercury, and Venus 
    HAE_sun, HAE_mercury, HAE_venus = HAE_sun_mercury_venus(t)


    # Galactic coordinates for V1 antenna
    coords = apc.SkyCoord(j2000[:, 0] * apu.deg, j2000[:, 1] * apu.deg, frame='icrs', equinox='J2000')
    l = coords.galactic.l.deg
    b = coords.galactic.b.deg
    galactic_V1_T = np.array([l,b])
    galactic_V1 = galactic_V1_T.T





          
    # Output
    # ------
    out = {
            # Stokes parameters
            "I": I,
            "Q": Q,
            "U": U,
            "V": V,
            "t": t,
            "f": f,
            
            # Temperature
            "temp":   temp,          
            "temp_t": temp_t,

            # V1 galactic coordinates
            "galactic_V1":   galactic_V1,
            "galactic_V1_t": t,
    
            # PSP HAE coordinates
            "HAE_psp":   HAE_psp,
            "HAE_psp_t": HAE_psp_t,
    
            # Sun HAE coordinates
            "HAE_sun":   HAE_sun,
            "HAE_sun_t": t,
    
            # Mercury HAE coordinates
            "HAE_mercury":   HAE_mercury,
            "HAE_mercury_t": t,
    
            # Venus HAE coordinates
            "HAE_venus":   HAE_venus,
            "HAE_venus_t": t,
            
        }    
        
        
    return out



