'''Here are some function used to test the algorithm'''

from db_extractor import blob2list
import numpy as np

# mean of the spectrum
def mean_spec(wlen, spec):
    return sum(spec)/len(spec)


# maximum value of the spectrum
def max_spec(wlen, spec):
    return max(spec)


# median of the spectrum
def med_spec(wlen, spec):
    spec.sort()
    return spec[len(spec)//2]


# standard deviation
def std_dev(wlen, spec):

    # list of the corresponding absorption
    absp = np.array(spec)
    absp2 = absp*absp
    mean2 = sum(absp2) / len(absp2)

    mean = mean_spec(spec,wlen)

    var = float(mean2) - float(mean**2)

    return np.sqrt(var)



