import numpy as np

from db_extractor import blob2list

def sum_spec(spec):

    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]

    return sum(absp)/len(absp)




def max_spec(spec):

    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]

    return max(absp)


def med_spec(spec):
    spec_extracted = blob2list(spec)

    # list of the wavelength
    wlen = spec_extracted[0:-1:2]

    # list of the corresponding absorption
    absp = spec_extracted[1:len(spec_extracted):2]
    absp.sort()

    return absp[len(absp)//2]


#db_path = 'sqlite:///C:\\Users\\cphnano\\paul lebaigue\\production_data\\db\\database.db'
#spec = db_extrac(db_path,'G1_1_14_127')

#print(sum_spec(spec))