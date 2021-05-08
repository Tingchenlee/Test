# Microkinetic model for ammonia oxidation
# Inspired by Grabow, Lars C. 
# "Computational catalyst screening."
# Computational Catalysis. RSC Publishing, 2013. 1-58.

database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran', 'primaryNS', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006'], 
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
    bindingEnergies = {  # default values for Pt(111)    
                          'H': (-2.754, 'eV/molecule'),
                          'O': (-3.811, 'eV/molecule'),
                          'C': (-7.025, 'eV/molecule'),
                          'N': (-4.632, 'eV/molecule'),
                      },
    surfaceSiteDensity=(2.483e-9, 'mol/cm^2'), # Default for Pt(111)
)
#CT = 1.467 * 10**19, m-2 sites per unit area on the Pt 211/111 surface
#site density = 1.467e19/1e4/6.02214086e23 = 2.436e-9 'mol/cm^2'

generatedSpeciesConstraints(
    allowed=['reaction libraries'],
    maximumNitrogenAtoms=2,
)

# List of species
species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]"),
)

species(
    label='H2O',
    reactive=True,
    structure=SMILES("O"),
)

species(
    label='N2',
    reactive=True,
    structure=SMILES("N#N"),
)

species(
    label='NO',
    reactive=True,
    structure=adjacencyList(
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
"""),
)

species(
    label='NH3',
    reactive=True,
    structure=adjacencyList(
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
"""),
)

species(
    label='N2O',
    reactive=True,
    structure=adjacencyList(
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
"""),
)
#-------------

#temperature from 1200 to 400K 
surfaceReactor(  
    temperature=(300,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "NH3": 0.001,
        "O2": 0.02,
        "H2O": 0.05, 
        "NO": 0.0,
        "N2": 0.0,
        "N2O": 0.0,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e3, 'm^-1'),
    terminationConversion = { "NH3":0.80,},
    #terminationTime=(60, 's'),
)

# surfaceReactor(  
#     temperature=(800,'K'),
#     initialPressure=(1.0, 'bar'),
#     initialGasMoleFractions={
#         "NH3": 0.001,
#         "O2": 0.02,
#         "H2O": 0.05, 
#         "NO": 0.0,
#         "N2": 0.0,
#         "N2O": 0.0,
#     },
#     initialSurfaceCoverages={
#         "X": 1.0,
#     },
#     surfaceVolumeRatio=(1.e3, 'm^-1'),
#     terminationConversion = { "NH3":0.80,},
# )

# surfaceReactor(  
#     temperature=(1000,'K'),
#     initialPressure=(1.0, 'bar'),
#     initialGasMoleFractions={
#         "NH3": 0.001,
#         "O2": 0.02,
#         "H2O": 0.05, 
#         "NO": 0.0,
#         "N2": 0.0,
#         "N2O": 0.0,
#     },
#     initialSurfaceCoverages={
#         "X": 1.0,
#     },
#     surfaceVolumeRatio=(1.e3, 'm^-1'),
#     terminationConversion = { "NH3":0.80,},
# )

# surfaceReactor(  
#     temperature=(1200,'K'),
#     initialPressure=(1.0, 'bar'),
#     initialGasMoleFractions={
#         "NH3": 0.001,
#         "O2": 0.02,
#         "H2O": 0.05, 
#         "NO": 0.0,
#         "N2": 0.0,
#         "N2O": 0.0,
#     },
#     initialSurfaceCoverages={
#         "X": 1.0,
#     },
#     surfaceVolumeRatio=(1.e3, 'm^-1'),
#     terminationConversion = { "NH3":0.80,},
# )

simulator(
    atol=1e-15, # absolute tolerance from the tpaper
    rtol=1e-12, # relative tolerance from the paper
)

model( 
    toleranceKeepInEdge=0.01,
    toleranceMoveToCore=0.001, 
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=100,
    #toleranceThermoKeepSpeciesInEdge=0.5, 
    #minSpeciesExistIterationsForPrune=4,
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=True, 
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)