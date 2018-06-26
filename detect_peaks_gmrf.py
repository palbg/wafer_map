"""
Detect peaks for GMRF nanocuvette spectra.

Code by emiho.

2018-06-16 emiho

"""


import numpy as np
import matplotlib.pyplot as plt
from _modules.detect_peaks import *


def detect_peaks_valleys_gmrf(spectrum):

    idx_p = detect_peaks(spectrum, mph=0.2, mpd=5, threshold=0.0001, edge=None)
    idx_v = detect_peaks(spectrum, valley=True, mpd=15, mph=-0.4,threshold=0.0001, edge=None, show=True, kpsh=True)

    idx = idx_p
    for idx_temp in idx_v:
        if idx_p[-1] > idx_temp > idx_p[0]:
            idx = np.append(idx, idx_temp)

    idx = np.append(idx, 0)
    idx = np.append(idx, np.size(spectrum)-1)
    idx = np.sort(idx)

    return idx

def detect_needed_valley(spectrum):
    valleys = detect_peaks(spectrum, valley=True, mpd=15, mph=-0.4, threshold=0.0001, edge=None,
                           #show=True,
                           kpsh=True
                           )

    wlen_list = []
    for v in valleys :
        if 520 < v < 532:
            wlen_list.append(v + 200)

    if wlen_list == []:
        return None

    wlen_list.sort()
    return wlen_list[0]
