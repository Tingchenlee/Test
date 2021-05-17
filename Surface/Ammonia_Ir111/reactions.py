#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ir111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Adsorption and decomposition of NH3 on Ir(111): A density functional theory study"
https://doi.org/10.1016/j.susc.2013.06.001
Wuying Huang,Chun Cheng, Eryin Feng
Surface Science
Volume 616, October 2013, Pages 29-35
"""
entry(
    index = 12,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.109E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (94560.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
Based primarily on 
"Adsorption and decomposition of NH3 on Ir(111): A density functional theory study"
https://doi.org/10.1016/j.susc.2013.06.001
Wuying Huang,Chun Cheng, Eryin Feng
Surface Science
Volume 616, October 2013, Pages 29-35
Use theoretical calculation method proposed by Campbell et al.(2013) and
applied RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A (at 298K) = 5.456E11(1/s)/2.587E-9(mol/cm^2) = 2.109E20 cm^2/(mol*s)
Ea = 0.98eV = 94560.2J/mol
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 13,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.355E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (101314.5, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
Based primarily on 
"Adsorption and decomposition of NH3 on Ir(111): A density functional theory study"
https://doi.org/10.1016/j.susc.2013.06.001
Wuying Huang,Chun Cheng, Eryin Feng
Surface Science
Volume 616, October 2013, Pages 29-35
Use theoretical calculation method proposed by Campbell et al.(2013) and
applied RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A (at 298K) = 6.09253E11(1/s)/2.587E-9(mol/cm^2) = 2.355E20 cm^2/(mol*s)
Ea = 1.05eV = 101314.5J/mol
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 14,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.355E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (90700.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
Based primarily on 
"Adsorption and decomposition of NH3 on Ir(111): A density functional theory study"
https://doi.org/10.1016/j.susc.2013.06.001
Wuying Huang,Chun Cheng, Eryin Feng
Surface Science
Volume 616, October 2013, Pages 29-35
Use theoretical calculation method proposed by Campbell et al.(2013) and
applied RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A (at 298K) = 6.09253E11(1/s)/2.587E-9(mol/cm^2) = 2.355E20 cm^2/(mol*s)
Ea = 0.94eV = 90700.6J/mol
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.585E23, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (149559.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
Based primarily on 
"Adsorption and decomposition of NH3 on Ir(111): A density functional theory study"
https://doi.org/10.1016/j.susc.2013.06.001
Wuying Huang,Chun Cheng, Eryin Feng
Surface Science
Volume 616, October 2013, Pages 29-35
Use theoretical calculation method proposed by Campbell et al.(2013) and
applied RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A (at 298K) = 4.10125E14(1/s)/2.587E-9(mol/cm^2) = 1.585E23 cm^2/(mol*s)
Ea = 1.55eV = 149559.5J/mol
""",
    metal = "Ir",
    facet = "111",
)