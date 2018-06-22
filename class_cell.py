'''definition of a class cell, containing the location and the value of the cells'''

from db_extractor import blob2list

class wafer:

    cell_list = []

    def __init__(self):
        self.x = []
        self.y = []
        self.value = []
        self.cell_list.append(self)


    def add_cell(self, x, y, spec, spec_analyser):
        #print(blob2list(spec))
        if blob2list(spec)!= None and x!=None and y!=None:
            self.x.append(x)
            self.y.append(y)
            self.value.append(spec_analyser(spec))


    def amplitude(self):
        M = max(p for p in self.value)
        m = min(p for p in self.value)
        ampli = (M-m)/1.9999
        midl = (M+m)/2
        return(ampli,midl,M,m)


"""
w1 = wafer()
w1.add_cell(('x1','y1'))
w1.add_cell(('x2','y2'))
w1.add_cell(('x3','y3'))

for c in w1.cell_list:
    for i in range(len(c.x)):
        if c.x[i] == 'x2':
            print(c.y[i])"""