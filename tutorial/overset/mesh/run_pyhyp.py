from pyhyp import pyHyp, pyHypMulti



commonOptions= {

    # ---------------------------
    #        Input Parameters
    # ---------------------------
    # 'inputFile':fileName,
    'fileType': 'CGNS',
    'unattachedEdgesAreSymmetry':False,
    'outerFaceBC':'overset',
    'autoConnect':True,
    'BC':{},
    'families':'wall',

    # ---------------------------
    #        Grid Parameters
    # ---------------------------
    'N': 89, 
    's0': 1e-6,
    'marchDist':2.5*0.8,
    'splay':0.25,
    # ---------------------------
    #   Pseudo Grid Parameters
    # ---------------------------
    'ps0': -1,
    'pGridRatio': -1,
    'cMax': 5,

    # ---------------------------
    #   Smoothing parameters
    # ---------------------------
    # 'epsE': 1.0,
    # 'epsI': 2.0,
    # 'theta': 3.0,
    'epsE': 1.0,
    'epsI': 2.0,
    'theta': 1.0,
    'volCoef': 0.5,
    'volBlend': 0.0001,
    'volSmoothIter': 100,
    
    # -------------------------------
    #   Solution Parameters (Common)
    # -------------------------------
    'kspMaxIts': 1500,
}

# Now set up specific options
from collections import OrderedDict
options = OrderedDict()

options['wing'] = {
                'inputFile': 'wing.cgns',
                'outputFile':'wing_hyp.cgns',
                'BC':{
                    5:{'jLow':'ySymm'},
                    6:{'jLow':'ySymm'},
                    11:{'jLow':'ySymm'}
                }
            }

options['tip'] = {
                'inputFile': 'tip.cgns',
                'outputFile':'tip_hyp.cgns'
            }

options['far'] = 'far_bc.cgns'


hyp = pyHypMulti(options=options,commonOptions=commonOptions)
hyp.combineCGNS('wing_final.cgns', eraseFiles=False)
