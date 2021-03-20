#Copy data from 0916-1,revise to easier version for testing new libraries
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006'], 
    seedMechanisms = [],  
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',

)

catalystProperties(
    bindingEnergies = {  # default values for Cu(111)   
    		            'H':(-2.58383235E+00, 'eV/molecule'),
                        'C':(-4.96033553E+00, 'eV/molecule'),
                        'N':(-3.58446699E+00, 'eV/molecule'),
                        'O':(-4.20763879E+00, 'eV/molecule'),
                      },
    surfaceSiteDensity=(2.943E-09, 'mol/cm^2'), # Default for Cu(111)
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
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


surfaceReactor(  #1
    temperature=(725,'K'),
    initialPressure=(200.0, 'bar'),
    initialGasMoleFractions={
        "H2": 0.67,
        "N2": 0.33,
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

model( #1
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.000000000001, 
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
