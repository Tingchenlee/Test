
entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Cattype',
)

entry(
    index = 2,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Cattype',
)


entry(
    index = 3,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Cattype",
)

entry(
    index = 4,
    label = "H2 + X <=> H2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R4""",
    longDesc = u"""H2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 5,
    label = "N2 + X <=> N2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 6,
    label = "O2 + X <=> O2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R6""",
    longDesc = u"""O2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 7,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 8,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R8""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 9,
    label = "H_X + OH_X <=> H2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R9""",
    longDesc = u"""Surface_Dissociation?""",
    metal = "Cattype",
)

entry(
    index = 10,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R10""",
    longDesc = u"""Surface_Adsorption""",
	metal = "Cattype",
)

entry(
    index = 11,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Cattype',
)

entry(
    index = 12,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 13,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 14,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 15,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R15""",
    longDesc = u"""Surface_Abstraction_vdW""",
    metal = "Cattype",
)

entry(
    index = 16,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R16""",
    longDesc = u"""Surface_Abstraction""",
    metal = "Cattype",
)

entry(
    index = 17,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R17""",
    longDesc = u"""Surface_Abstraction""",
    metal = "Cattype",
)

entry(
    index = 18,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R18""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 19,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R19""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 20,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R20""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)


entry(
    index = 21,
    label = "NH3_X + OH_X <=> NH2_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R21""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 22,
    label = "NH2_X + OH_X <=> NH_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R22""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 23,
    label = "NH_X + OH_X <=> N_X + H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R23""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 24,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R24""",
    longDesc = u"""Nitrogen/51""",
    metal = "Cattype",
)

entry(
    index = 25,
    label = "N_X + O2_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R25""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 26,
    label = "N2_X + O_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R26""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = 'Cattype',
)

entry(
    index = 27,
    label = "N2_X + OH_X <=> N2OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R27""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = 'Cattype',
)

entry(
    index = 28,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R28""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 29,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R30""",
    longDesc = u"""Surface_Adsorption_Single""",
    metal = 'Cattype',
)

entry(
    index = 30,
    label = "NO2 + X <=> NO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R31""",
    longDesc = u"""Surface_Adsorption_Single""",
    metal = 'Cattype',
)

entry(
    index = 31,
    label = "N2O + X <=> N2O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R31""",
    longDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 32,
    label = "N2O + X <=> N2 + O_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R32""",
    longDesc = u"""""",
    metal = 'Cattype',
)

#This reaction shows resonanceError
entry(
    index = 33,
    label = "N2O + X + X <=> N_X + NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R33""",
    longDesc = u"""""",
    metal = 'Cattype',
)
entry(
    index = 34,
    label = "N2O_X + X <=> N_X + NO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R34""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 35,
    label = "N2H4_X + X <=> NH2_X + NH2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R35""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 36,
    label = "N2H4_X + X <=> N2H3_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R36""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 37,
    label = "N2H3_X + X <=> N2H2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R37""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 38,
    label = "N2H2_X + X <=> N2H_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R38""",
    longDesc = u"""Surface_Dissociation_Beta""",
    metal = "Cattype",
)

entry(
    index = 39,
    label = "N2H_X + X <=> N2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R39""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 40,
    label = "H_X + NO_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R40""",
    longDesc = u"""Surface_Dissociation_Beta """,
    metal = "Cattype",
)

entry(
    index = 41,
    label = "H_X + N_X + O_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  #maybe the unit is 'm^4/(mol*s)'
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R41""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 42,
    label = "NHO + X <=> HNO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R42""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)

entry(
    index = 43,
    label = "NHO2 + X <=> HNO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R43""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)

entry(
    index = 44,
    label = "NHO3 + X <=> HNO3_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R44""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)

entry(
    index = 45,
    label = "NH2OH + X <=> NH2OH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R45""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)

entry(
    index = 46,
    label = "NH2NO + X <=> NH2NO_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R46""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)


entry(
    index = 47,
    label = "NH2NO2 + X <=> NH2NO2_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R47""",
    longDesc = u"""adsoprtion""",
    metal = 'Cattype',
)

entry(
    index = 48,
    label = "H_X + H_X <=> H2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Cattype',
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Cattype',
)

entry(
    index = 50,
    label = "O_X + O_X <=> O2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Cattype",
)

entry(
    index = 51,
    label = "H2_X <=> H2 + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R4""",
    longDesc = u"""H2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 52,
    label = "N2_X <=> N2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 53,
    label = "O2_X <=> O2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R6""",
    longDesc = u"""O2 Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 54,
    label = "OH_X + X <=> H_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 55,
    label = "H2O_X + X <=> H_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R8""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 56,
    label = "H2O + X + X <=> H_X + OH_X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R9""",
    longDesc = u"""Surface_Dissociation?""",
    metal = "Cattype",
)

entry(
    index = 57,
    label = "H2O_X <=> H2O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R10""",
    longDesc = u"""Surface_Adsorption""",
	metal = "Cattype",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Cattype',
)

entry(
    index = 59,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 60,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 61,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 62,
    label = "NH2_X + OH_X <=> NH3_X +O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R15""",
    longDesc = u"""Surface_Abstraction_vdW""",
    metal = "Cattype",
)

entry(
    index = 63,
    label = "NH_X + OH_X <=> NH2_X +O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R16""",
    longDesc = u"""Surface_Abstraction""",
    metal = "Cattype",
)

entry(
    index = 64,
    label = "N_X + OH_X <=> NH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R17""",
    longDesc = u"""Surface_Abstraction""",
    metal = "Cattype",
)

entry(
    index = 65,
    label = "NH2_X + H2O_X <=> NH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R18""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 66,
    label = "NH_X + H2O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R19""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 67,
    label = "N_X + H2O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R20""",
    longDesc = u"""Surface_Abstraction_Single_vdW""",
    metal = "Cattype",
)


entry(
    index = 68,
    label = "NH2_X + H2O + X <=> NH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R21""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 69,
    label = "NH_X + H2O + X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R22""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 70,
    label = "N_X + H2O + X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'm^5/(mol^2*s)'), 
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R23""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 71,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R24""",
    longDesc = u"""Nitrogen/51"""
    metal = "Cattype",
)

entry(
    index = 72,
    label = "NO2_X + X <=> N_X + O2_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R25""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 73,
    label = "N2O_X + X <=> N2_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R26""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = 'Cattype',
)

entry(
    index = 74,
    label = "N2OH_X + X <=> N2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R27""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = 'Cattype',
)

entry(
    index = 75,
    label = "NO2_X + X <=> NO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R28""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 76,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R30""",
    longDesc = u"""Surface_Adsorption_Single""",
    metal = 'Cattype',
)

entry(
    index = 77,
    label = "NO2_X <=> NO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R31""",
    longDesc = u"""Surface_Adsorption_Single""",
    metal = 'Cattype',
)

entry(
    index = 78,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R31""",
    longDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    metal = 'Cattype',
)

entry(
    index = 79,
    label = "N2 + O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R32""",
    longDesc = u"""""",
    metal = 'Cattype',
)

#This reaction shows resonanceError
entry(
    index = 80,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R33""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 81,
    label = "N_X + NO_X <=> N2O_X + X,
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R34""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 82,
    label = "NH2_X + NH2_X <=> N2H4_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R35""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 83,
    label = "N2H3_X + H_X <=> N2H4_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R36""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Cattype",
)

entry(
    index = 84,
    label = "N2H2_X + H_X <=> N2H3_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R37""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cattype",
)

entry(
    index = 85,
    label = "N2H_X + H_X <=> N2H2_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R38""",
    longDesc = u"""Surface_Dissociation_Beta""",
    metal = "Cattype",
)

entry(
    index = 86,
    label = "N2_X + H_X <=> N2H_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R39""",
    longDesc = u"""Surface_Addition_Single_vdW""",
    metal = "Cattype",
)

entry(
    index = 87,
    label = "HNO_X + X <=> H_X + NO_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R40""",
    longDesc = u"""Surface_Dissociation_Beta """,
    metal = "Cattype",
)

entry(
    index = 88,
    label = "HNO_X + X <=> H_X + N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R41""",
    longDesc = u"""""",
    metal = "Cattype",
)

entry(
    index = 89,
    label = "HNO_X <=> NHO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R42""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 90,
    label = "HNO2_X <=> NHO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R43""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 91,
    label = "HNO3_X <=> NHO3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R44""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 92,
    label = "NH2OH_X <=> NH2OH + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R45""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 93,
    label = "NH2NO_X <=> NH2NO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R46""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 94,
    label = "NH2NO2_X <=> NH2NO2 + X",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R47""",
    longDesc = u"""desorption""",
    metal = 'Cattype',
)

entry(
    index = 95,
    label = "O_X + H2O_X <=> OH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R95""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 96,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R95""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 97,
    label = "HNO_X + X <=> NH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R97""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 98,
    label = "NH_X + O_X <=> HNO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R97""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 99,
    label = "NOH_X + X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R99""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 100,
    label = "N_X + OH_X <=> NOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R99""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 101,
    label = "HNOH_X + X <=> HNO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R101""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 102,
    label = "HNO_X + H_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R101""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 103,
    label = "HNOH_X + X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R103""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 104,
    label = "NH_X + OH_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R103""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 105,
    label = "HNOH_X + X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R105""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 106,
    label = "N_X + H2O_X <=> HNOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R105""",
    longDesc = u"""""",
    metal = 'Cattype',
)


#entry(
#    index = 1,
#    label = "H2 + X + X <=> H_X + H_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R1""",
#    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    metal = 'Cattype',
#)

#entry(
#    index = 2,
#    label = "N2 + X + X <=> N_X + N_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R2""",
#    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
#    metal = 'Cattype',
#)


#entry(
#    index = 3,
#    label = "O2 + X + X <=> O_X + O_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R3""",
#    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
#	metal = "Cattype",
#)

#entry(
#    index = 4,
#    label = "H2 + X <=> H2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R4""",
#    longDesc = u"""H2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 5,
#    label = "N2 + X <=> N2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R5""",
#    longDesc = u"""N2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 6,
#    label = "O2 + X <=> O2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R6""",
#    longDesc = u"""O2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 7,
#    label = "H_X + O_X <=> OH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R7""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 8,
#    label = "H_X + OH_X <=> H2O_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R8""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 9,
#    label = "H_X + OH_X <=> H2O + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R9""",
#    longDesc = u"""Surface_Dissociation?""",
#    metal = "Cattype",
#)

#entry(
#    index = 10,
#    label = "H2O + X <=> H2O_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R10""",
#    longDesc = u"""Surface_Adsorption""",
#	metal = "Cattype",
#)

#entry(
#    index = 11,
#    label = "NH3 + X <=> NH3_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Cattype',
#)

#entry(
#    index = 12,
#    label = "NH3_X + X <=> NH2_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#       Tmin = (200, 'K'),
#      Tmax = (3000, 'K'),
#   ),
#   shortDesc = u"""R12""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 13,
#    label = "NH2_X + X <=> NH_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R13""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 14,
#    label = "NH_X + X <=> N_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R14""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 15,
#    label = "NH3_X +O_X <=> NH2_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R15""",
#    longDesc = u"""Surface_Abstraction_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 16,
#    label = "NH2_X +O_X <=> NH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R16""",
#    longDesc = u"""Surface_Abstraction""",
#    metal = "Cattype",
#)

#entry(
#    index = 17,
#    label = "NH_X + O_X <=> N_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R17""",
#    longDesc = u"""Surface_Abstraction""",
#    metal = "Cattype",
#)

#entry(
#    index = 18,
#    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R18""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 19,
#    label = "NH2_X + OH_X <=> NH_X + H2O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R19""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 20,
#    label = "NH_X + OH_X <=> N_X + H2O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R20""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)


#entry(
#    index = 21,
#    label = "NH3_X + OH_X <=> NH2_X + H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R21""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 22,
#    label = "NH2_X + OH_X <=> NH_X + H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R22""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 23,
#    label = "NH_X + OH_X <=> N_X + H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R23""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 24,
#    label = "N_X + O_X <=> NO_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R24""",
#    longDesc = u"""Nitrogen/51"""
#    metal = "Cattype",
#)

#entry(
#    index = 25,
#    label = "N_X + O2_X <=> NO2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R25""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 26,
#    label = "N2_X + O_X <=> N2O_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R26""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 27,
#    label = "N2_X + OH_X <=> N2OH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R27""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 28,
#    label = "NO_X + O_X <=> NO2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R28""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 29,
#    label = "NO + X <=> NO_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R30""",
#    longDesc = u"""Surface_Adsorption_Single""",
#    metal = 'Cattype',
#)

#entry(
#    index = 30,
#    label = "NO2 + X <=> NO2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R31""",
#    longDesc = u"""Surface_Adsorption_Single""",
#    metal = 'Cattype',
#)

#entry(
#    index = 31,
#    label = "N2O + X <=> N2O_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R31""",
#    longDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 32,
#    label = "N2O + X <=> N2 + O_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R32""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#This reaction shows resonanceError
#entry(
#    index = 33,
#    label = "N2O + X + X <=> N_X + NO_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R33""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 34,
#    label = "N2O_X + X <=> N_X + NO_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),   
#        n = 0.0,
#        Ea = (, 'J/mol'), 
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R34""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 35,
#    label = "N2H4_X + X <=> NH2_X + NH2_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R35""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 36,
#    label = "N2H4_X + X <=> N2H3_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R36""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 37,
#    label = "N2H3_X + X <=> N2H2_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R37""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 38,
#    label = "N2H2_X + X <=> N2H_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R38""",
#    longDesc = u"""Surface_Dissociation_Beta""",
#    metal = "Cattype",
#)

#entry(
#    index = 39,
#    label = "N2H_X + X <=> N2_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R39""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 40,
#    label = "H_X + NO_X <=> HNO_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R40""",
#    longDesc = u"""Surface_Dissociation_Beta """,
#    metal = "Cattype",
#)

#entry(
#    index = 41,
#    label = "H_X + N_X + O_X <=> HNO_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  #maybe the unit is 'm^4/(mol*s)'
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R41""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 42,
#    label = "NHO + X <=> HNO_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R42""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 43,
#    label = "NHO2 + X <=> HNO2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R43""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 44,
#    label = "NHO3 + X <=> HNO3_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R44""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 45,
#    label = "NH2OH + X <=> NH2OH_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R45""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 46,
#    label = "NH2NO + X <=> NH2NO_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R46""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 47,
#    label = "NH2NO2 + X <=> NH2NO2_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R47""",
#    longDesc = u"""adsoprtion""",
#    metal = 'Cattype',
#)

#entry(
#    index = 48,
#    label = "H_X + H_X <=> H2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R1""",
#    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    metal = 'Cattype',
#)

#entry(
#    index = 49,
#    label = "N_X + N_X <=> N2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R2""",
#    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
#    metal = 'Cattype',
#)

#entry(
#    index = 50,
#    label = "O_X + O_X <=> O2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R3""",
#    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
#	metal = "Cattype",
#)

#entry(
#    index = 51,
#    label = "H2_X <=> H2 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R4""",
#    longDesc = u"""H2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 52,
#    label = "N2_X <=> N2 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R5""",
#    longDesc = u"""N2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 53,
#    label = "O2_X <=> O2 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R6""",
#    longDesc = u"""O2 Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 54,
#    label = "OH_X + X <=> H_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R7""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 55,
#    label = "H2O_X + X <=> H_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R8""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 56,
#    label = "H2O + X + X <=> H_X + OH_X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R9""",
#    longDesc = u"""Surface_Dissociation?""",
#    metal = "Cattype",
#)

#entry(
#    index = 57,
#    label = "H2O_X <=> H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R10""",
#    longDesc = u"""Surface_Adsorption""",
#	metal = "Cattype",
#)

#entry(
#    index = 58,
#    label = "NH3_X <=> NH3 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Cattype',
#)

#entry(
#    index = 59,
#    label = "NH2_X + H_X <=> NH3_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R12""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 60,
#    label = "NH_X + H_X <=> NH2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R13""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 61,
#    label = "N_X + H_X <=> NH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R14""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 62,
#    label = "NH2_X + OH_X <=> NH3_X +O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R15""",
#    longDesc = u"""Surface_Abstraction_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 63,
#    label = "NH_X + OH_X <=> NH2_X +O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R16""",
#    longDesc = u"""Surface_Abstraction""",
#    metal = "Cattype",
#)

#entry(
#    index = 64,
#    label = "N_X + OH_X <=> NH_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R17""",
#    longDesc = u"""Surface_Abstraction""",
#    metal = "Cattype",
#)

#entry(
#    index = 65,
#    label = "NH2_X + H2O_X <=> NH3_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R18""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 66,
#    label = "NH_X + H2O_X <=> NH2_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R19""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 67,
#    label = "N_X + H2O_X <=> NH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R20""",
#    longDesc = u"""Surface_Abstraction_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 68,
#    label = "NH2_X + H2O + X <=> NH3_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'm^5/(mol^2*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),   
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R21""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 69,
#    label = "NH_X + H2O + X <=> NH2_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'm^5/(mol^2*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R22""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 70,
#    label = "N_X + H2O + X <=> NH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'm^5/(mol^2*s)'), 
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R23""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 71,
#    label = "NO_X + X <=> N_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R24""",
#    longDesc = u"""Nitrogen/51"""
#    metal = "Cattype",
#)

#entry(
#    index = 72,
#    label = "NO2_X + X <=> N_X + O2_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R25""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 73,
#    label = "N2O_X + X <=> N2_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R26""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 74,
#    label = "N2OH_X + X <=> N2_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R27""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 75,
#    label = "NO2_X + X <=> NO_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R28""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 76,
#    label = "NO_X <=> NO + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R30""",
#    longDesc = u"""Surface_Adsorption_Single""",
#    metal = 'Cattype',
#)

#entry(
#    index = 77,
#    label = "NO2_X <=> NO2 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R31""",
#    longDesc = u"""Surface_Adsorption_Single""",
#    metal = 'Cattype',
#)

#entry(
#    index = 78,
#    label = "N2O_X <=> N2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R31""",
#    longDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
#    metal = 'Cattype',
#)

#entry(
#    index = 79,
#    label = "N2 + O_X <=> N2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R32""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#This reaction shows resonanceError
#entry(
#    index = 80,
#    label = "N_X + NO_X <=> N2O + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R33""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 81,
#    label = "N_X + NO_X <=> N2O_X + X,
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),   
#        n = 0.0,
#        Ea = (, 'J/mol'), 
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R34""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 82,
#    label = "NH2_X + NH2_X <=> N2H4_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R35""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 83,
#    label = "N2H3_X + H_X <=> N2H4_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R36""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 84,
#    label = "N2H2_X + H_X <=> N2H3_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R37""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Cattype",
#)

#entry(
#    index = 85,
#    label = "N2H_X + H_X <=> N2H2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R38""",
#    longDesc = u"""Surface_Dissociation_Beta""",
#    metal = "Cattype",
#)

#entry(
#    index = 86,
#    label = "N2_X + H_X <=> N2H_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R39""",
#    longDesc = u"""Surface_Addition_Single_vdW""",
#    metal = "Cattype",
#)

#entry(
#    index = 87,
#    label = "HNO_X + X <=> H_X + NO_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R40""",
#    longDesc = u"""Surface_Dissociation_Beta """,
#    metal = "Cattype",
#)

#entry(
#    index = 88,
#    label = "HNO_X + X <=> H_X + N_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R41""",
#    longDesc = u"""""",
#    metal = "Cattype",
#)

#entry(
#    index = 89,
#    label = "HNO_X <=> NHO + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R42""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 90,
#    label = "HNO2_X <=> NHO2 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R43""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 91,
#    label = "HNO3_X <=> NHO3 + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R44""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 92,
#    label = "NH2OH_X <=> NH2OH + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R45""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 93,
#    label = "NH2NO_X <=> NH2NO + X",
#    kinetics = SurfaceArrhenius(
#        A = (, '1/s'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R46""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 94,
#    label = "NH2NO2_X <=> NH2NO2 + X",
#    kinetics = StickingCoefficient(
#        A = ,
#        n = 0,
#        Ea = (, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R47""",
#    longDesc = u"""desorption""",
#    metal = 'Cattype',
#)

#entry(
#    index = 95,
#    label = "O_X + H2O_X <=> OH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R95""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 96,
#    label = "OH_X + OH_X <=> O_X + H2O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R95""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 97,
#    label = "HNO_X + X <=> NH_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R97""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 98,
#    label = "NH_X + O_X <=> HNO_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R97""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 99,
#    label = "NOH_X + X <=> N_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R99""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 100,
#    label = "N_X + OH_X <=> NOH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R99""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 101,
#    label = "HNOH_X + X <=> HNO_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R101""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 102,
#    label = "HNO_X + H_X <=> HNOH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R101""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 103,
#    label = "HNOH_X + X <=> NH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R103""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 104,
#    label = "NH_X + OH_X <=> HNOH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R103""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 105,
#    label = "HNOH_X + X <=> N_X + H2O_X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""R105""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)

#entry(
#    index = 106,
#    label = "N_X + H2O_X <=> HNOH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (, 'J/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Reverse R105""",
#    longDesc = u"""""",
#    metal = 'Cattype',
#)