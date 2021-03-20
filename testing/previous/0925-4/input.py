#Copy data from 0916-1, T=723K, P=10bar, H2/N2 ratio=2, only Ammonia_Ru in seedMechanisms
#Try different P, T
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'], # 'surfaceThermoPt' is the default. Thermo data is derived using bindingEnergies for other metals 
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006','Surface/ammoniaCombine'], # 'BurkeH2O2inN2', 'ERC-FoundationFuelv0.9', 'GRI-Mech3.0-N', 'Klippenstein_Glarborg2016' when Ni is used change the library to Surface/Deutschmann_Ni 
    seedMechanisms = ['Surface/Ammonia_Ru'],  #'Nitrogen_Glarborg_Gimenez_et_al
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
    surfaceSiteDensity=(2.630E-09, 'mol/cm^2'), # Default for Ru(0001)
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



surfaceReactor(  
    temperature=(723,'K'),
    initialPressure=(200.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.0,
        "H2": 0.67,
        "H2O": 0.0, 
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

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.000000000001, 
    toleranceInterruptSimulation=1,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=150,
    toleranceThermoKeepSpeciesInEdge=0.5, # prune before simulation based on thermo
    minSpeciesExistIterationsForPrune=4,
)



options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=True, # Enable to make plots of core and edge size etc. But takes a lot of the total runtime!
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
