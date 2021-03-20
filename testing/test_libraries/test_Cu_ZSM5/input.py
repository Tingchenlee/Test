database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006'], 
    seedMechanisms = ['Surface/Ammonia_Cu_ZSM5'],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',

)

catalystProperties(
     bindingEnergies = {# Default for Cu(111)
     		            'H':(-2.58383235E+00, 'eV/molecule'),
                        'C':(-4.96033553E+00, 'eV/molecule'),
                        'N':(-3.58446699E+00, 'eV/molecule'),
                        'O':(-4.20763879E+00, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.943E-09, 'mol/cm^2'), # Default for Cu(111)
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
    structure=SMILES('[O][O]'),
)


surfaceReactor(  
    temperature=(723,'K'),
    initialPressure=(100.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.0,
        "H2": 0.25,
        "H2O": 0.25, 
        "N2": 0.25,
        "O2": 0.25,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion = { "N2":0.80,},
    terminationTime=(0.01, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1E-6, 
    toleranceInterruptSimulation=0.05,
    maximumEdgeSpecies=1E6,
    minCoreSizeForPrune=100,
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



