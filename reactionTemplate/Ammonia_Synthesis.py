
entry(
    index = 1,
    label = " H2 + X + X <=> H_X + H_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""H adsorption""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 2,
    label = " N2 + X + X <=> N_X + N_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""N adsorption""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 3,
    label = " H2 + X <=> H2_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 4,
    label = " N2 + X <=> N2_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 5,
    label = " H2O + X <=> H2O_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
)

entry(
    index = 6,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = ,
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 7,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 8,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 9,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R1
entry(
    index = 10,
    label = " H_X + H_X  <=>  H2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (  , 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (  , 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""H desorption""",
    longDesc = u"""
""",
    metal = "Cattype" ,
)
#Reverse of R2
entry(
    index = 11,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (  , 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (  , 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Cattype" ,
)
#Reverse of R3
entry(
    index = 12,
    label = " H2_X <=>  H2  + X ",
    kinetics = SurfaceArrhenius(
        A = (  , 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (  , 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Cattype" ,
)
#Reverse of R4
entry(
    index = 13,
    label = " N2_X  <=>  N2 + X ",
    kinetics = SurfaceArrhenius(
        A = (  , 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (  , 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Cattype" ,
)
#Reverse of R5
entry(
    index = 14,
    label = " H2O_X  <=>  H2O + X ",
    kinetics = SurfaceArrhenius(
        A = (  , 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (  , 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Cattype" ,
)

#Reverse of R6
entry(
    index = 15,
    label = " NH3_X <=> NH3 + X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R7
entry(
    index = 16,
    label = " NH2_X + H_X <=> NH3_X + X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R8
entry(
    index = 17,
    label = " NH_X + H_X <=> NH2_X + X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R9
entry(
    index = 18,
    label = " N_X + H_X <=> NH_X + X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 19,
    label = " HNO_X <=> HNO + X ",
    kinetics = SurfaceArrhenius(
        A = (0, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 20,
    label = " HNO2_X <=> HNO2 + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 21,
    label = " HNO3_X <=> HNO3 + X ",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (14.71, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 22,
    label = " NH2OH_X <=> NH2OH + X ",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, '1/s'), 
        n = 0.0,
        Ea = (35.68, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 23,
    label = " NH2NO_X <=> NH2NO + X ",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, '1/s'), 
        n = 0.0,
        Ea = (25.43, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 24,
    label = " NH2NO2_X <=> NH2NO2 + X ",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, '1/s'), 
        n = 0.0,
        Ea = (25.69, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 25,
    label = "NO2_X  <=> NO2 + X",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, '1/s'),
        n = 0,
        Ea = (8.24, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R24 oxidation""",
    longDesc = u"""""",
    metal = 'Cattype',
)


#Reverse of R1
#entry(
#    index = 10,
#    label = " H_X + H_X  <=>  H2 + X + X ",
#    kinetics = SurfaceArrhenius(
#        A = (  , 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (  , 'kJ/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""H desorption""",
#    longDesc = u"""
#""",
#    metal = "Ru" ,
#)

#Reverse of R2
#entry(
#    index = 11,
#    label = " N_X + N_X  <=>  N2 + X + X ",
#    kinetics = SurfaceArrhenius(
#        A = (  , 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (  , 'kJ/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""N desorption""",
#    longDesc = u"""
#""",
#    metal = "Cattype" ,
#)


#Reverse of R6
#entry(
#    index = 15,
#    label = " NH3_X <=> NH3 + X ",
#    kinetics = SurfaceArrhenius(
#        A = (0, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""ammonia desorption""",
#    longDesc = u"""""",
#    metal = "Cattype" ,
#)

#Reverse of R7
#entry(
#    index = 16,
#    label = " NH2_X + H_X <=> NH3_X + X ",
#    kinetics = SurfaceArrhenius(
#        A = (0, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u"""""",
#    metal = "Cattype" ,
#)

#Reverse of R8
#entry(
#    index = 17,
#    label = " NH_X + H_X <=> NH2_X + X ",
#    kinetics = SurfaceArrhenius(
#        A = (0, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u"""""",
#    metal = "Cattype" ,
#)

#Reverse of R9
#entry(
#    index = 18,
#    label = " N_X + H_X <=> NH_X + X ",
#    kinetics = SurfaceArrhenius(
#        A = (0, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u"""""",
#    metal = "Cattype" ,
#)