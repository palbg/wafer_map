'''Taking ID of the wafer and the spectrum analyser function (for example a function which get a spectrum and
returns the thickness of a cell) this function draw a wafer map'''

from class_cell import *
from db_extractor import db_extrac
from draw_map import draw
from func_test_spec import mean_spec, max_spec, med_spec


def color_wafer(wafer_ID,spec_analyser):

    # initialize the wafer class corresponding to the ID
    Wafer = wafer()

    # takes data from the sqlite database
    db_path = 'sqlite:///C:\\Users\\cphnano\\paul lebaigue\\production_data\\db\\database.db'
    wafer_extracted = db_extrac(db_path,wafer_ID)

    x_cell_extracted = wafer_extracted[0]
    y_cell_extracted = wafer_extracted[1]
    spec_cell_extracted = wafer_extracted[2]

    for k in range(len(x_cell_extracted)):

        Wafer.add_cell(x_cell_extracted[k][0],
                       y_cell_extracted[k][0],
                       spec_cell_extracted[k][0],
                       spec_analyser)

    draw(Wafer)


color_wafer('G1_1_14_',med_spec)