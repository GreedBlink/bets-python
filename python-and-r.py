import rpy2.robjects as ro
import pandas as pd
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

# Obtendo a Produção industrial (2002=100) - Rio de Janeiro

bets = importr("BETS")
dados = bets.BETSget(code=11081, data_frame=True)


with localconverter(ro.default_converter + pandas2ri.converter):
    pim_rj = ro.conversion.rpy2py(dados)

print(pim_rj)