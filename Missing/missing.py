#Ishikawa_Rh111
#This is Nitrogen/51
entry(
    index = 1,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (8.19E19, 'cm^2/(mol*s)'),  
        n = 1.009,
        Ea = (76196, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NO Dissociation""",
    longDesc = u"""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906
This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal = "Rh",
    facet = "111",
)

#Schnedier_Rh111
entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.47E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (226751.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 2.35eV = 226751.5J/mol

This is reaction (12) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.47E21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (206488.6, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 2.14eV = 206488.6J/mol

This is reaction (14) in Table S3
""",
    metal = "Rh",
    facet = "111",
)