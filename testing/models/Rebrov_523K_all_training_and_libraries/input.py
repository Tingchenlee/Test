# Microkinetic model for ammonia oxidation
# E.V. Rebrov, M.H.J.M. de Croon, J.C. Schouten
# Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor
# Chemical Engineering Journal 90 (2002) 61–76

database(
    thermoLibraries=['surfaceThermoPt111', 'surfaceThermoNi111', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo', 'GRI-Mech3.0-N', 'NitrogenCurran', 'primaryNS', 'CHON'],
    reactionLibraries = ['Surface/CPOX_Pt/Deutschmann2006', 'Surface/Schneider_Pt111', 'Surface/Novell_Pt111', 'Surface/Offermans_Pt111', 'Surface/Scheuer_Pt', 'Surface/Ryan_Pt111', 'Surface/Rebrov_Pt111','Surface/Ralph_Pt111'], 
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
    metal = 'Pt111'
)

# catalystProperties(
#     bindingEnergies = {  # default values for Pt(111)    
#                           'H': (-2.754, 'eV/molecule'),
#                           'O': (-3.811, 'eV/molecule'),
#                           'C': (-7.025, 'eV/molecule'),
#                           'N': (-4.632, 'eV/molecule'),
#                       },
#     surfaceSiteDensity=(2.483e-9, 'mol/cm^2'), #This is calculated based on the value from the paper# Default for Pt(111) =2.483e-9
# )

generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumNitrogenAtoms=2,
    maximumOxygenAtoms=3,
)

# List of species
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

species(
    label='N2O',
    reactive=True,
    structure=adjacencyList(
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
"""),
)

species(
    label='He',
    reactive=False,
    structure=adjacencyList(
"""
1 He u0 p1 c0
"""),
)

#-------------

#temperature from 523-673K 
surfaceReactor(  
    temperature=(523,'K'),
    initialPressure=(1.0, 'bar'),
    nSims=12,
    initialGasMoleFractions={
        "NH3": 0.12,
        "O2": 0.4,
        "He": 0.48,
        "NO":0.0,
        "H2O":0.0,
        "N2O":0.0,
        "N2":0.0,
    },
    initialSurfaceCoverages={
        "X": 1.0,
    },
    surfaceVolumeRatio=(2.8571428e4, 'm^-1'), #A/V = 280µm*π*9mm/140µm*140µm*π*9mm = 2.8571428e4^m-1
    terminationConversion = {"NH3":0.99,},
    #terminationTime=(10, 's'),
)

simulator( #default for surface reaction atol=1e-18,rtol=1e-12
    atol=1e-18, #absolute tolerance are 1e-15 to 1e-25
    rtol=1e-12, #relative tolerance is usually 1e-4 to 1e-8
)

model( 
    toleranceKeepInEdge=0.001, #recommend setting toleranceKeepInEdge to not be larger than 10% of toleranceMoveToCore
    toleranceMoveToCore=0.01, 
    toleranceInterruptSimulation=1e8, #This value should be set to be equal to toleranceMoveToCore unless the advanced pruning feature is desired
    #to always enable pruning should be set as a high value, e.g. 1e8
    maximumEdgeSpecies=50000, #set up less than 200000
    minCoreSizeForPrune=50, #default value
    #toleranceThermoKeepSpeciesInEdge=0.5, 
    minSpeciesExistIterationsForPrune=2, #default value = 2 iteration
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=True, 
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)