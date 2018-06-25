'''definition of a class wafer, containing the location and the value of the cells'''

from db_extractor import blob2list

class wafer:

    cell_list = []

    def __init__(self):
        self.x = []
        self.y = []
        self.value = []
        self.cell_list.append(self)


    def add_cell(self, x, y, spec, spec_analyser):

        if blob2list(spec)!= None and x!=None and y!=None:
            self.x.append(x)
            self.y.append(y)
            self.value.append(spec_analyser(spec))


    def amplitude(self):
        M = max(p for p in self.value)
        m = min(p for p in self.value)
        # python doesn't round well
        ampli = (M-m)/1.9999
        midl = (M+m)/2
        return(ampli,midl,M,m)

