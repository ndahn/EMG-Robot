import numpy as np


# TODO T-values
myop_T = 0.5
wamp_T = 0.5
ialv_T = 1.0   # to avoid log of negative values


def diff(win):
    return win.diff(axis=0, periods=-1)


def f_iemg(win):
    '''integrated EMG'''
    return np.abs(win).sum(axis=0)

def f_mav(win):
    '''mean absolute value'''
    return f_iemg(win) / win.shape[0]

def f_ssi(win):
    '''simple square integrated'''
    return np.power(win, 2).sum(axis=0)

def f_rms(win):
    '''root mean square'''
    return np.sqrt(f_ssi(win) / win.shape[0])

def f_var(win):
    '''variance'''
    return win.var(axis=0)

def f_myop(win):
    '''myopulse percentage rate'''
    myop = np.abs(win)
    myop = np.where(myop > myop_T, 1, 0)
    return myop.sum(axis=0) / win.shape[0]

def f_wl(win):
    '''waveform length'''
    return np.abs(diff(win)).sum(axis=0)

def f_damv(win):
    '''difference absolute mean value'''
    return np.abs(diff(win)).sum(axis=0) / (win.shape[0] - 1)

def f_m2(win):
    '''second order moment'''
    return np.power(diff(win), 2).sum(axis=0)

def f_dvarv(win):
    '''difference variance version'''
    return f_m2(win) / (win.shape[0] - 2)

def f_dasdv(win):
    '''difference absolute standard deviation value'''
    return np.sqrt(f_m2(win) / (win.shape[0] - 1))

def f_max(win):
    '''mxaimum'''
    return win.max(axis=0)

def f_min(win):
    '''minimum'''
    return win.min(axis=0)

def f_wamp(win):
    '''willison amplitude'''
    wamp = np.abs(diff(win))
    wamp = np.where(wamp > wamp_T, 1, 0)
    return wamp.sum(axis=0)

def f_iasd(win):
    '''integrated absolute of second derivative'''
    x1 = diff(diff(win))
    return np.abs(x1).sum(axis=0)

def f_iatd(win):
    '''integrated absolute of third derivative'''
    x2 = diff(diff(diff(win)))
    return np.abs(x2).sum(axis=0)

def f_ieav(win):
    '''integrated exponential of absolute values'''
    return np.exp(np.abs(win)).sum(axis=0)

def f_ialv(win):
    '''integrated absolute log values'''
    return np.abs(np.log(win + ialv_T)).sum(axis=0)

def f_ie(win):
    '''integrated exponential'''
    return np.exp(win).sum(axis=0)


all_features = [
#    f_iemg,  # redundant with mav
    f_mav,
#    f_ssi,   # redundant with rms
    f_rms,
    f_var,
    f_myop,
#    f_wl,    # redundant with damv
    f_damv,
#    f_m2,    # somewhat redundant with damv
#    f_dvarv, # redundant with m2
    f_dasdv,  # somewhat redundant with dvarv (keep for now)
    f_max,
    f_min,
    f_wamp,   # like myop, but on differences
    f_iasd,
    f_iatd,
    f_ieav,
#    f_ialv,  # causes nan/inf for negative coefficients when ialv_T is not right
    f_ie,     # somewhat redundant with ieav (keep for now)
]
