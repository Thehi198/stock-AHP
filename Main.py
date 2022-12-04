# import numpy as np 
# import pandas as pd

coreParameters = ['management', 'cashflow', 'forcast', 'brand']

coreParametersRank = [1, 2, 3, 4]

comparisonMatrix = {
    'management': [coreParametersRank[0], coreParametersRank[0]/coreParametersRank[1], coreParametersRank[0]/coreParametersRank[2], coreParametersRank[0]/coreParametersRank[3]],
    'cashflow': [coreParametersRank[1], coreParametersRank[1]/coreParametersRank[0], coreParametersRank[1]/coreParametersRank[2], coreParametersRank[1]/coreParametersRank[3]],
    'forcast': [coreParametersRank[2], coreParametersRank[2]/coreParametersRank[1], coreParametersRank[2]/coreParametersRank[2], coreParametersRank[2]/coreParametersRank[3]],
    'brand': [coreParametersRank[3], coreParametersRank[3]/coreParametersRank[1], coreParametersRank[3]/coreParametersRank[2], coreParametersRank[3]/coreParametersRank[3]]
}


#print(comparisonMatrix)
for i in comparisonMatrix:
    print(f'{i}: {comparisonMatrix[i]}')