def lSet(object, attribute, value):
    try:
        setattr(object, attribute, value)
        return True
    except:
        print("%s.%s does not exist" %(object, attribute))
        return False

def lGet(object, attribute):
    try:
        return getattr(object, attribute)
    except:
        print("%s.%s does not exist" %(object, attribute))
        return False

cellParams = {'conds': {'cellType': {'model': 'mm'}}, 'secs': {'soma': {'geom': {'L': 24.0, 'nseg': 1, 'diam': 24.0, 'Ra': 100.0, 'cm': 1.548}, 'topol': {}, 'mechs': {'CaL': {'pmax': 2.75e-05, 'hca': 0.0}, 'CaN': {'pmax': 2.8e-05, 'a': 0.7326, 'hca': 0.0}, 'CaPQ': {'pmax': 8e-06}, 'CaR': {'pmax': 1e-08}, 'CaT': {'pmax': 1e-08}, 'bkca': {'gbar': 0.0009}, 'cacc': {'gbar': 1e-06}, 'cadyn': {'vmaxsr': 3.75e-06, 'kpsr': 0.00027, 'jmaxsr': 3.5e-06, 'kip3': 0.0008, 'kactip3': 0.0003, 'konip3': 2.7, 'kinhip3': 0.0002, 'kcicr': 0.00198, 'ktcicr': 0.0006, 'vcicr': 5e-07, 'Kmer': 0.5, 'Bmer': 10.0, 'vmcu': 1.4468e-06, 'kmcu': 0.000606, 'nmcu': 2.3, 'vncx': 6e-05, 'kna': 8.0, 'kncx': 0.035, 'Kmmt': 1e-05, 'Bmmt': 0.065, 'k1': 37400000.0, 'k2': 250000.0, 'k3': 500.0, 'k4': 5.0, 'pump0': 4.232e-13}, 'hcn': {'gbarfast': 1.352e-05, 'gbarslow': 6.7615e-06}, 'ip3dif': {}, 'kaslow': {'gbar': 0.00136}, 'kdr': {'gbar': 0.002688}, 'kmtype': {'gbar': 0.0001}, 'knatype': {'gbar': 1e-05}, 'nakpump': {'gbar': 0.001, 'capm': 1.548}, 'nattxs': {'gbar': 0.0001}, 'nav1p8': {'gbar': 0.0087177}, 'nav1p9': {'gbar': 1e-05}, 'ncxsoma': {'ImaxNax': 1.1e-05, 'KnNacx': 87.5, 'KcNacx': 1.38}, 'pas': {'g': 0.0001, 'e': -41.583}, 'skca3': {'gbar': 0.0009, 'hcsk3': 5.6, 'E50hsk3': 0.00042, 'm': 0.0, 'm_vh': 24.0, 'm_sf': 128.0}, 'soce': {'pmax': 1e-09}, 'trpm8': {'gbar': 1e-07, 'C': 67.0, 'z': 0.65, 'em8': 0.0, 'p_ca': 0.01}}, 'ions': {'ca': {'e': 132.4579341637009, 'i': 0.000136, 'o': 2.0}, 'caer': {'e': 0.0, 'i': 0.4, 'o': 1.0}, 'caip3r': {'e': 0.0, 'i': 0.000136, 'o': 1.0}, 'camt': {'e': 0.0, 'i': 0.0002, 'o': 1.0}, 'cl': {'e': -32.7, 'i': 40.0, 'o': 145.0}, 'h': {'e': -30.0, 'i': 1.0, 'o': 1.0}, 'ip3': {'e': 0.0, 'i': 1.0, 'o': 1.0}, 'k': {'e': -84.7, 'i': 140.0, 'o': 5.0}, 'na': {'e': 68.83, 'i': 10.0, 'o': 150.0}}, 'vinit': -53.5}}, 'secLists': {'SectionList[0]': [], 'SectionList[1]': []}, 'globals': {'celsius': 22.0, 'v_init': -53.5}}


"""
cfg.gbar_bkca = 0.0009
cfg.gbar_kaslow = 0.00136
cfg.gbar_kdr = 0.002688
cfg.gbar_kmtype = 0.0001
cfg.gbar_knatype = 1e-5
cfg.gbar_nav1p7 = 0.10664
cfg.gbar_nav1p8 = 0.24271
cfg.gbar_nav1p9 = 1e-5
cfg.gbar_skca3 = 0.0009
"""