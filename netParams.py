from netpyne import specs
try:
    from __main__ import cfg
except:
    from cfg import cfg

from params import lSet, lGet, cellParams
# NetParams object to store network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

lbl = "mm"

params = {}

# can store  cfg params in cellType
cellType = {'model': "%s" % (lbl)}
cellLbl = str(cellType)

param = cellParams

"""
All the mechanisms used in the cell
for mech in ['CaL', 'CaN', 'CaPQ', 'CaR', 'CaT', 'bkca', 'cacc', 'cadyn', 'hcn', 'ip3dif', 'kaslow', 'kdr', 'kmtype',
             'knatype', 'nakpump', 'nav1p7', 'nav1p8', 'nav1p9', 'ncxsoma', 'pas', 'skca3', 'soce', 'trpm8']:
"""

mechs = param['secs']['soma']['mechs']

# sodium channels
for mech in ['nattxs', 'nav1p8', 'nav1p9']:
    ig = mechs[mech]['gbar']                # initial g
    ng = getattr(cfg, 'gbar_%s' %(mech))    # new g
    mechs[mech]['gbar'] = ng                #

# potassium channels
for mech in ['kaslow', 'kdr', 'bkca', 'skca3', 'kmtype', 'knatype']:
    ig = mechs[mech]['gbar']                # initial g
    ng = getattr(cfg, 'gbar_%s' %(mech))    # new g
    mechs[mech]['gbar'] = ng                #


# passive channel
for mech in ['pas']:
    ie = mechs[mech]['e']                # initial e
    ne = getattr(cfg, 'e_%s' %(mech))    # new e
    mechs[mech]['e'] = ne

# HCN channel
for mech in ['hcn']:
    ig = mechs[mech]['gbarfast']                # initial g
    ng = getattr(cfg, 'gbarfast_%s' %(mech))    # new g
    mechs[mech]['gbarfast'] = ng

    ig = mechs[mech]['gbarslow']  # initial g
    ng = getattr(cfg, 'gbarslow_%s' % (mech))  # new g
    mechs[mech]['gbarslow'] = ng





# can change cellType
# param['conds']['cellType'] = cellType
# cellLbl = str(cellType)

# create cell population
netParams.cellParams[cellLbl] = param
netParams.popParams[cellLbl] = {'numCells': 1, 'cellType': cellType}

# create stimulation
netParams.stimTargetParams['ic_%s' %(cellLbl)] = {'source': 'ic_%s' %(cellLbl), 'conds': {'cellType': cellType}, 'sec': 'soma', 'loc': 0.5}
#netParams.stimTargetParams['vc_%s' %(cellLbl)] = {'source': 'vc_%s' %(cellLbl), 'conds': {'cellType': cellType}, 'sec': 'soma', 'loc': 0.5}

netParams.stimSourceParams['ic_%s' %(cellLbl)] = {'type': 'IClamp', 'amp': 0, 'delay': 0, 'dur': cfg.duration}
#netParams.stimSourceParams['vc_%s' %(cellLbl)] = {'type': 'VClamp', 'amp': [-60, -60, -60], 'dur': [0, cfg.delay, 0]}