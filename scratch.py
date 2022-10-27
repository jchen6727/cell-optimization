from netpyne import sim
import numpy as np
from cfg import cfg
from netParams import netParams

sim.h.load_file('tautables.hoc')

sim.create(simConfig = cfg, netParams = netParams)

sim.simulate()

svt = sim.simData['cell_0']
