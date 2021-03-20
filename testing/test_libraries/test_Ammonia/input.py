database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'], 
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006','Surface/Ammonia'],  
    seedMechanisms = [],  
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',

)

catalystProperties(
    bindingEnergies= {  
    		             'H':(-2.75367887E+00, 'eV/molecule'),
                         'C':(-7.02515507E+00, 'eV/molecule'),
                         'N':(-4.63224568E+00, 'eV/molecule'),
                         'O':(-3.81153179E+00, 'eV/molecule'),
                      },
    surfaceSiteDensity=(2.483E-09, 'mol/cm^2'),
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
    label='NH3',
    reactive=True,
    structure=adjacencyList("""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}"""),
)


species(
    label='NX',
    reactive=True,
    structure=adjacencyList("""
1 N u0 p1 c0 {2,T}
2 X u0 p0 c0 {1,T}"""),
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
        "CH4": 0.0,
        "H2": 0.5,
        "H2O": 0.0, 
        "N2": 0.0,
        "NX": 0.5,
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
