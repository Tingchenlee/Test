database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006'],  
    seedMechanisms = [],  
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
    bindingEnergies = {  # default values for Ru(0001)  
    		              'H':(-2.85191775E+00, 'eV/molecule'),
                          'C':(-7.59790076E+00, 'eV/molecule'),
                          'N':(-5.96899731E+00, 'eV/molecule'),
                          'O':(-5.44919557E+00, 'eV/molecule'),
                      },
    surfaceSiteDensity=(2.630E-09, 'mol/cm^2'), 
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("C"),
)

species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

surfaceReactor(  
    temperature=(723,'K'),
    initialPressure=(200.0, 'bar'),
    initialGasMoleFractions={
        "H2": 0.67,
        "CH4": 0.33,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion = { "CH4":0.80,},
    terminationTime=(0.1, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.0000000001, 
    toleranceInterruptSimulation=1,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=150,
    toleranceThermoKeepSpeciesInEdge=0.5, 
    minSpeciesExistIterationsForPrune=4,
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=True, 
    saveSimulationProfiles=True,
)
