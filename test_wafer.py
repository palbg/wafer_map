import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from db_extractor import db_extrac, blob2list
from detect_peaks_gmrf import detect_peaks_valleys_gmrf


for k in range(10):
    wafer_ID = 'G1_1_14_12'+str(k)
    print(wafer_ID)

    db_path = 'sqlite:///C:\\Users\\cphnano\\paul lebaigue\\production_data\\db\\database.db'
    wafer_extracted = db_extrac(db_path, wafer_ID)
    spec_wlen = blob2list(wafer_extracted[2][0][0])
    spec = spec_wlen[1:len(spec_wlen):2]
    wlen = spec_wlen[0:-1:2]

    detect_peaks_valleys_gmrf(spec)
#plt.plot(wlen,spec)
#plt.show()
