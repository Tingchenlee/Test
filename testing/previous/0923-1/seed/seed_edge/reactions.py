#!/usr/bin/env python
# encoding: utf-8

name = "seed_edge"
shortDesc = ""
longDesc = """

"""
autoGenerated=True
entry(
    index = 0,
    label = "X + NH3 <=> NH3_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=3.2189e+10, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Ammonia_Cu_SSZ_13
""",
)

entry(
    index = 1,
    label = "O + NO <=> NO2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.9229e+21,'m^2/(mol*s)'), n=0, Ea=(68,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Ammonia_Cu_SSZ_13
""",
)

entry(
    index = 2,
    label = "1_N4(T) <=> N2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
    Euclidian distance = 0
    family: 1,4_Linear_birad_scission"""),
    longDesc = 
"""
Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission
""",
)

entry(
    index = 3,
    label = "H + H2NN(T) <=> NNHJ + H2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.6e+08,'cm^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Matched reaction 85 H + H2N2 <=> H2 + HN2 in Disproportionation/training
    This reaction matched rate rule [H_rad;N3s/H2_s_Nbirad]
    family: Disproportionation"""),
    longDesc = 
"""
Matched reaction 85 H + H2N2 <=> H2 + HN2 in Disproportionation/training
This reaction matched rate rule [H_rad;N3s/H2_s_Nbirad]
family: Disproportionation
""",
)

entry(
    index = 4,
    label = "H + N2H2(T) <=> NNHJ + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+08,'cm^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Estimated using an average for rate rule [H_rad;NH_s_Rbirad]
    Euclidian distance = 0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using an average for rate rule [H_rad;NH_s_Rbirad]
Euclidian distance = 0
family: Disproportionation
""",
)

entry(
    index = 5,
    label = "NNHJ + NNHJ <=> NDNNDN",
    degeneracy = 0.5,
    kinetics = Arrhenius(A=(5.1562e+30,'m^3/(mol*s)'), n=-7.48856, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.354218852058, var=34.8187486739, Tref=1000.0, N=6, correlation='Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0
        Total Standard Deviation in ln(k): 12.7194203157
    Exact match found for rate rule [Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0]
    Euclidian distance = 0
    family: R_Recombination"""),
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 12.7194203157
Exact match found for rate rule [Root_N-1R->H_1CNOS->N_Ext-2R-R_3R!H-u0]
Euclidian distance = 0
family: R_Recombination
""",
)

entry(
    index = 6,
    label = "X + X + NDNNDN <=> [Pt]N=N + [Pt]N=N",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.01, n=0, Ea=(41.84,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
    Euclidian distance = 0
    family: Surface_Adsorption_Dissociative"""),
    longDesc = 
"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 7,
    label = "H + NH2NHJ <=> H2 + HNNH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.8e+08,'cm^3/(mol*s)'), n=1.5, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Matched reaction 91 H + H3N2 <=> H2 + H2N2-2 in Disproportionation/training
    This reaction matched rate rule [H_rad;N3s/H2_s_Nrad]
    family: Disproportionation"""),
    longDesc = 
"""
Matched reaction 91 H + H3N2 <=> H2 + H2N2-2 in Disproportionation/training
This reaction matched rate rule [H_rad;N3s/H2_s_Nrad]
family: Disproportionation
""",
)

entry(
    index = 8,
    label = "[NH]NN=[N] <=> N2 + HNNH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
    Euclidian distance = 0
    family: 1,4_Linear_birad_scission"""),
    longDesc = 
"""
Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission
""",
)

entry(
    index = 9,
    label = "H + HNNH <=> NH2NHJ",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.982e+35,'cm^3/(mol*s)'), n=-7.67, Ea=(52.551,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Matched reaction 2841 H + H2N2 <=> H3N2 in R_Addition_MultipleBond/training
    This reaction matched rate rule [N3d-H_N3d-H;HJ]
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Matched reaction 2841 H + H2N2 <=> H3N2 in R_Addition_MultipleBond/training
This reaction matched rate rule [N3d-H_N3d-H;HJ]
family: R_Addition_MultipleBond
""",
)

entry(
    index = 10,
    label = "NNHJ + H2NN(T) <=> NNHJ + HNNH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.6e+06,'cm^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Estimated using template [N3_rad;N3s/H2_s_Nbirad] for rate rule [N3d_rad/N;N3s/H2_s_Nbirad]
    Euclidian distance = 2.0
    Multiplied by reaction path degeneracy 2.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [N3_rad;N3s/H2_s_Nbirad] for rate rule [N3d_rad/N;N3s/H2_s_Nbirad]
Euclidian distance = 2.0
Multiplied by reaction path degeneracy 2.0
family: Disproportionation
""",
)

entry(
    index = 11,
    label = "NNHJ + HNNH <=> [NH]NNDN",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.982e+35,'cm^3/(mol*s)'), n=-7.67, Ea=(52.551,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Estimated using template [N3d-H_N3d-H;YJ] for rate rule [N3d-H_N3d-H;N3dJ_N]
    Euclidian distance = 4.0
    Multiplied by reaction path degeneracy 2.0
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Estimated using template [N3d-H_N3d-H;YJ] for rate rule [N3d-H_N3d-H;N3dJ_N]
Euclidian distance = 4.0
Multiplied by reaction path degeneracy 2.0
family: R_Addition_MultipleBond
""",
)

entry(
    index = 12,
    label = "NNHJ + N2H2(T) <=> NNHJ + HNNH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [N3_rad;NH_s_Rbirad] for rate rule [N3d_rad/N;NH_s_Rbirad]
    Euclidian distance = 2.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [N3_rad;NH_s_Rbirad] for rate rule [N3d_rad/N;NH_s_Rbirad]
Euclidian distance = 2.0
family: Disproportionation
""",
)

entry(
    index = 13,
    label = "[NH]NN[NH] <=> HNNH + HNNH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
    Euclidian distance = 0
    family: 1,4_Linear_birad_scission"""),
    longDesc = 
"""
Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission
""",
)

entry(
    index = 14,
    label = "NNHJ + NH2NHJ <=> HNNH + HNNH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(920000,'cm^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Estimated using template [N3_rad;N3s/H2_s_Nrad] for rate rule [N3d_rad/N;N3s/H2_s_Nrad]
    Euclidian distance = 2.0
    Multiplied by reaction path degeneracy 2.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [N3_rad;N3s/H2_s_Nrad] for rate rule [N3d_rad/N;N3s/H2_s_Nrad]
Euclidian distance = 2.0
Multiplied by reaction path degeneracy 2.0
family: Disproportionation
""",
)

entry(
    index = 15,
    label = "H + H3N2 <=> H2 + NNH2(S)",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1075.54,'m^3/(mol*s)'), n=1.5, Ea=(0.934427,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [H_rad;NH_s_Rrad] for rate rule [H_rad;N5H_s_Rrad]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 3.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [H_rad;NH_s_Rrad] for rate rule [H_rad;N5H_s_Rrad]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 3.0
family: Disproportionation
""",
)

entry(
    index = 16,
    label = "H + NH2NHJ <=> H2 + NNH2(S)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(358.512,'m^3/(mol*s)'), n=1.5, Ea=(0.934427,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [H_rad;NH_s_Rrad]
    Euclidian distance = 0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using an average for rate rule [H_rad;NH_s_Rrad]
Euclidian distance = 0
family: Disproportionation
""",
)

entry(
    index = 17,
    label = "H + NNH2(S) <=> H3N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.89174e+09,'m^3/(mol*s)'), n=-1.15717, Ea=(21.4703,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R_R;HJ]
    Euclidian distance = 0
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Estimated using an average for rate rule [R_R;HJ]
Euclidian distance = 0
family: R_Addition_MultipleBond
""",
)

entry(
    index = 18,
    label = "H + NNH2(S) <=> NH2NHJ",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.88497e+29,'m^3/(mol*s)'), n=-8.04, Ea=(52.3,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Nd_R;HJ] for rate rule [N1dc_R;HJ]
    Euclidian distance = 1.0
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Estimated using template [Nd_R;HJ] for rate rule [N1dc_R;HJ]
Euclidian distance = 1.0
family: R_Addition_MultipleBond
""",
)

entry(
    index = 19,
    label = "NNHJ + H2NN(T) <=> NNHJ + NNH2(S)",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.2e+06,'cm^3/(mol*s)'), n=1.87, Ea=(0.54392,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Estimated using template [Y_rad;N3s/H2_s_Nbirad] for rate rule [N5_rad;N3s/H2_s_Nbirad]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 2.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [Y_rad;N3s/H2_s_Nbirad] for rate rule [N5_rad;N3s/H2_s_Nbirad]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Disproportionation
""",
)

entry(
    index = 20,
    label = "NNHJ + NNH2(S) <=> H3N4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000614,'m^3/(mol*s)'), n=2.756, Ea=(6.93707,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R_R;N3J] for rate rule [N1dc_R;N3dJ_N]
    Euclidian distance = 2.8284271247461903
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Estimated using template [R_R;N3J] for rate rule [N1dc_R;N3dJ_N]
Euclidian distance = 2.8284271247461903
family: R_Addition_MultipleBond
""",
)

entry(
    index = 21,
    label = "NNHJ + N2H2(T) <=> NNHJ + NNH2(S)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.98203,'m^3/(mol*s)'), n=1.92742, Ea=(-4.70733,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Y_rad;NH_s_Rbirad] for rate rule [N5_rad;NH_s_Rbirad]
    Euclidian distance = 1.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [Y_rad;NH_s_Rbirad] for rate rule [N5_rad;NH_s_Rbirad]
Euclidian distance = 1.0
family: Disproportionation
""",
)

entry(
    index = 22,
    label = "NNHJ + NNH2(S) <=> H3N4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.88497e+29,'m^3/(mol*s)'), n=-8.04, Ea=(52.3,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Nd_R;YJ] for rate rule [N1dc_R;NJ]
    Euclidian distance = 1.4142135623730951
    family: R_Addition_MultipleBond"""),
    longDesc = 
"""
Estimated using template [Nd_R;YJ] for rate rule [N1dc_R;NJ]
Euclidian distance = 1.4142135623730951
family: R_Addition_MultipleBond
""",
)

entry(
    index = 23,
    label = "NNHJ + H3N2 <=> HNNH + NNH2(S)",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(0.338605,'m^3/(mol*s)'), n=2.315, Ea=(-5.77392,'kJ/mol'), T0=(1,'K'), comment="""Estimated using average of templates [N3_rad;NH_s_Rrad] + [N3d_rad;XH_s_Rrad] for rate rule [N3d_rad/N;N5H_s_Rrad]
    Euclidian distance = 2.23606797749979
    Multiplied by reaction path degeneracy 3.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using average of templates [N3_rad;NH_s_Rrad] + [N3d_rad;XH_s_Rrad] for rate rule [N3d_rad/N;N5H_s_Rrad]
Euclidian distance = 2.23606797749979
Multiplied by reaction path degeneracy 3.0
family: Disproportionation
""",
)

entry(
    index = 24,
    label = "NNHJ + NH2NHJ <=> HNNH + NNH2(S)",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(0.014,'m^3/(mol*s)'), n=2.69, Ea=(26.4681,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [N3d_rad;XH_s_Rrad] for rate rule [N3d_rad/N;NH_s_Rrad]
    Euclidian distance = 1.4142135623730951
    family: Disproportionation
    Ea raised from -6.7 to 26.5 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using template [N3d_rad;XH_s_Rrad] for rate rule [N3d_rad/N;NH_s_Rrad]
Euclidian distance = 1.4142135623730951
family: Disproportionation
Ea raised from -6.7 to 26.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 25,
    label = "NNHJ + NH2NHJ <=> HNNH + NNH2(S)",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = Arrhenius(A=(1.64e+06,'cm^3/(mol*s)'), n=1.87, Ea=(26.4681,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K'), comment="""Estimated using template [Y_rad;N3s/H2_s_Nrad] for rate rule [N5_rad;N3s/H2_s_Nrad]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 2.0
    family: Disproportionation
    Ea raised from 25.7 to 26.5 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using template [Y_rad;N3s/H2_s_Nrad] for rate rule [N5_rad;N3s/H2_s_Nrad]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Disproportionation
Ea raised from 25.7 to 26.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 26,
    label = "NNHJ + H3N2 <=> NNH2(S) + NNH2(S)",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(12.8623,'m^3/(mol*s)'), n=1.9216, Ea=(-2.95768,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Y_rad;NH_s_Rrad] for rate rule [N5_rad;N5H_s_Rrad]
    Euclidian distance = 1.4142135623730951
    Multiplied by reaction path degeneracy 3.0
    family: Disproportionation"""),
    longDesc = 
"""
Estimated using template [Y_rad;NH_s_Rrad] for rate rule [N5_rad;N5H_s_Rrad]
Euclidian distance = 1.4142135623730951
Multiplied by reaction path degeneracy 3.0
family: Disproportionation
""",
)

entry(
    index = 27,
    label = "NNHJ + NH2NHJ <=> NNH2(S) + NNH2(S)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.28744,'m^3/(mol*s)'), n=1.9216, Ea=(126.921,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Y_rad;NH_s_Rrad] for rate rule [N5_rad;NH_s_Rrad]
    Euclidian distance = 1.0
    family: Disproportionation
    Ea raised from -3.0 to 126.9 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using template [Y_rad;NH_s_Rrad] for rate rule [N5_rad;NH_s_Rrad]
Euclidian distance = 1.0
family: Disproportionation
Ea raised from -3.0 to 126.9 kJ/mol to match endothermicity of reaction.
""",
)

