import posregi1
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

minipos = posregi1.PosRegi('master.csv')

minipos.accept_order()