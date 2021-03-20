#Why SurfaceArrhenius
entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^5/(mol^2*s)'),
        n = 0,
        Ea = ( , 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
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
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = ( , 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = ( , 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
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
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
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
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
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
    label = " NO_X <=> NO + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),   
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
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""""""
    metal = "Cattype" ,
)

entry(
    index = 10,
    label = " N_X + NO_X   <=>  N2O_X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
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
    index = 11,
    label = " N_X + NO_X   <=>  N2O + X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#similar to another 11 but only on vacant 
entry(
    index = 11,
    label = " N_X + NO_X   <=>  N2O_X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
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
    index = 12,
    label = " NO_X + NO_X   <=>  N2O + O_X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
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
    index = 13,
    label = " N2O_X <=>  N2O + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
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
    index = 14,
    label = " N2O + X <=>  N2 + O_X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),  
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
    index = 15,
    label = " O_X + O_X <=> O2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^5/(mol^2*s)'),
        n = 0,
        Ea = (, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Cattype",
)

#Reverse of R2
entry(
    index = 16,
    label = " NH2_X + OH_X <=> NH3_X + O_X  ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R3
entry(
    index = 17,
    label = " NH_X + OH_X <=> NH2_X + O_X  ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R4
entry(
    index = 18,
    label = " N_X + OH_X <=> NH_X + O_X  ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R5
entry(
    index = 19,
    label = " NH2_X + H2O_X <=> NH3_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Cattype" ,
)

#Reverse of R6
entry(
    index = 20,
    label = " NH_X + H2O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
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
    index = 21,
    label = " N_X + H2O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=( , 'm^2/(mol*s)'), 
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
    index = 22,
    label = " NO + X <=> NO_X ",
    kinetics = SurfaceArrhenius(
        A = (, 'm^2/(mol*s)'),   
        n = 0.0,
        Ea = (, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
)

#Reverse of R9
entry(
    index = 23,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
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
    index = 24,
    label = "NO2_X  <=> NO2 + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)