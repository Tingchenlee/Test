database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006'], 
    seedMechanisms = ['Surface/Popa_Rh111'],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(  #Rh111
    bindingEnergies = { 
    		           'H':(-2.83000775E+00, 'eV/molecule'),
                       'C':(-7.33483762E+00, 'eV/molecule'),
                       'N':(-5.30055389E+00, 'eV/molecule'),
                       'O':(-4.71419163E+00, 'eV/molecule'),
    },
    surfaceSiteDensity = (2.656E-09, 'mol/cm^2'),
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
    structure=adjacencyList(
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
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

surfaceReactor(  
    temperature=(723,'K'),
    initialPressure=(50.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.2,
        "H2": 0.1,
        "H2O": 0.2, 
        "N2": 0.2,
        "O2": 0.2,
        "NH3": 0.1,
    },
    initialSurfaceCoverages={
        "X": 1,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion = { "N2":0.80,},
    terminationTime=(10, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.01, 
    toleranceInterruptSimulation=1,
    maximumEdgeSpecies=10000,
    minCoreSizeForPrune=100,
    toleranceThermoKeepSpeciesInEdge=0.5, 
    minSpeciesExistIterationsForPrune=4,
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=False,
    generatePlots=False, 
    saveEdgeSpecies=False,
    saveSimulationProfiles=False,
)