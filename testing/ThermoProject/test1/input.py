
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
    label='N2',
    reactive=True,
    structure=SMILES("N#N"),
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

#-------------

surfaceReactor(  
    temperature=(500,'K'),
    initialPressure=(70.0, 'bar'),
    initialGasMoleFractions={
        "NH3": 1.0,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e3, 'm^-1'),
    terminationConversion = { "NH3":0.90,},
)

simulator(
    atol=1e-18, 
    rtol=1e-12, 
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