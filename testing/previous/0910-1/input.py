# Temperature from 625K to 775K
#The final model core has 26 species and 28 reactions & The final model edge has 80 species and 157 reactions
#Create little NH3!!!
#Data sources
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran','primaryNS', 'CHON_G4', 'CHON'], # 'surfaceThermoPt' is the default. Thermo data is derived using bindingEnergies for other metals 
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006',], # 'BurkeH2O2inN2', 'ERC-FoundationFuelv0.9', 'GRI-Mech3.0-N', 'Klippenstein_Glarborg2016' when Ni is used change the library to Surface/Deutschmann_Ni 
    seedMechanisms = ['Surface/ammoniaCombine'],  #'Nitrogen_Glarborg_Gimenez_et_al
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

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='CO2',
    reactive=True,
    structure=SMILES("O=C=O"),
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
    reactive = True,
    structure=SMILES('N')
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
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)


# Reaction systems
surfaceReactor(  #1
    temperature=(775,'K'),
    initialPressure=(200.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.0,
        "CO2": 0.0,
        "H2": 0.75,
        "H2O": 0.0, 
        "O2": 0.0,
        "N2": 0.25,
        "NH3": 0.0,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion = { "N2":0.80,},
    terminationTime=(0.1, 's'),
)

#c

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model( #1
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.0000000001, 
    toleranceInterruptSimulation=1,
    maximumEdgeSpecies=100000,
    minCoreSizeForPrune=150,
    toleranceThermoKeepSpeciesInEdge=0.5, # prune before simulation based on thermo
    minSpeciesExistIterationsForPrune=4,
    #filterReactions=False, # NotImplemented for SurfaceReactor
    #maxNumSpecies=100,
)


options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=True, # Enable to make plots of core and edge size etc. But takes a lot of the total runtime!
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
