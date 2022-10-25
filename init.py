from netpyne import sim

cfg, netParams = sim.readCmdLineArgs()
sim.create(simConfig = cfg, netParams = netParams)

# h -> define tau values
sim.h.load_file('tautables.hoc')
sim.simulate() # calls runSim() and gatherData()
sim.analyze()
