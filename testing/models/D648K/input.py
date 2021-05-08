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
    surfaceSiteDensity=(2.72e-9, 'mol/cm^2'), # value in Deutschmann's paper
)

generatedSpeciesConstraints(
    allowed=['reaction libraries'],
    maximumNitrogenAtoms=2,
)

species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

species(
   label='O2',
   reactive=True,
   structure=adjacencyList(
       """
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

species(
    label='H2O',
    reactive=True,
    structure=SMILES("O"),
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
    label='NO2',
    reactive=True,
    structure=adjacencyList(
        """
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
"""),
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='CO',
    reactive=True,
    structure=adjacencyList(
        """
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
"""),
)

species(
    label='CO2',
    reactive=True,
    structure=adjacencyList(
        """
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
"""),
)

species(
    label='C3H6',
    reactive=True,
    structure=adjacencyList(
        """
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
"""),
)

species(
    label='Ar',
    reactive=False,
    structure=adjacencyList("1 Ar u0 p4 c0"),
)

#Lean cycle
surfaceReactor(  
    temperature=(648,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "NO": 0.000002,
        "NO2": 0.0000004,
        "C3H6": 0.0000006,
        "CO": 0.0004,
        "CO2": 0.07,
        "H2": 0.0,
        "H2O": 0.1, 
        "O2": 0.12,
        "Ar": 0.709597,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(4e3, 'm^-1'), #for cylinder: D=1mm=0.001m, surface/volume = 4/D = 4/(0.001m)
    terminationConversion = { "NO":0.9,},
)

#Rich cycle
surfaceReactor(  
    temperature=(648,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "NO": 0.000002,
        "NO2": 0.0000004,
        "C3H6": 0.0000006,
        "CO": 0.021,
        "CO2": 0.07,
        "H2": 0.007,
        "H2O": 0.1, 
        "O2": 0.009,
        "Ar": 0.792997,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(4e3, 'm^-1'), #for cylinder: D=1mm=0.001m, surface/volume = 4/D = 4/(0.001m)
    terminationConversion = { "NO":0.9,},
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