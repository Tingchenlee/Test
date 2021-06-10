
entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 2,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)


entry(
    index = 3,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 4,
    label = "H2 + X <=> H2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R4""",
    longDesc = u"""H2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 5,
    label = "N2 + X <=> N2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 6,
    label = "O2 + X <=> O2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R6""",
    longDesc = u"""O2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 7,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 8,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R8""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 9,
    label = "H_X + OH_X <=> H2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R9""",
    longDesc = u"""Surface_Dissociation?""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 10,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 11,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 12,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 13,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 14,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 15,
    label = "NH3_X + O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 16,
    label = "NH2_X + O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 17,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 18,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 19,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 20,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)


entry(
    index = 21,
    label = "NH3_X + OH_X <=> NH2_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R21""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 22,
    label = "NH2_X + OH_X <=> NH_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R22""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 23,
    label = "NH_X + OH_X <=> N_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R23""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 24,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 25,
    label = "N_X + O2_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R25""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 26,
    label = "N2_X + O_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 27,
    label = "N2_X + OH_X <=> N2OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R27""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 28,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 29,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 30,
    label = "NO2 + X <=> NO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 31,
    label = "N2O + X <=> N2O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 32,
    label = "N2O + X <=> N2 + O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R32""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

#This reaction shows resonanceError
entry(
    index = 33,
    label = "N2O + X + X <=> N_X + NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R33""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 34,
    label = "N2O_X + X <=> N_X + NO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'kJ/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 35,
    label = "N2H4_X + X <=> NH2_X + NH2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R35""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 36,
    label = "N2H4_X + X <=> N2H3_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R36""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 37,
    label = "N2H3_X + X <=> N2H2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R37""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 38,
    label = "N2H2_X + X <=> N2H_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R38""",
    longDesc = u"""Surface_Dissociation_Beta""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 39,
    label = "N2H_X + X <=> N2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R39""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 40,
    label = "H_X + NO_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R40""",
    longDesc = u"""Surface_Dissociation_Beta """,
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 41,
    label = "H_X + N_X + O_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  #maybe the unit is 'm^4/(mol*s)'
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R41""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 42,
    label = "NHO + X <=> HNO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R42""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 43,
    label = "NHO2 + X <=> HNO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R43""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 44,
    label = "NHO3 + X <=> HNO3_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R44""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 45,
    label = "NH2OH + X <=> NH2OH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R45""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 46,
    label = "NH2NO + X <=> NH2NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R46""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)


entry(
    index = 47,
    label = "NH2NO2 + X <=> NH2NO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R47""",
    longDesc = u"""adsoprtion""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 48,
    label = "H_X + H_X <=> H2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 50,
    label = "O_X + O_X <=> O2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 51,
    label = "H2_X <=> H2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R4""",
    longDesc = u"""H2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 52,
    label = "N2_X <=> N2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 53,
    label = "O2_X <=> O2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R6""",
    longDesc = u"""O2 Surface_Adsorption_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 54,
    label = "OH_X + X <=> H_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 55,
    label = "H2O_X + X <=> H_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 56,
    label = "H2O + X + X <=> H_X + OH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R9""",
    longDesc = u"""Surface_Dissociation?""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 57,
    label = "H2O_X <=> H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 59,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 60,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 61,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 62,
    label = "NH2_X + OH_X <=> NH3_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 63,
    label = "NH_X + OH_X <=> NH2_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 64,
    label = "N_X + OH_X <=> NH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 65,
    label = "NH2_X + H2O_X <=> NH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 66,
    label = "NH_X + H2O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 67,
    label = "N_X + H2O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)


entry(
    index = 68,
    label = "NH2_X + H2O + X <=> NH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R21""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 69,
    label = "NH_X + H2O + X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R22""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 70,
    label = "N_X + H2O + X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R23""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 71,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 72,
    label = "NO2_X + X <=> N_X + O2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R25""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 73,
    label = "N2O_X + X <=> N2_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 74,
    label = "N2OH_X + X <=> N2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 75,
    label = "NO2_X + X <=> NO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 76,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 77,
    label = "NO2_X <=> NO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 78,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 79,
    label = "N2 + O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R32""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

#This reaction shows resonanceError
entry(
    index = 80,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R33""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 81,
    label = "N_X + NO_X <=> N2O_X + X,
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'kJ/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 82,
    label = "NH2_X + NH2_X <=> N2H4_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R35""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 83,
    label = "N2H3_X + H_X <=> N2H4_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R36""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 84,
    label = "N2H2_X + H_X <=> N2H3_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R37""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 85,
    label = "N2H_X + H_X <=> N2H2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R38""",
    longDesc = u"""Surface_Dissociation_Beta""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 86,
    label = "N2_X + H_X <=> N2H_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R39""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 87,
    label = "HNO_X + X <=> H_X + NO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R40""",
    longDesc = u"""Surface_Dissociation_Beta """,
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 88,
    label = "HNO_X + X <=> H_X + N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R41""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 89,
    label = "HNO_X <=> NHO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R42""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 90,
    label = "HNO2_X <=> NHO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R43""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 91,
    label = "HNO3_X <=> NHO3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R44""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 92,
    label = "NH2OH_X <=> NH2OH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R45""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 93,
    label = "NH2NO_X <=> NH2NO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R46""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 94,
    label = "NH2NO2_X <=> NH2NO2 + X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R47""",
    longDesc = u"""desorption""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 95,
    label = "O_X + H2O_X <=> OH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 96,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 97,
    label = "HNO_X + X <=> NH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R97""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 98,
    label = "NH_X + O_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R97""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 99,
    label = "NOH_X + X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R99""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 100,
    label = "N_X + OH_X <=> NOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R99""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 101,
    label = "HNOH_X + X <=> HNO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R101""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 102,
    label = "HNO_X + H_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R101""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 103,
    label = "HNOH_X + X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R103""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 104,
    label = "NH_X + OH_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R103""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 105,
    label = "HNOH_X + X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R105""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 106,
    label = "N_X + H2O_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R105""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 107,
    label = "O + X <=> O_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 108,
    label = "O_X <=> O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 109,
    label = "CO + X <=> CO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 110,
    label = "CO_X <=> CO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 111,
    label = "CO2 + X <=> CO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 112,
    label = "CO2_X <=> CO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 113,
    label = "CO2_X + X <=> CO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 114,
    label = "CO_X + O_X <=> CO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 115,
    label = "OH + X <=> OH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 116,
    label = "OH_X <=> OH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 117,
    label = "H + X <=> H_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 118,
    label = "H_X <=> H + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 119,
    label = "CO2_X + H_X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt/19""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 120,
    label = "CO_X + OH_X <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt/19""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 121,
    label = "COOH + X <=> COOH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 122,
    label = "COOH_X <=> COOH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 123,
    label = "COOH_X + X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 124,
    label = "CO_X + OH_X <=> COOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 125,
    label = "COOH_X + X <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 126,
    label = "CO2_X + H_X <=> COOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 127,
    label = "CO_X + H2O_X <=> COOH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 128,
    label = "COOH_X + H_X <=> CO_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 129,
    label = "CO2_X + OH_X <=> COOH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 130,
    label = "COOH_X + O_X <=> CO2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 131,
    label = "CO2_X + H2O_X <=> COOH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 132,
    label = "COOH_X + OH_X <=> CO2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 133,
    label = "HCOO + X + X <=> HCOO_XX",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Bidentate""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 134,
    label = "HCOO_XX <=> HCOO + X + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Bidentate""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

#index=135 in the paper was a bidentate HCOO_XX, which might cause the issue of an adsorbate vdW species.
#This might cause an UndeterminableKineticsError, maybe we don't want to include this reaction.
entry(
    index = 135,
    label = "CO2_X + H_X <=> HCOO_XX",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

#Same issue as index=135
entry(
    index = 136,
    label = "HCOO_XX <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

#index=137 in the paper was a bidentate HCOO_XX, which might cause the issue of an adsorbate vdW species.
#This might cause an UndeterminableKineticsError, maybe we don't want to include this reaction.
entry(
    index = 137,
    label = "CO2_X + OH_X + X <=> HCOO_XX + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^4/(mol^2*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

#Same issue as index=137
entry(
    index = 138,
    label = "HCOO_XX + O_X <=> CO2_X + OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 139,
    label = "C + X <=> C_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Triple bonds""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 140,
    label = "C_X <=> C + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Triple bonds""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 141,
    label = "CH + X <=> CH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 142,
    label = "CH_X <=> CH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 143,
    label = "CH2 + X <=> CH2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 144,
    label = "CH2_X <=> CH2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 145,
    label = "CH3 + X <=> CH3_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 146,
    label = "CH3_X <=> CH3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 147,
    label = "CH4 + X + X <=> CH3_X + H_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Dissociative""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 148,
    label = "CH3_X + H_X <=> CH4 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Dissociative""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 149,
    label = "CH3_X + X <=> CH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 150,
    label = "CH2_X + H_X <=> CH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 151,
    label = "CH2_X + X <=> CH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 152,
    label = "CH_X + H_X <=> CH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (7.73E19, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (35.4, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 153,
    label = "CH_X + X <=> C_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 154,
    label = "C_X + H_X <=> CH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 155,
    label = "CH3_X + O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 156,
    label = "CH2_X + OH_X <=> CH3_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""= """,
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 157,
    label = "CH_X + OH_X <=> CH2_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 158,
    label = "CH2_X + O_X <=> CH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 159,
    label = "C_X + OH_X <=> CH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 160,
    label = "CH_X + O_X <=> C_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 161,
    label = "CH2_X + H2O_X <=> CH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 162,
    label = "CH3_X + OH_X <=> CH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 163,
    label = "CH_X + H2O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 164,
    label = "CH2_X + OH_X <=> CH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 165,
    label = "C_X + H2O_X <=> CH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 166,
    label = "CH_X + OH_X <=> C_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 167,
    label = "CO_X + X <=> C_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 168,
    label = "C_X + O_X <=> CO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 169,
    label = "CO_X + H_X <=> CH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 170,
    label = "CH_X + O_X <=> CO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 171,
    label = "CO_X + H_X <=> C_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 172,
    label = "C_X + OH_X <=> CO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 173,
    label = "CO_X + CO_X <=> C_X + CO2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 174,
    label = "C_X + CO2_X <=> CO_X + CO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 175,
    label = "CH3OH + X <=> CH3OH_X",
    kinetics = StickingCoefficient(
        A = ,  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 176,
    label = "CH3OH_X <=> CH3OH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 177,
    label = "CH3O + X <=> CH3O_X",
    kinetics = StickingCoefficient(
        A = ,  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 178,
    label = "CH3O_X <=> CH3O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 179,
    label = "CH2O + X <=> CH2O_X",
    kinetics = StickingCoefficient(
        A = ,  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 180,
    label = "CH2O_X <=> CH2O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 181,
    label = "HCO + X <=> HCO_X",
    kinetics = StickingCoefficient(
        A = ,  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 182,
    label = "HCO_X <=> HCO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 183,
    label = "CH2OH + X <=> CH2OH_X",
    kinetics = StickingCoefficient(
        A = ,  
        n = ,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 184,
    label = "CH2OH_X <=> CH2OH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 185,
    label = "CH3OH_X + X <=> CH3O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 186,
    label = "CH3O_X + H_X <=> CH3OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 187,
    label = "CH3O_X + X <=> CH2O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 188,
    label = "CH2O_X + H_X <=> CH3O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 189,
    label = "CH2O_X + X <=> HCO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 190,
    label = "HCO_X + H_X <=> CH2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 191,
    label = "HCO_X + X <=> CO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 192,
    label = "CO_X + H_X <=> HCO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 193,
    label = "CH3OH_X + X <=> CH2OH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (), 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 194,
    label = "CH2OH_X + H_X <=> CH3OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 195,
    label = "CH2OH_X + X <=> CH2O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 196,
    label = "CH2O_X + H_X <=> CH2OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 197,
    label = "N + X <=> N_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Triple""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 198,
    label = "N_X <=> N + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Triple""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 199,
    label = "NH2 + X <=> NH2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 200,
    label = "NH2_X <=> NH2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 201,
    label = "NH + X <=> NH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = ,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 202,
    label = "NH_X <=> NH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 203,
    label = "N_X + OH_X <=> NO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 204,
    label = "NO_X + H_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 205,
    label = "NO_X + OH_X <=> NO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 206,
    label = "N2O_X + H_X <=> NO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 81,
    label = "HCN + X <=> HCN_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 82,
    label = "HCN_X <=> HCN + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 83,
    label = "CN + X <=> CN_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 84,
    label = "CN_X <=> CN + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 85,
    label = "HCN_X + X <=> CN_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 86,
    label = "CN_X + H_X <=> HCN_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 87,
    label = "HCN_X + O_X <=> CN_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 88,
    label = "CN_X + OH_X <=> HCN_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 89,
    label = "HCN_X + OH_X <=> CN_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 90,
    label = "CN_X + H2O_X <=> HCN_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 91,
    label = "CN_X + O_X <=> C_X + NO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 92,
    label = "C_X + NO_X <=> CN_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 93,
    label = "CO_X + N_X <=> CN_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 94,
    label = "CN_X + O_X <=> CO_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 99,
    label = "CH2O_X + X <=> HCO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 100,
    label = "HCO_X + H_X <=> CH2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 101,
    label = "HCO_X + OH_X <=> CH2O_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 102,
    label = "CH2O_X + O_X <=> HCO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 103,
    label = "HCO_X + H2O_X <=> CH2O_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 104,
    label = "CH2O_X + OH_X <=> HCO_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)


entry(
    index = 109,
    label = "CO_X + H2O_X <=> HCO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 110,
    label = "HCO_X + OH_X <=> CO_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = ,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 121,
    label = "C2N2 + X <=> C2N2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 122,
    label = "C2N2_X <=> C2N2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 123,
    label = "C2N2_X + X <=> CN_X + CN_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'kJ/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 124,
    label = "CN_X + CN_X <=> C2N2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'kJ/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = 107,
    label = "CO_X + OH_X <=> HCO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = 108,
    label = "HCO_X + O_X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = ,
    label = "N2H3_X + NH2_X <=> N2H2_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = ,
    label = "N2H2_X + NH3_X <=> N2H3_X + NH2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""""",
	metal = "Cattype",
    facet = "111",
)

entry(
    index = ,
    label = "N2H2_X + NH2_X <=> N2H_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)

entry(
    index = ,
    label = "N2H4_X + NH2_X <=> N2H3_X + NH3_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""""",
    metal = "Cattype",
    facet = "111",
)