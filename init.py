from netpyne import sim
from scipy import signal
import numpy as np

"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-o", "--output", default=None, help="output file for pkl dump of voltage trace")
args = vars(parser.parse_args())
"""
"""
# ---------------------------
# This will break the sim
# ---------------------------
from neuron import h
foo = h.Section(name='bar')
"""

cfg, netParams = sim.readCmdLineArgs()
sim.create(simConfig = cfg, netParams = netParams)

# store stims in object (otherwise will be gc if more than one)
stims = []

t = np.arange(0, cfg.duration, cfg.dt)
tv = sim.h.Vector(t)

# Choi
# Membrane potential was set by constant current injection
# (−13.74 pA for −70 mV, −7.24 pA for −65 mV, 9.55 pA for −55 mV, and 25.64 pA for −50 mV)

for cell in sim.net.cells:
    tags = cell.tags['cellType']
# create stimulus vector
    duty = cfg.width / cfg.isi
    stim = [ 0 ] * int(cfg.delay / cfg.dt)
    stim.extend( ( signal.square(2 * np.pi * t / cfg.isi, duty) == 1 ) * cfg.amp )
# play stimulus vector
    stimv = sim.h.Vector( stim )
    stims.append(stimv)
    stimv.play(cell.stims[0]['hObj']._ref_amp, tv)

sim.simulate() # calls runSim() and gatherData()
sim.analyze()

"""
output = args['output']
if output:
    print("dumping voltage trace to: %s" %(output))
    import pickle
    fptr = open(output, 'wb')
    vt = sim.simData['v_drg']['cell_0'].as_numpy()
    pickle.dump(vt, fptr)
    fptr.close()
"""