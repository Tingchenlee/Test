#have same errors as issue#2039 and allowSingletO2=true
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006','Surface/Ammonia_Pd111_oxidation'], 
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',

)

catalystProperties(  #Pd111
    bindingEnergies = {
     		             'H':(-2.92248796E+00, 'eV/molecule'),
                         'C':(-7.16786381E+00, 'eV/molecule'),
                         'N':(-4.78495869E+00, 'eV/molecule'),
                         'O':(-4.13577325E+00, 'eV/molecule'),
                      },
    surfaceSiteDensity = (2.534E-09, 'mol/cm^2'),
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
    terminationTime=(0.1, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( 
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.00001, 
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

generatedSpeciesConstraints(
    allowSingletO2 = True,
)

