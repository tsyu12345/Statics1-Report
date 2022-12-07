from __future__ import annotations
from typing import Final as const

import pandas as pd


class Table:
    
    def __init__(self, excel_filename:str) -> None:
        
        self.filename: const[str] = excel_filename
        self.data_frame: const[pd.DataFrame] = pd.read_excel(self.filename)
    
if __name__ == '__main__':
    Table('data.xlsx')    
