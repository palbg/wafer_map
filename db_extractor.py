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