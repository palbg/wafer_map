'''This function take the ID of a wafer and extract the imprint coordinates and
the spectrums of each cuvette in the considered wafer'''

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import numpy as np

# import from another file
import sys
sys.path.append("C:\\Users\\cphnano\\paul lebaigue\\production_data")
from cuvette_db_declarative import Base, Cuvette

db_path = 'sqlite:///C:\\Users\\cphnano\\paul lebaigue\\production_data\\db\\database.db'
wafer_ID = 'G1_1_14'

def db_extrac(db_path,wafer_ID):
    engine = create_engine(db_path)

    # enable the access for DBSession
    Base.metadata.bind = engine

    # Create a conversation with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # querying the database
    x = session.query(Cuvette.impr_x).filter(Cuvette.int_id.contains(wafer_ID)).all()
    y = session.query(Cuvette.impr_y).filter(Cuvette.int_id.contains(wafer_ID)).all()
    spec = session.query(Cuvette.spectrum_air_ri1).filter(Cuvette.int_id.contains(wafer_ID)).all()
    wafer = x,y,spec

    session.commit()
    session.close()

    return(x,y,spec)



def blob2list(blob):
    if blob is None or blob==0:
        return None

    return np.fromstring(blob).tolist()



#wafer = db_extrac(db_path,'G1_1_14_195')



'''
x_cell_extracted = wafer[0]
y_cell_extracted = wafer[1]
spec_cell_extracted = wafer[2]
for k in range(len(x_cell_extracted)):
    print(x_cell_extracted[k][0],y_cell_extracted[k][0])'''

#print(wafer)
# print(np.fromstring(wafer[2][5][0]).tolist())
#print(blob2list(wafer[2][0][0]))