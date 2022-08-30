import pygsheets
from utils.parameters import Pars
import aranet4 as a4
import panel as pn
import pandas as pd
import param
import time
import re




class CarbonPanel(Pars):
    in_mac = pn.widget.from_param()
    def __init__(self,**params):
        


    @classmethod
    @param.depends('cell', on_init=True, watch=True)
    def _encode(self):
        _row = re.split('[A-Z]{1,2}', self.cell)
        _col = [ord(i)-64 for i in list(self.cell)[:len(_row)]]
        _col = (25 * _col[0] + _col[1])
        return (int(_col), int(_row))

    @staticmethod
    @param.depends('mac_address', on_init=True, watch=True)
    def readings(self):
        self.current = a4.get_current_readings(mac_address=self.mac_address)
        all_read = a4.get_all_readings(mac_address=self.mac_address, 
            entry_filter=self.ENTRY_FIL)
        df = pd.DataFrame(all_read)
        gc = pygsheets.authorize()
        sh = gc.open(self.sheet)[0]

        # (0,0) relates to A,1
        sh.set_dataframe(df, (self.col, self.row))    
