'''Here are some function used to test the algorithm'''

from db_extractor import blob2list

# mean of the spectrum
def mean_spec(spec):

    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]

    return sum(absp)/len(absp)


# maximum value of the spectrum
def max_spec(spec):

    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]

    return max(absp)


# median of the spectrum
def med_spec(spec):
    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]
    absp.sort()

    return absp[len(absp)//2]