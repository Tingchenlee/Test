database(
    thermoLibraries=['surfaceThermoNi111', 'primaryThermoLibrary'],
    reactionLibraries = ['Surface/Deutschmann_Ni'],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
     bindingEnergies = { #Ni111
     		            'H':(-2.89202876E+00, 'eV/molecule'),
                        'C':(-6.79794124E+00, 'eV/molecule'),
                        'N':(-5.16380660E+00, 'eV/molecule'),
                        'O':(-4.98902184E+00, 'eV/molecule'),
                       },
    surfaceSiteDensity = (3.148E-09, 'mol/cm^2'),
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
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
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]"),
)

surfaceReactor(  
    temperature=(723,'K'),
    initialPressure=(50.0, 'bar'),
    initialGasMoleFractions={
        "H2O": 0.5,
        "N2": 0.5,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion = { "N2":0.80,},
    terminationTime=(0.1, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.00000001,
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
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)