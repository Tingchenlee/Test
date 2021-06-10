#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Double/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CO + X <=> CO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.5,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111

"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R5 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "NH_X <=> NH + X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4E21, '1/s'), 
        n = 0.0,
        Ea = (83, 'kcal/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111

"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R48 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "O + X <=> O_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.0491,
        n = 0.250,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Vlachos_Pt111

"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R3 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "CO + X <=> CO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Vlachos_Pt111

"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R5 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "CH2 + X <=> CH2_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.045,
        n = 0.118,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Vlachos_Pt111

"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R51 in Table 2
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 6,
    label = "CO + X <=> CO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.5,
        n = -2.00,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
Training reaction from kinetics library: Surface/Vlachos_Rh

"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R19 in Table 4
""",
    metal = "Rh",
)

