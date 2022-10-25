""" cfg.py """
from netpyne import specs

from params import lSet, cellParams

cfg = specs.SimConfig()

cfg.dt = 0.025
cfg.cvode_active = False
cfg.recordStims = False
cfg.recordStep = 0.05
cfg.duration = 100

mechs = cellParams['secs']['soma']['mechs']

#sodium channels
for mech in ['nattxs', 'nav1p8', 'nav1p9']:
    lSet(cfg, 'gbar_%s' %(mech), mechs[mech]['gbar'])

#potassium channels
for mech in ['kaslow', 'kdr', 'bkca', 'skca3', 'kmtype', 'knatype']:
    lSet(cfg, 'gbar_%s' %(mech), mechs[mech]['gbar'])

#passive, HCN
for mech in ['pas']:
    lSet(cfg, 'e_%s' %(mech), mechs[mech]['e'])

for mech in ['hcn']:
    lSet(cfg, 'gbarfast_%s' % (mech), mechs[mech]['gbarfast'])
    lSet(cfg, 'gbarslow_%s' % (mech), mechs[mech]['gbarslow'])

cfg.recordCells = ['all']

cfg.recordTraces["v_drg" ] = {'sec': 'soma', 'loc': 0.5, 'var': 'v'}

# for label, var in [ ['NaV1.7', 'ina_nattxs'], ['NaV1.8', 'ina_nav1p8'], ['KA', 'ik_kas'], ['KDR', 'ik_kdr'] ]:
#     cfg.recordTraces[label] = {'sec': 'cable', 'loc': 0.50, 'var': var}

# Saving
cfg.simLabel = 'sim'
cfg.saveFolder = 'data'
cfg.savePickle = True

# run simulation
cfg.hParams = {'celsius': 22, 'v_init': -53.5}

cfg.analysis.plotTraces = {'include': ['all'], 'overlay': True, 'oneFigPer': 'trace', 'saveData': True, 'saveFig': True,
                           'showFig': False} #, 'timeRange': [0, 145]}

#use the saveData to plot values
