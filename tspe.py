from netpyne import specs
from netpyne.batch import Batch

import numpy as np
import pandas as pd
import itertools

# target values

def batchOptuna():
    params = specs.ODict()
    params['gbar_kaslow' ] = [1e-4, 1e-1 ]  # 0.00136 # min, max - no starting - it handles its own sampling
    params['gbar_kdr'    ] = [1e-5, 1e-1 ]  # 0.002688
    params['gbar_kmtype' ] = [1e-5, 1e-2 ]  # 0.0001
    params['gbar_knatype'] = [1e-6, 1e-3 ]  # 1e-5

    params['e_pas'       ] = [-70 , -40  ]  # -41.583
    params['gbarfast_hcn'] = [1e-7, 1e-3 ]  # 1.32e-5
    params['gbarslow_hcn'] = [1e-8, 1e-4 ]  # 6.7615e-6
    fitnessFuncArgs = {'foo': 'bar'}

    def fitnessEq( data ):


        t = data['t']
        v = data['v_drg']['cell_0']
        ddf = {}
        ddf['t'] = np.array(t)[1:]  # need to strip initial value (to work with dataframe)
        ddf['v'] = np.array(v)[1:]
        # parsed dataframe
        ddf['dv'] = np.diff(v)
        ddf['dt'] = np.diff(t)
        ddf['dvdt'] = ddf['dv'] / ddf['dt']
        pdf = pd.DataFrame(ddf)
        dFts = genFts(pdf)
        fitness = 0
        fitness += np.abs(tFts['trMax'] - dFts['trMax'])
        fitness += np.abs(tFts['trMin'] - dFts['trMin'])
        fitness += np.abs(tFts['trWdth'] - dFts['trWdth'])
        return fitness, dFts['trMax'], dFts['trMin'], dFts['trWdth']

    def fitnessFunc(simData, **kwargs):
        import numpy as np
        foo = kwargs['foo']
        fitness, trMax, trMin, trWdth = fitnessEq(simData)
        popInfo = '; Max:%s Min:%s Width:%s Fitness:%s' %(trMax, trMin, trWdth, fitness)
        print('  '+popInfo)
        return fitness

    b = Batch(params = params, cfgFile = 'cfg.py', netParamsFile = 'netParams.py')

    # Set output folder, grid method (all param combinations), and run configuration
    b.batchLabel = 'simple'
    b.saveFolder = './'+b.batchLabel
    b.method = 'optuna'
    b.runCfg = {
        'type': 'mpi_direct',
        'script': 'init.py',
        'mpiCommand': 'mpiexec',
        'nodes': 1,
        'coresPerNode': 1,
    }
    b.optimCfg = {
        'fitnessFunc': fitnessFunc, # fitness expression (should read simData)
        'fitnessFuncArgs': fitnessFuncArgs,
        'maxFitness': 1000,
        'maxiters':     500,    #    Maximum number of iterations (1 iteration = 1 function evaluation)
        'maxtime':      3600 * 6,    #    Maximum time allowed, in seconds
        'maxiter_wait': 360,
        'time_sleep': 5,
        #'popsize': 1  # unused - run with mpi
    }

    # Run batch simulations
    b.run()

if __name__ == '__main__':
    batchOptuna()