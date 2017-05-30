from astropy.io import ascii
import numpy as np

def read_swasp_cleaned():
    t_wasp = ascii.read('PDS110WASPlc.txt')

    #time_yrs,time_jd,rel_flux,wasp_flux,wasp_mag,rel_flux_err,wasp_flux_err,wasp_mag_err
    #    1        2       3         4        5          6             7     8

    # convert to modified HJD and magnitude
    TAMFLUX2 = t_wasp['col4']
    TAMFLUX2_ERR = t_wasp['col6']
    TAMMAG2 = t_wasp['col5']
    TAMMAG2_ERR = t_wasp['col8']
    MHJD = t_wasp['col2']  - 2450000.0
    return(MHJD, TAMMAG2, TAMMAG2_ERR, TAMFLUX2, TAMFLUX2_ERR)

def read_swasp():
    t_wasp = ascii.read('J0523_Wasp_tab.txt')

    # convert to modified HJD and magnitude
    TAMFLUX2 = t_wasp['col20']
    TAMFLUX2_ERR = t_wasp['col21']
    TAMMAG2 = 15. - 2.5 * np.log10(TAMFLUX2)
    TAMMAG2_ERR = 15. - 2.5 * np.log10(TAMFLUX2_ERR)
    MHJD = t_wasp['col1']
    CAMID = t_wasp['col19']
    return(MHJD, TAMMAG2, TAMMAG2_ERR, TAMFLUX2, TAMFLUX2_ERR, CAMID.astype(int))

def read_swasp_binned_cleaned():
    t_wasp = ascii.read('PDS110WASPlc_bin.dat')

    # convert to modified HJD and magnitude
    return(t_wasp['time'], t_wasp['flux'], t_wasp['flux_rms'])

def read_swasp_binned():
    t_wasp = ascii.read('j0523_bin.cc.dat')

    # convert to modified HJD and magnitude
    return(t_wasp['time'], t_wasp['flux'], t_wasp['flux_rms'])


def read_kelt():
    t_kelt = ascii.read('J0523_KELT.txt')

    # convert to modified HJD and magnitude
    MHJD = t_kelt['col1'] - 2450000.0
    KELTMAG = t_kelt['col2']
    KELTMAGERR = t_kelt['col3']

    return(MHJD, KELTMAG, KELTMAGERR)

def read_asassn():
    t_asassn = ascii.read('PDS110_ASASSN_good_Fix.dat')

    # convert to modified HJD and magnitude
    MHJD = t_asassn['JD'] - 2450000.0
    ASASMAG = t_asassn['Limit']
    ASASMAGERR = t_asassn['mag']

    return(MHJD, ASASMAG, ASASMAGERR)

def read_asas():
    t_asas = ascii.read('ASAS052331dat.txt')

    # convert to modified HJD and magnitude
    MHJD = t_asas['col1']
    ASASMAG = t_asas['col3']
    ASASMAGERR = t_asas['col8']

    return(MHJD, ASASMAG, ASASMAGERR)

