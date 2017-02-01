# CIDOC CRM 5.0.2

class E1(object):
    "E1 CRM Entity"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p1 = P1()
        self.p2 = P2()
        self.p3 = P3()
        self.p48 = P48()
        self.p137 = P137()
        
        ### Reverse CIDOC CRM properties
        self.p15b = P15()
        self.p17b = P17()
        self.p39b = P39()
        self.p41b = P41()
        self.p62b = P62()
        self.p67b = P67()
        self.p70b = P70()
        self.p129b = P129()
        self.p136b = P136()
        self.p138b = P138()
        self.p140b = P140()
        self.p141b = P141()
        
    def crm_fproperties(self):
        return (self.p1, self.p2, self.p3, self.p48, self.p137)
    def crm_rproperties(self):
        return (self.p15b, self.p17b, self.p39b, self.p41b, self.p62b, self.p67b, self.p70b, self.p129b, self.p136b, self.p138b, self.p140b, self.p141b)
    def __str__(self):
        return "E1 CRM Entity"
    
class E2(E1):
    "E2 Temporal Entity"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p4 = P4()
        self.p114 = P114() # symmetric, homonymic
        self.p115 = P115() # symmetric
        self.p116 = P116() # symmetric
        self.p117 = P117() # symmetric
        self.p118 = P118() # symmetric
        self.p119 = P119() # symmetric
        self.p120 = P120() # symmetric
        
        # Reverse CIDO CRM properties
        self.p114b = P114() # symmetric, homonymic
        self.p115b = P115() # symmetric
        self.p116b = P116() # symmetric
        self.p117b = P117() # symmetric
        self.p118b = P118() # symmetric
        self.p119b = P119() # symmetric
        self.p120b = P120() # symmetric
        
    def crm_fproperties(self):
        return (self.p4, self.p114, self.p115, self.p116, self.p117, self.p118, self.p119, self.p120)
    def crm_rproperties(self):
        return(self.p114b, self.p115b, self.p116b, self.p117b, self.p118b, self.p119b, self.p120b)
    def __str__(self):
        return "E2 Temporal Entity"

class E3(E2):
    "E3 Condition State"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p5 = P5() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p5b = P5() # symmetric
        self.p35b = P35()
        self.p44b = P44()
        
    def crm_fproperties(self):
        return (self.p5,)
    def crm_rproperties(self):
        return (self.p5b, self.p35b, self.p44b)
    def __str__(self):
        return "E3 Condition State"

class E4(E2):
    "E4 Period"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p7 = P7()
        self.p8 = P8()
        self.p9 = P9() # symmetric
        self.p10 = P10() # symmetric
        self.p132 = P132() # symmetric, homonymic
        self.p133 = P133() # symmetric, homonymic
        
        ### Reverse CIDOC CRM properties
        self.p9b = P9() # symmetric
        self.p10b = P10() # symmetric
        self.p132b = P132() # symmetric, homonymic
        self.p133b = P133() # symmetric, homonymic
        
    def crm_fproperties(self):
        return (self.p7, self.p8, self.p9, self.p10, self.p132, self.p133)
    def crm_rproperties(self):
        return (self.p9b, self.p10b, self.p132b, self.p133b)
    def __str__(self):
        return "E4 Period"

class E5(E4):
    "E5 Event"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p11 = P11()
        self.p12 = P12()
        
        ### Reverse CIDOC CRM properties
        self.p20b = P20()
        
    def crm_fproperties(self):
        return (self.p11, self.p12)
    def crm_rproperties(self):
        return (self.p20b,)
    def __str__(self):
        return "E5 Event"

class E64(E5):
    "E64 End of Existence"
    def __init__(self):
        self.p93 = P93()
    def crm_fproperties(self):
        return (self.p93,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E64 End of Existence"

class E6(E64):
    "E6 Destruction"
    def __init__(self):
        self.p13 = P13()
    def crm_fproperties(self):
        return (self.p13,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E5 Event"

class E7(E5):
    "E7 Activity"    
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p14 = P14()
        self.p15 = P15()
        self.p16 = P16()
        self.p19 = P19()
        self.p20 = P20()
        self.p21 = P21()
        self.p32 = P32()
        self.p33 = P33()
        self.p125 = P125()
        self.p134 = P134() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p134b = P134() # symmetric
        
    def crm_fproperties(self):
        return (self.p14, self.p15, self.p16, self.p19, self.p20, self.p21, self.p32, self.p33, self.p125, self.p134)
    def crm_rproperties(self):
        return (self.p134b,)
    def __str__(self):
        return "E7 Activity"

class E8(E7):
    "E8 Acquisition"
    def __init__(self):
        self.p22 = P22()
        self.p23 = P23()
        self.p24 = P24()
    def crm_fproperties(self):
        return (self.p22, self.p23, self.p24)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E8 Acquisition"

class E9(E7):
    "E9 Move"
    def __init__(self):
        self.p25 = P25()
        self.p26 = P26()
        self.p27 = P27()
    def crm_fproperties(self):
        return (self.p25, self.p26, self.p27)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E10 Move"

class E10(E7):
    "E10 Transfer of Custody"
    def __init__(self):
        self.p28 = P28()
        self.p29 = P29()
        self.p30 = P30()
    def crm_fproperties(self):
        return (self.p28, self.p29, self.p30)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E10 Transfer of Custody"

class E11(E7):
    "E11 Modification"
    def __init__(self):
        self.p31 = P31()
        self.p126 = P126()
    def crm_fproperties(self):
        return (self.p31, self.p126)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E11 Modification"

class E63(E5):
    "E63 Beginning of Existence"
    def __init__(self):
        self.p92 = P92()
    def crm_fproperties(self):
        return (self.p92,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E63 Beginning of Existence"

class E12(E11, E63):
    "E12 Production"
    def __init__(self):
        self.p108 = P108()
    def crm_fproperties(self):
        return (self.p108,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E12 Production"

class E13(E7):
    "E13 Attribute Assignment"
    def __init__(self):
        self.p140 = P140()
        self.p141 = P141()
    def crm_fproperties(self):
        return (self.p140, self.p141)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E13 Attribute Assignment"

class E14(E13):
    "E14 Condition Assessment"
    def __init__(self):
        self.p34 = P34()
        self.p35 = P35()
    def crm_fproperties(self):
        return (self.p34, self.p35)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E14 Condition Assessment"

class E15(E13):
    "E15 Identifier Assignment"
    def __init__(self):
        self.p37 = P37()
        self.p38 = P38()
        self.p142 = P142()
    def crm_fproperties(self):
        return (self.p37, self.p38, self.p142)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E15 Identifier Assignment"

class E16(E13):
    "E16 Measurement"
    def __init__(self):
        self.p39 = P39()
        self.p40 = P40()
    def crm_fproperties(self):
        return (self.p39, self.p40)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E16 Measurement"

class E17(E13):
    "E17 Type Assignment"
    def __init__(self):
        self.p41 = P41()
        self.p42 = P42()
    def crm_fproperties(self):
        return (self.p41, self.p42)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E17 Type Assignment"

class E77(E1):
    "E77 Persistent Item"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E77 Persistent Item"
    
class E70(E77):
    "E70 Thing"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p43 = P43()
        self.p101 = P101()
        self.p130 = P130() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p16b = P16()
        self.p130b = P130() # symmetric
        
    def crm_fproperties(self):
        return (self.p43, self.p101, self.p130)
    def crm_rproperties(self):
        return (self.p16b, self.p130b)
    def __str__(self):
        return "E70 Thing"

class E72(E70):
    "E72 Legal Object"
    def __init__(self):
        self.p104 = P104()
        self.p105 = P105()
    def crm_fproperties(self):
        return (self.p104, self.p105)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E72 Legal Object"

class E18(E72):
    "E18 Physical Thing"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p44 = P44()
        self.p45 = P45()
        self.p46 = P46()
        self.p49 = P49()
        self.p50 = P50()
        self.p51 = P51()
        self.p52 = P52()
        self.p53 = P53()
        self.p58 = P58()
        self.p59 = P59()
        
        ### Reverse CIDOC CRM properties
        self.p13b = P13()
        self.p24b = P24()
        self.p30b = P30()
        self.p34b = P34()
        self.p46b = P46()
        self.p111b = P111()
        self.p113b = P113()
        
    def crm_fproperties(self):
        return (self.p44, self.p45, self.p46, self.p49, self.p50, self.p51, self.p52, self.p53, self.p58, self.p59)
    def crm_rproperties(self):
        return (self.p13b, self.p24b, self.p30b, self.p34b, self.p46b, self.p111b, self.p113b)
    def __str__(self):
        return "E18 Physical Thing"

class E19(E18):
    "E19 Physical Object"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p54 = P54()
        self.p55 = P55()
        self.p56 = P56()
        self.p57 = P57()
        
        ### Reverse CIDOC CRM properties   
        self.p8b = P8()
        self.p25b = P25()
        
    def crm_fproperties(self):
        return (self.p54, self.p55, self.p56, self.p57)
    def crm_rproperties(self):
        return (self.p8b, self.p25b)
    def __str__(self):
        return "E19 Physical Object"

class E20(E19):
    "E20 Biological Object"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E20 Biological Object"
    
class E39(E77):
    "E39 Actor"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p74 = P74()
        self.p75 = P75()
        self.p76 = P76()
        self.p131 = P131()
        
        ### Reverse CIDOC CRM properties
        self.p11b = P11()
        self.p14b = P14()
        self.p22b = P22()
        self.p23b = P23()
        self.p28b = P28()
        self.p29b = P29()
        self.p49b = P49()
        self.p50b = P50()
        self.p51b = P51()
        self.p52b = P52()
        self.p105b = P105()
        self.p107b = P107()
        self.p109b = P109()
        self.p143b = P143()
        self.p145b = P145()
        
    def crm_fproperties(self):
        return (self.p74, self.p75, self.p76, self.p131)
    def crm_rproperties(self):
        return (self.p11b, self.p14b, self.p22b, self.p23b, self.p28b, self.p29b, self.p49b, self.p50b, self.p51b, self.p52b, self.p105b, self.p107b, self.p109b, self.p143b, self.p145b)
    def __str__(self):
        return "E39 Actor"

class E21(E20, E39):
    "E21 Person"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p96b = P96()
        self.p97b = P97()
        self.p98b = P98()
        self.p100b = P100()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p96b, self.p97b, self.p98b, self.p100b)
    def __str__(self):
        return "E21 Person"

class E71(E70):
    "E71 Man-Made Thing"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p102 = P102()
        self.p103 = P103()
        
        ### Reverse CIDOC CRM properties
        self.p19b = P19()
        
    def crm_fproperties(self):
        return (self.p102, self.p103)
    def crm_rproperties(self):
        return (self.p19b,)
    def __str__(self):
        return "E71 Man-Made Thing"

class E24(E18, E71):
    "E24 Physical Man-Made Thing"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p62 = P62()
        self.p65 = P65()
        self.p128 = P128()
        
        ### Reverse CIDOC CRM properties
        self.p31b = P31()
        self.p108b = P108()
        self.p110b = P110()
        self.p112b = P112()
        
    def crm_fproperties(self):
        return (self.p62, self.p65, self.p128)
    def crm_rproperties(self):
        return (self.p31b, self.p108b, self.p110b, self.p112b)
    def __str__(self):
        return "E24 Physical Man-Made Thing"

class E22(E19, E24):
    "Man-Made Object"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "Man-Made Object"
    
class E26(E18):
    "E26 Physical Feature"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p56b = P56()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p56b,)
    def __str__(self):
        return "E26 Physical Feature"

class E25(E24, E26):
    "Man-Made Feature"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "Man-Made Feature"
    
class E22(E19, E24):
    "E22 Man-Made Object"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E22 Man-Made Object"
        
class E25(E24, E26):
    "E25 Man-Made Feature"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E25 Man-Made Feature"

class E27(E26):
    "E27 Site"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E27 Site"
    
class E28(E71):
    "E28 Conceptual Object"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p94b = P94()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p94b,)
    def __str__(self):
        return "E28 Conceptual Object"

class E89(E28):
    "E89 Propositional Object"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p67 = P67()
        self.p129 = P129()
        self.p148 = P148() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p148b = P148() # symmetric
        
    def crm_fproperties(self):
        return (self.p67, self.p129, self.p148)
    def crm_rproperties(self):
        return (self.p148b,)
    def __str__(self):
        return "E89 Propositional Object"

class E90(E28, E72):
    "E90 Symbolic Object"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p106 = P106() # symmetric
        
        ### Forward CIDOC CRM properties
        self.p106b = P106() # symmetric
        
    def crm_fproperties(self):
        return (self.p106,)
    def crm_rproperties(self):
        return (self.p106b,)
    def __str__(self):
        return "E90 Symbolic Object"

class E73(E89, E90):
    "E73 Information Object"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p128b = P128()
    
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p128b,)
    def __str__(self):
        return "E73 Information Object"

class E29(E73):
    "Design or Procedure"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p68 = P68()
        self.p69 = P69() # symmetric, homonymic
        
        ### Reverse CIDOC CRM properties
        self.p33b = P33()
        self.p69b = P69() # symmetric, homonymic
        
    def crm_fproperties(self):
        return (self.p68, self.p69)
    def crm_rproperties(self):
        return (self.p33b, self.p69b)
    def __str__(self):
        return "Design or Procedure"

class E30(E89):
    "Right"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p75b = P75()
        self.p104b = P104()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p75b, self.p104b)
    def __str__(self):
        return "Right"

class E31(E73):
    "Document"
    def __init__(self):
        self.p70 = P70()
    def crm_fproperties(self):
        return (self.p70,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "Document"

class E32(E31):
    "Authority Document"
    def __init__(self):
        self.p71 = P71()
    def crm_fproperties(self):
        return (self.p71,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "Authority Document"    
    
class E29(E73):
    "E29 Design or Procedure"
    def __init__(self):
        self.p68 = P68()
        self.p69 = P69()
    def crm_fproperties(self):
        return (self.p68, self.p69)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E29 Design or Procedure"

class E30(E89):
    "E30 Right"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E30 Right"

class E31(E73):
    "E31 Document"
    def __init__(self):
        self.p70 = P70()
    def crm_fproperties(self):
        return (self.p70,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E31 Document"
    
class E32(E31):
    "E32 Authority Document"
    def __init__(self):
        self.p71 = P71()
    def crm_fproperties(self):
        return (self.p71,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E32 Authority Document"
    
class E33(E73):
    "E33 Linguistic Object"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p72 = P72()
        self.p73 = P73() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p73b = P73() # symmetric
        
    def crm_fproperties(self):
        return (self.p72, self.p73)
    def crm_rproperties(self):
        return (self.p73b,)
    def __str__(self):
        return "E33 Linguistic Object"
    
class E34(E33):
    "E34 Inscription"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E34 Inscription"
    
class E41(E90):
    "E41 Appellation"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p139 = P139() # symmetric, homonymic
        
        ### Reverse CIDOC CRM properties
        self.p1b = P1()
        self.p139b = P139() # symmetric, homonymic
        self.p142b = P142()
        
    def crm_fproperties(self):
        return (self.p139,)
    def crm_rproperties(self):
        return (self.p1b, self.p139b, self.p142b)
    def __str__(self):
        return "E41 Appellation"

class E35(E33, E41):
    "E35 Title"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p102b = P102()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p102b,)
    def __str__(self):
        return "E35 Title"

class E36(E73):
    "E36 Visual Item"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p138 = P138()
        
        ### Reverse CIDOC CRM properties
        self.p65b = P65()
        
    def crm_fproperties(self):
        return (self.p138,)
    def crm_rproperties(self):
        return (self.p65b,)
    def __str__(self):
        return "E36 Visual Item"

class E37(E36):
    "E37 Mark"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E37 Mark"
    
class E38(E36):
    "E38 Image"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E38 Image"

class E74(E39):
    "E74 Group"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p107 = P107()
        
        ### Reverse CIDOC CRM properties
        self.p95b = P95()
        self.p99b = P99()
        self.p144b = P144()
        self.p146b = P146()  
        
    def crm_fproperties(self):
        return (self.p107,)
    def crm_rproperties(self):
        return (self.p95b, self.p99b, self.p144b, self.p146b)
    def __str__(self):
        return "E74 Group"

class E40(E74):
    "E40 Legal Body"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E40 Legal Body"

class E42(E41):
    "E42 Identifier"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p48b = P48()
        self.p37b = P37()
        self.p38b = P38()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p48b, self.p37b, self.p38b)
    def __str__(self):
        return "E42 Identifier"
    
class E44(E41):
    "E44 Place Appellation"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p87b = P87()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p87b,)
    def __str__(self):
        return "E44 Place Appellation"
    
class E51(E41):
    "E51 Contact Point"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p76b = P76()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p76b,)
    def __str__(self):
        return "E51 Contact Point"

class E77(E1):
    "E77 Persistent Item"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p12b = P12()
        self.p92b = P92()
        self.p93b = P93()
        self.p123b = P123()
        self.p124b = P124()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p12b, self.p92b, self.p93b, self.p123b, self.p124b)
    def __str__(self):
        return "E77 Persistent Item"

class E45(E44, E51):
    "E45 Address"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E45 Address"

class E46(E44):
    "E46 Section Definition"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p58b = P58()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p58b,)
    def __str__(self):
        return "E46 Section Definition"
    
class E47(E44):
    "E47 Spatial Coordinates"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E47 Spatial Coordinates"

class E48(E44):
    "E48 Place Name"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E48 Place Name"

class E49(E41):
    "E49 Time Appellation"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p78b = P78()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p78b,)
    def __str__(self):
        return "E49 Time Appellation"

class E50(E49):
    "E50 Date"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E50 Date"
    
class E52(E1):
    "E52 Time-Span"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p78 = P78()
        self.p79 = P79()
        self.p80 = P80()
        self.p81 = P81()
        self.p82 = P82()
        self.p83 = P83()
        self.p84 = P84()
        self.p86 = P86() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p4b = P4()
        self.p86b = P86() # symmetric
        
    def crm_fproperties(self):
        return (self.p78, self.p79, self.p80, self.p81, self.p82, self.p83, self.p84, self.p86)
    def crm_rproperties(self):
        return (self.p4b, self.p86b)
    def __str__(self):
        return "E52 Time-Span"

class E53(E1):
    "E53 Place"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p87 = P87()
        self.p88 = P88() # symmetric
        self.p89 = P89() # symmetric
        self.p121 = P121() # symmetric, homonymic
        self.p122 = P122() # symmetric, homonymic
        
        ### Reverse CIDOC CRM properties
        self.p7b = P7()
        self.p26b = P26()
        self.p27b = P27()
        self.p53b = P53()
        self.p54b = P54()
        self.p55b = P55()
        self.p59b = P59()
        self.p74b = P74()
        self.p88b = P88() # symmetric
        self.p89b = P89() # symmetric
        self.p121b = P121() # symmetric, homonymic
        self.p122b = P122() # symmetric, homonymic
        
    def crm_fproperties(self):
        return (self.p87, self.p88, self.p89, self.p121, self.p122)
    def crm_rproperties(self):
        return (self.p7b, self.p26b, self.p27b, self.p53b, self.p54b, self.p55b, self.p59b, self.p74b, self.p88b, self.p89b, self.p121b, self.p122b)
    def __str__(self):
        return "E53 Place"

class E54(E1):
    "E54 Dimension"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p90 = P90()
        self.p91 = P91()
        
        ### Reverse CIDOC CRM properties
        self.p40b = P40()
        self.p43b = P43()
        self.p83b = P83()
        self.p84b = P84()
        
    def crm_fproperties(self):
        return (self.p90, self.p91)
    def crm_rproperties(self):
        return (self.p40b, self.p43b, self.p83b, self.p84b)
    def __str__(self):
        return "E54 Dimension"
    
class E55(E28):
    "E55 Type"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p127 = P127() # symmetric
        
        ### Reverse CIDOC CRM properties
        self.p2b = P2()
        self.p21b = P21()
        self.p32b = P32()
        self.p42b = P42()
        self.p71b = P71()
        self.p101b = P101()
        self.p103 = P103()
        self.p125 = P125()
        self.p127b = P127() # symmetric
        self.p135b = P135()
        self.p137b = P137()
        
    def crm_fproperties(self):
        return (self.p127,)
    def crm_rproperties(self):
        return (self.p2b, self.p21b, self.p32b, self.p42b, self.p71b, self.p101b, self.p103, self.p125, self.p127b, self.p135b, self.p137b)
    def __str__(self):
        return "E55 Type"

class E56(E55):
    "E56 Language"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p72b = P72()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p72b,)
    def __str__(self):
        return "E56 Language"

class E57(E55):
    "E57 Material"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p45b = P45()
        self.p68b = P68()    
        self.p126b = P126()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p45b, self.p68b, self.p126b)
    def __str__(self):
        return "E57 Material"

class E58(E55):
    "E58 Measurement Unit"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p91b = P91()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p91b,)
    def __str__(self):
        return "E58 Measurement Unit"

class E59(object):
    "E59 Primitive Value"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E59 Primitive Value"
    
class E60(E59):
    "E60 Number"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p57b = P57()
        self.p90b = P90()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p57b, self.p90b)
    def __str__(self):
        return "E60 Number"

class E61(E59):
    "E61 Time Primitive"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p81b = P81()
        self.p82b = P82()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p81b, self.p82b)
    def __str__(self):
        return "E61 Time Primitive"

class E62(E59):
    "E62 String"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p3b = P3()
        self.p79b = P79()
        self.p80b = P80()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p3b, self.p79b, self.p80b)
    def __str__(self):
        return "E62 String"

class E65(E7, E63):
    "E65 Creation"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p94 = P94()
        
    def crm_fproperties(self):
        return (self.p94,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E65 Creation"
    
class E66(E7, E63):
    "E66 Formation"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p95 = P95()
        
    def crm_fproperties(self):
        return (self.p95,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E66 Formation"
    
class E67(E63):
    "E67 Birth"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p96 = P96()
        self.p97 = P97()
        self.p98 = P98()
        
    def crm_fproperties(self):
        return (self.p96, self.p97, self.p98)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E67 Birth"
    
class E68(E64):
    "E68 Dissolution"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p99 = P99()
        
    def crm_fproperties(self):
        return (self.p99,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E68 Dissolution"
    
class E69(E64):
    "E69 Death"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p100 = P100()
        
    def crm_fproperties(self):
        return (self.p100,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E69 Death"
            
class E75(E41):
    "E75 Conceptual Object Appellation"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E75 Conceptual Object Appellation"
    
class E78(E24):
    "E78 Collection"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p109 = P109()
        
        ### Reverse CIDOC CRM properties
        self.p147b = P147()
        
    def crm_fproperties(self):
        return (self.p109,)
    def crm_rproperties(self):
        return (self.p147b,)
    def __str__(self):
        return "E78 Collection"

class E79(E11):
    "E79 Part Addition"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p110 = P110()
        self.p111 = P111()
        
    def crm_fproperties(self):
        return (self.p110, self.p111)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E79 Part Addition"
    
class E80(E11):
    "E80 Part Removal"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p112 = P112()
        self.p113 = P113()
        
    def crm_fproperties(self):
        return (self.p112, self.p113)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E80 Part Removal"
    
class E81(E63, E64):
    "E81 Transformation"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p123 = P123()
        self.p124 = P124()
        
    def crm_fproperties(self):
        return (self.p123, self.p124)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E81 Transformation"
    
class E82(E41):
    "E82 Actor Appellation"
    def __init__(self):
        
        ### Reverse CIDOC CRM properties
        self.p131b = P131()
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return (self.p131b,)
    def __str__(self):
        return "E82 Actor Appellation"

class E83(E65):
    "E83 Type Creation"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p135 = P135()
        self.p136 = P136()
        
    def crm_fproperties(self):
        return (self.p135, self.p136)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E83 Type Creation"
    
class E84(E22):
    "E84 Information Carrier"
    def __init__(self):
        pass
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E84 Information Carrier"
    
class E85(E7):
    "E85 Joining"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p143 = P143()
        self.p144 = P144()
        
    def crm_fproperties(self):
        return (self.p143, self.p144)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E85 Joining"
    
class E86(E7):
    "E86 Leaving"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p145 = P145()
        self.p146 = P146()
        
    def crm_fproperties(self):
        return (self.p145, self.p146)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E86 Leaving"
    
class E87(E7):
    "E87 Curation Activity"
    def __init__(self):
        
        ### Forward CIDOC CRM properties
        self.p147 = P147()
        
    def crm_fproperties(self):
        return (self.p147,)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "E87 Curation Activity"

### PROPERTIES

class P1(object):
    "P1 is identified by (identifies)"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E41 # E41 Appellation
        self.flabel = "P1 is identified by"
        self.rlabel = "P1B identifies"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P1 is identified by (identifies)"
                         
class P2(object):
    "P2 has type (is type of)"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E55 # E55 Type
        self.flabel = "P2 has type"
        self.rlabel = "P2B is type of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P2 has type (is type of)"

class P3(object):
    "P3 has note"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E62 # E62 String
        self.flabel = "P3 has note"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 0:n,0:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P3 has note"
        
class P4(object):
    "P4 has time-span (is time-span of)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E52 # E52 Time-Span
        self.flabel = "P4 has time-span"
        self.rlabel = "P4B is time-span of"
        
        ### Quantification: 1:1,1:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 1
        self.range.max = -1
    def __str__(self):
        return "P4 has time-span (is time-span of)"
    
class P5(object):
    "P5 consists of (forms part of)"
    def __init__(self):
        self.domain = E3 # E3 Condition State
        self.range = E3 # E3 Condition State
        self.flabel = "P5 consists of"
        self.rlabel = "P5B forms part of"
        
        ### Quantification: 0:n,0:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P5 consists of (forms part of)"
    
class P7(object):
    "P7 took place at (witnessed)"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E53 # E53 Place
        self.flabel = "P7 took place at"
        self.rlabel = "P7B witnessed"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P7 took place at (witnessed)"
    
class P8(object):
    "P8 took place on or within (witnessed)"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E19 # E19 Physical Object
        self.flabel = "P8 took place on or within"
        self.rlabel = "P8B witnessed"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P8 took place on or within (witnessed)"
    
class P9(object):
    "P9 consists of (forms part of)"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E4 # E4 Period
        self.flabel = "P9 consists of"
        self.rlabel = "P9B forms part of"
        
        ### Quantification: 0:n,0:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P9 consists of (forms part of)"
    
# Required by FRBRoo_101.py
class P9B(object):
    "P9 consists of (forms part of)"
    def __init__(self):
        self.domain = E4
        self.range = E4
        self.flabel = "P9B forms part of"
        self.rlabel = "P9 consists of"
    
class P10(object):
    "P10 falls within (contains)"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E4 # E4 Period
        self.flabel = "P10 falls within"
        self.rlabel = "P10B contains"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P10 falls within (contains)"

class P12(object):
    "P12 occurred in the presence of (was present at)"
    def __init__(self):
        self.domain = E5 # E5 Event
        self.range = E77 # E77 Persistent Item
        self.flabel = "P12 occurred in the presence of"
        self.rlabel = "P12B was present at"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P12 occurred in the presence of (was present at)"

class P11(P12):
    "P11 had participant (participated in)"
    def __init__(self):
        self.domain = E5 # E5 Event
        self.range = E39 # E39 Actor
        self.flabel = "P11 had participant"
        self.rlabel = "P11B participated in"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P11 had participant (participated in)"
    
class P93(P12):
    "P93 took out of existence (was taken out of existence by)"
    def __init__(self):
        self.domain = E64 # E64 End of Existence
        self.range = E77 # E77 Persistent Item
        self.flabel = "P93 took out of existence"
        self.rlabel = "P93B was taken out of existence by"
        
        ### Quantification: 1:n,0:1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P93 took out of existence (was taken out of existence by)"
        
class P13(P93):
    "P13 destroyed (was destroyed by)"
    def __init__(self):
        self.domain = E6 # E6 Destruction
        self.range = E18 # E18 Physical Thing
        self.flabel = "P13 destroyed"
        self.rlabel = "P13B was destroyed by"
        
        ### Quantification: 1:n,0:1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P13 destroyed (was destroyed by)"
    
class P14(P11):
    "P14 carried out by (performed)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E39 # E39 Actor
        self.flabel = "P14 carried out by"
        self.rlabel = "P14B performed"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P14 carried out by (performed)"
    
class P15(object):
    "P15 was influenced by (influenced)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E1 # E1 CRM Entity
        self.flabel = "P15 was influenced by"
        self.rlabel = "P15B influenced"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P15 was influenced by (influenced)"
    
class P16(P12, P15):
    "P16 used specific object (was used for)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E70 # E70 Thing
        self.flabel = "P16 used specific object"
        self.rlabel = "P16B was used for"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P16 used specific object (was used for)"
    
# Required by FRBRoo_101.py
class P16B(object):
    "P16 used specific object (was used for)"
    def __init__(self):
        self.domain = E70
        self.range = E7
        self.flabel = "P16B was used for"
        self.rlabel = "P16 used specific object"
    
class P17(P15):
    "P17 was motivated by (motivated)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E1 # E1 CRM Entity
        self.flabel = "P17 was motivated by"
        self.rlabel = "P17B motivated"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P17 was motivated by (motivated)"
    
class P19(object):
    "P19 was intended use of (was made for):"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E71 # E71 Man-Made Thing
        self.flabel = "P19 was intended use of"
        self.rlabel = "P19B was made for"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P19 was intended use of (was made for):"
    
class P20(object):
    "P20 had specific purpose (was purpose of)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E5 # E5 Event
        self.flabel = "P20 had specific purpose"
        self.rlabel = "P20B was purpose of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P20 had specific purpose (was purpose of)"
    
class P21(object):
    "P21 had general purpose (was purpose of)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E55 # E55 Type
        self.flabel = "P21 had general purpose"
        self.rlabel = "P21B was purpose of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P21 had general purpose (was purpose of)"
    
class P22(P14):
    "P22 transferred title to (acquired title through)"
    def __init__(self):
        self.domain = E8 # E8 Acquisition
        self.range = E39 # E39 Actor
        self.flabel = "P22 transferred title to"
        self.rlabel = "P22B acquired title through"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P22 transferred title to (acquired title through)"

class P23(P14):
    "P23 transferred title from (surrendered title through)"
    def __init__(self):
        self.domain = E8 # E8 Acquisition
        self.range = E39 # E39 Actor
        self.flabel = "P23 transferred title from"
        self.rlabel = "P23B surrendered title through"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P23 transferred title from (surrendered title through)"
    
class P24(object):
    "P24 transferred title of (changed ownership through)"
    
    def __init__(self):
        self.domain = E8 # E8 Acquisition
        self.range = E18 # E18 Physical Thing
        self.flabel = "P24 transferred title of"
        self.rlabel = "P24B changed ownership through"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P24 transferred title of (changed ownership through)"
    
class P25(P12):
    "P25 moved (moved by)"
    def __init__(self):
        self.domain = E9 # E9 Move
        self.range = E19 # E19 Physical Object
        self.flabel = "P25 moved"
        self.rlabel = "P25B moved by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P25 moved (moved by)"
    
class P26(P7):
    "P26 moved to (was destination of)"
    def __init__(self):
        self.domain = E9 # E9 Move
        self.range = E53 # E53 Place
        self.flabel = "P26 moved to"
        self.rlabel = "P26B was destination of"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P26 moved to (was destination of)"
    
class P27(P7):
    "P27 moved from (was origin of)"
    def __init__(self):
        self.domain = E9 # E9 Move
        self.range = E53 # E53 Place
        self.flabel = "P27 moved from"
        self.rlabel = "P27B was origin of"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P27 moved from (was origin of)"
    
class P28(P14):
    "P28 custody surrendered by (surrendered custody through)"
    def __init__(self):
        self.domain = E10 # E10 Transfer of Custody
        self.range = E39 # E39 Actor
        self.flabel = "P28 custody surrendered by"
        self.rlabel = "P28B surrendered custody through"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P28 custody surrendered by (surrendered custody through)"
        
class P29(P14):
    "P29 custody received by (received custody through)"
    def __init__(self):
        self.domain = E10 # E10 Transfer of Custody
        self.range = E39 # E39 Actor
        self.flabel = "P29 custody received by"
        self.rlabel = "P29B received custody through"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P29 custody received by (received custody through)"

class P30(object):
    "P30 transferred custody of (custody transferred through)"
    def __init__(self):
        self.domain = E10 # E10 Transfer of Custody
        self.range = E18 # E18 Physical Thing
        self.flabel = "P30 transferred custody of"
        self.rlabel = "P30B custody transferred through"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P30 transferred custody of (custody transferred through)"
    
class P31(P12):
    "P31 has modified (was modified by)"
    def __init__(self):
        self.domain = E11 # E11 Modification
        self.range = E24 # E24 Physical Man-Made Thing
        self.flabel = "P31 has modified"
        self.rlabel = "P31B was modified by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P31 has modified (was modified by)"
    
class P125(object):
    "P125 used object of type (was type of object used in)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E55 # E55 Type
        self.flabel = "P125 used object of type"
        self.rlabel = "P125B was type of object used in"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P125 used object of type (was type of object used in)"
    
class P32(P125):
    "P32 used general technique (was technique of)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E55 # E55 Type
        self.flabel = "P32 used general technique"
        self.rlabel = "P32B was technique of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P32 used general technique (was technique of)"
    
class P33(P16):
    "P33 used specific technique (was used by)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E29 # E29 Design or Procedure
        self.flabel = "P33 used specific technique"
        self.rlabel = "P33B was used by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P33 used specific technique (was used by)"
    
class P140(object):
    "P140 assigned attribute to (was attributed by)"
    def __init__(self):
        self.domain = E13 # E13 Attribute Assignment
        self.range = E1 # E1 CRM Entity
        self.flabel = "P140 assigned attribute to"
        self.rlabel = "P140B was attributed by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P140 assigned attribute to (was attributed by)"
    
class P34(P140):
    "P34 concerned (was assessed by)"
    def __init__(self):
        self.domain = E14 # E14 Condition Assessment
        self.range = E18 # E18 Physical Thing
        self.flabel = "P34 concerned"
        self.rlabel = "P34B was assessed by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P34 concerned (was assessed by)"
    
class P141(object):
    "P141 assigned (was assigned by)"
    def __init__(self):
        self.domain = E13 # E13 Attribute Assignment
        self.range = E1 # E1 CRM Entity
        self.flabel = "P141 assigned"
        self.rlabel = "P141B was assigned by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P141 assigned (was assigned by)"
    
class P35(P141):
    "P35 has identified (was identified by)"
    def __init__(self):
        self.domain = E14 # E14 Condition Assessment
        self.range = E3 # E3 Condition State
        self.flabel = "P35 has identified"
        self.rlabel = "P35B was identified by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P35 has identified (was identified by)"
    
class P37(P141):
    "P37 assigned (was assigned by)"
    def __init__(self):
        self.domain = E15 # E15 Identifier Assignment
        self.range = E42 # E42 Identifier
        self.flabel = "P37 assigned"
        self.rlabel = "P37B was assigned by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P37 assigned (was assigned by)"
    
class P38(P141):
    "P38 deassigned (was deassigned by)"
    def __init__(self):
        self.domain = E15 # E15 Identifier Assignment
        self.range = E42 # E42 Identifier
        self.flabel = "P38 deassigned"
        self.rlabel = "P38B was deassigned by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P38 deassigned (was deassigned by)"
    
class P39(P140):
    "P39 measured (was measured by):"
    def __init__(self):
        self.domain = E16 # E16 Measurement
        self.range = E1 # E1 CRM Entity
        self.flabel = "P39 measured"
        self.rlabel = "P39B was measured by"
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P39 measured (was measured by):"
    
class P40(P141):
    "P40 observed dimension (was observed in)"
    def __init__(self):
        self.domain = E16 # E16 Measurement
        self.range = E54 # E54 Dimension
        self.flabel = "P40 observed dimension"
        self.rlabel = "P40B was observed in"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P40 observed dimension (was observed in)"
    
class P41(P140):
    "P41 classified (was classified by)"
    def __init__(self):
        self.domain = E17 # E17 Type Assignment
        self.range = E1 # E1 CRM Entity
        self.flabel = "P41 classified"
        self.rlabel = "P41B was classified by"
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P41 classified (was classified by)"
    
class P42(P141):
    "P42 assigned (was assigned by)"
    def __init__(self):
        self.domain = E17 # E17 Type Assignment
        self.range = E55 # E55 Type
        self.flabel = "P42 assigned"
        self.rlabel = "P42B was assigned by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P42 assigned (was assigned by)"
    
class P43(object):
    "P43 has dimension (is dimension of)"
    def __init__(self):
        self.domain = E70 # E70 Thing
        self.range = E54 # E54 Dimension
        self.flabel = "P43 has dimension"
        self.rlabel = "P43B is dimension of"
        
        ### Quantification: 0:n,1:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P43 has dimension (is dimension of)"
    
class P44(object):
    "P44 has condition (is condition of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E3 # E3 Condition State
        self.flabel = "P44 has condition"
        self.rlabel = "P44B is condition of"
        
        ### Quantification: 0:n,1:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P44 has condition (is condition of)"
    
class P45(object):
    "P45 consists of (is incorporated in)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E57 # E57 Material
        self.flabel = "P45 consists of"
        self.rlabel = "P45B is incorporated in"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P45 consists of (is incorporated in)"
    
class P46(object):
    "P46 is composed of (forms part of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E18 # E18 Physical Thing
        self.flabel = "P46 is composed of"
        self.rlabel = "P46B forms part of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P46 is composed of (forms part of)"

class P48(P1):
    "P48 has preferred identifier (is preferred identifier of)"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E42 # E42 Identifier
        self.flabel = "P48 has preferred identifier"
        self.rlabel = "P48B is preferred identifier of"
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P48 has preferred identifier (is preferred identifier of)"
        
class P49(object):
    "P49 has former or current keeper (is former or current keeper of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E39 # E39 Actor
        self.flabel = "P49 has former or current keeper"
        self.rlabel = "P49B is former or current keeper of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P49 has former or current keeper (is former or current keeper of)"
    
class P50(P49):
    "P50 has current keeper (is current keeper of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E39 # E39 Actor
        self.flabel = "P50 has current keeper"
        self.rlabel = "P50B is current keeper of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P50 has current keeper (is current keeper of)"
    
class P51(object):
    "P51 has former or current owner (is former or current owner of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E39 # E39 Actor
        self.flabel = "P51 has former or current owner"
        self.rlabel = "P51B is former or current owner of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P51 has former or current owner (is former or current owner of)"
    
class P52(P51):
    "P52 has current owner (is current owner of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E39 # E39 Actor
        self.flabel = "P52 has current owner"
        self.rlabel = "P52B is current owner of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P52 has current owner (is current owner of)"
    
class P53(object):
    "P53 has former or current location (is former or current location of)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E53 # E53 Place
        self.flabel = "P53 has former or current location"
        self.rlabel = "P53B is former or current location of"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P53 has former or current location (is former or current location of)"
    
class P54(object):
    "P54 has current permanent location (is current permanent location of)"
    def __init__(self):
        self.domain = E19 # E19 Physical Object
        self.range = E53 # E53 Place
        self.flabel = "P54 has current permanent location"
        self.rlabel = "P54B is current permanent location of"
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P54 has current permanent location (is current permanent location of)"
    
class P55(P53):
    "P55 has current location (currently holds)"
    def __init__(self):
        self.domain = E19 # E19 Physical Object
        self.range = E53 # E53 Place
        self.flabel = "P55 has current location"
        self.rlabel = "P55B currently holds"
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P55 has current location (currently holds)"
    
class P56(P46):
    "P56 bears feature (is found on):"
    def __init__(self):
        self.domain = E19 # E19 Physical Object
        self.range = E26 # E26 Physical Feature
        self.flabel = "P56 bears feature"
        self.rlabel = "P56B is found on"
        
        ### Quantification: 0:n,1:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P56 bears feature (is found on):"
    
class P57(object):
    "P57 has number of parts"
    def __init__(self):
        self.domain = E19 # E19 Physical Object
        self.range = E60 # E60 Number
        self.flabel = "P57 has number of parts"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P57 has number of parts"
    
class P58(object):
    "P58 has section definition (defines section)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E46 # E46 Section Definition
        self.flabel = "P58 has section definition"
        self.rlabel = "P58B defines section"
        
        ### Quantification: 0:n,1:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P58 has section definition (defines section)"
    
class P59(object):
    "P59 has section (is located on or within)"
    def __init__(self):
        self.domain = E18 # E18 Physical Thing
        self.range = E53 # E53 Place
        self.flabel = "P59 has section"
        self.rlabel = "P59B is located on or within"
        
        ### Quantification: 0:n,0:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P59 has section (is located on or within)"
    
class P62(object):
    "P62 depicts (is depicted by)"
    def __init__(self):
        self.domain = E24 # E24 Physical Man-Made Thing
        self.range = E1 # E1 CRM Entity
        self.flabel = "P62 depicts"
        self.rlabel = "P62B is depicted by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P62 depicts (is depicted by)"
    
class P128(object):
    "P128 carries (is carried by)"
    def __init__(self):
        self.domain = E24 # E24 Physical Man-Made Thing
        self.range = E73 # E73 Information Object
        self.flabel = "P128 carries"
        self.rlabel = "P128B is carried by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P128 carries (is carried by)"

# Required by FRBRoo_101.py
class P128B(object):
    "P128 carries (is carried by)"
    def __init__(self):
        self.domain = E73
        self.range = E24
        self.flabel = "P128B is carried by"
        self.rlabel = "P128 carries"
    
class P65(P128):
    "P65 shows visual item (is shown by)"
    def __init__(self):
        self.domain = E24 # E24 Physical Man-Made Thing
        self.range = E36 # E36 Visual Item
        self.flabel = "P65 shows visual item"
        self.rlabel = "P65B is shown by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P65 shows visual item (is shown by)"
    
class P67(object):
    "P67 refers to (is referred to by)"
    def __init__(self):
        self.domain = E89 # E89 Propositional Object
        self.range = E1 # E1 CRM Entity
        self.flabel = "P67 refers to"
        self.rlabel = "P67B is referred to by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P67 refers to (is referred to by)"
    
class P68(object):
    "P68 foresees use of (use foreseen by):"
    def __init__(self):
        self.domain = E29 # E29 Design or Procedure
        self.range = E57 # E57 Material
        self.flabel = "P68 foresees use of"
        self.rlabel = "P68B use foreseen by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P68 foresees use of (use foreseen by):"
    
class P69(object):
    "P69 is associated with"
    def __init__(self):
        self.domain = E29 # E29 Design or Procedure
        self.range = E29 # E29 Design or Procedure
        self.flabel = "P69 is associated with" # homonymic
        self.rlabel = "P69B is associated with" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P69 is associated with"
    
class P70(P67):
    "P70 documents (is documented in)"
    def __init__(self):
        self.domain = E31 # E31 Document
        self.range = E1 # E1 CRM Entity
        self.flabel = "P70 documents"
        self.rlabel = "P70B is documented in"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P70 documents (is documented in)"
    
class P71(P67):
    "P71 lists (is listed in)"
    def __init__(self):
        self.domain = E32 # E32 Authority Document
        self.range = E55 # E55 Type
        self.flabel = "P71 lists"
        self.rlabel = "P71B is listed in"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P71 lists (is listed in)"
    
class P72(object):
    "P72 has language (is language of)"
    def __init__(self):
        self.domain = E33 # E33 Linguistic Object
        self.range = E56 # E56 Language
        self.flabel = "P72 has language"
        self.rlabel = "P72B is language of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P72 has language (is language of)"
    
class P130(object):
    "P130 shows features of (features are also found on)"
    def __init__(self):
        self.domain = E70 # E70 Thing
        self.range = E70 # E70 Thing
        self.flabel = "P130 shows features of"
        self.rlabel = "P130B features are also found on"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P130 shows features of (features are also found on)"
    
class P73(P130):
    "P73 has translation (is translation of)"
    def __init__(self):
        self.domain = E33 # E33 Linguistic Object
        self.range = E33 # E33 Linguistic Object
        self.flabel = "P73 has translation"
        self.rlabel = "P73B is translation of"
        
        ### Quantification: 0:n,0:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P73 has translation (is translation of)"
    
class P74(object):
    "P74 has current or former residence (is current or former residence of)"
    def __init__(self):
        self.domain = E39 # E39 Actor
        self.range = E53 # E53 Place
        self.flabel = "P74 has current or former residence"
        self.rlabel = "P74B is current or former residence of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P74 has current or former residence (is current or former residence of)"
    
class P75(object):
    "P75 possesses (is possessed by)"
    def __init__(self):
        self.domain = E39 # E39 Actor
        self.range = E30 # E30 Right
        self.flabel = "P75 possesses"
        self.rlabel = "P75B is possessed by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P75 possesses (is possessed by)"
    
class P76(object):
    "P76 has contact point (provides access to)"
    def __init__(self):
        self.domain = E39 # E39 Actor
        self.range = E51 # E51 Contact Point
        self.flabel = "P76 has contact point"
        self.rlabel = "P76B provides access to"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P76 has contact point (provides access to)"
    
class P78(P1):
    "P78 is identified by (identifies)"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E49 # E49 Time Appellation
        self.flabel = "P78 is identified by"
        self.rlabel = "P78B identifies"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P78 is identified by (identifies)"
    
class P79(P3):
    "P79 beginning is qualified by"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E62 # E62 String
        self.flabel = "P79 beginning is qualified by"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P79 beginning is qualified by"
    
class P80(P3):
    "P80 end is qualified by"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E62 # E62 String
        self.flabel = "P80 end is qualified by"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 0:1,0:n
        self.domain.min = 0
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P80 end is qualified by"
    
class P81(object):
    "P81 ongoing throughout"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E61 # E61 Time Primitive
        self.flabel = "P81 ongoing throughout"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P81 ongoing throughout"
    
class P82(object):
    "P82 at some time within"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E61 # E61 Time Primitive
        self.flabel = "P82 at some time within"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P82 at some time within"
    
class P83(object):
    "P83 had at least duration (was minimum duration of)"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E54 # E54 Dimension
        self.flabel = "P83 had at least duration"
        self.rlabel = "P83B was minimum duration of"
        
        ### Quantification: 1,1:1,1
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P83 had at least duration (was minimum duration of)"
    
class P84(object):
    "P84 had at most duration (was maximum duration of)"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E54 # E54 Dimension
        self.flabel = "P84 had at most duration"
        self.rlabel = "P84B was maximum duration of"
        
        ### Quantification: 1,1:1,1
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P84 had at most duration (was maximum duration of)"
    
class P86(object):
    "P86 falls within (contains)"
    def __init__(self):
        self.domain = E52 # E52 Time-Span
        self.range = E52 # E52 Time-Span
        self.flabel = "P86 falls within"
        self.rlabel = "P86B contains"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P86 falls within (contains)"
    
class P87(object):
    "P87 is identified by (identifies)"
    def __init__(self):
        self.domain = E53 # E53 Place
        self.range = E44 # E44 Place Appellation
        self.flabel = "P87 is identified by"
        self.rlabel = "P87B identifies"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P87 is identified by (identifies)"
    
class P88(object):
    "P88 consists of (forms part of)"
    def __init__(self):
        self.domain = E53 # E53 Place
        self.range = E53 # E53 Place
        self.flabel = "P88 consists of"
        self.rlabel = "P88B forms part of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P88 consists of (forms part of)"
    
class P89(object):
    "P89 falls within (contains)"
    def __init__(self):
        self.domain = E53 # E53 Place
        self.range = E53 # E53 Place
        self.flabel = "P89 falls within"
        self.rlabel = "P89B contains"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P89 falls within (contains)"
    
class P90(object):
    "P90 has value"
    def __init__(self):
        self.domain = E54 # E54 Dimension
        self.range = E60 # E60 Number
        self.flabel = "P90 has value"
        self.rlabel = "" # No reverse link
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P90 has value"
    
class P91(object):
    "P91 has unit (is unit of)"
    def __init__(self):
        self.domain = E54 # E54 Dimension
        self.range = E58 # E58 Measurement Unit
        self.flabel = "P91 has unit"
        self.rlabel = "P91B is unit of"
        
        ### Quantification: 1:1,0:n
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P91 has unit (is unit of)"
    
class P92(P12):
    "P92 brought into existence (was brought into existence by)"
    def __init__(self):
        self.domain = E63 # E63 Beginning of Existence
        self.range = E77 # E77 Persistent Item
        self.flabel = "P92 brought into existence"
        self.rlabel = "P92B was brought into existence by"
        
        ### Quantification: 1,n:1,1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P92 brought into existence (was brought into existence by)"
        
class P94(P92):
    "P94 has created (was created by)"
    def __init__(self):
        self.domain = E65 # E65 Creation
        self.range = E28 # E28 Conceptual Object
        self.flabel = "P94 has created"
        self.rlabel = "P94B was created by"
        
        ### Quantification: 1,n:1,1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P94 has created (was created by)"
    
class P95(P92):
    "P95 has formed (was formed by)"
    def __init__(self):
        self.domain = E66 # E66 Formation
        self.range = E74 # E74 Group
        self.flabel = "P95 has formed"
        self.rlabel = "P95B was formed by"
        
        ### Quantification: 1,n:1,1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P95 has formed (was formed by)"
    
class P96(P11):
    "P96 by mother (gave birth)"
    def __init__(self):
        self.domain = E67 # E67 Birth
        self.range = E21 # E21 Person
        self.flabel = "P96 by mother"
        self.rlabel = "P96B gave birth"
        
        ### Quantification: 1,1:0,1
        self.domain.min = 1
        self.domain.max = 1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P96 by mother (gave birth)"
    
class P97(object):
    "P97 from father (was father for)"
    def __init__(self):
        self.domain = E67 # E67 Birth
        self.range = E21 # E21 Person
        self.flabel = "P97 from father"
        self.rlabel = "P97B was father for"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P97 from father (was father for)"
    
class P98(P92):
    "P98 brought into life (was born)"
    def __init__(self):
        self.domain = E67 # E67 Birth
        self.range = E21 # E21 Person
        self.flabel = "P98 brought into life"
        self.rlabel = "P98B was born"
        
        ### Quantification: 0:n,1:1
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P98 brought into life (was born)"
    
class P99(P11, P93):
    "P99 dissolved (was dissolved by)"
    def __init__(self):
        self.domain = E68 # E68 Dissolution
        self.range = E74 # E74 Group
        self.flabel = "P99 dissolved"
        self.rlabel = "P99B was dissolved by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P99 dissolved (was dissolved by)"
    
class P100(P93):
    "P100 was death of (died in)"
    def __init__(self):
        self.domain = E69 # E69 Death
        self.range = E21 # E21 Person
        self.flabel = "P100 was death of"
        self.rlabel = "P100B died in"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P100 was death of (died in)"

class P101(object):
    "P101 had as general use (was use of)"
    def __init__(self):
        self.domain = E70 # E70 Thing
        self.range = E55 # E55 Type
        self.flabel = "P101 had as general use"
        self.rlabel = "P101B was use of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P101 had as general use (was use of)"
    
class P102(P1):
    "P102 has title (is title of)"
    def __init__(self):
        self.domain = E71 # E71 Man-Made Thing
        self.range = E35 # E35 Title
        self.flabel = "P102 has title"
        self.rlabel = "P102B is title of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P102 has title (is title of)"
    
class P103(object):
    "P103 was intended for (was intention of)"
    def __init__(self):
        self.domain = E71 # E71 Man-Made Thing
        self.range = E55 # E55 Type
        self.flabel = "P103 was intended for"
        self.rlabel = "P103B was intention of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P103 was intended for (was intention of)"
    
class P104(object):
    "P104 is subject to (applies to)"
    def __init__(self):
        self.domain = E72 # E72 Legal Object
        self.range = E30 # E30 Right
        self.flabel = "P104 is subject to"
        self.rlabel = "P104B applies to"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P104 is subject to (applies to)"
    
class P105(P52):
    "P105 right held by (has right on)"
    def __init__(self):
        self.domain = E72 # E72 Legal Object
        self.range = E39 # E39 Actor
        self.flabel = "P105 right held by"
        self.rlabel = "P105B has right on"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P105 right held by (has right on)"
    
class P106(object):
    "P106 is composed of (forms part of)"
    def __init__(self):
        self.domain = E90 # E90 Symbolic Object
        self.range = E90 # E90 Symbolic Object
        self.flabel = "P106 is composed of"
        self.rlabel = "P106B forms part of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P106 is composed of (forms part of)"
    
class P107(object):
    "P107 has current or former member (is current or former member of)"
    def __init__(self):
        self.domain = E74 # E74 Group
        self.range = E39 # E39 Actor
        self.flabel = "P107 has current or former member"
        self.rlabel = "P107B is current or former member of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P107 has current or former member (is current or former member of)"
    
class P108(P31, P92):
    "P108 has produced (was produced by)"
    def __init__(self):
        self.domain = E12 # E12 Production
        self.range = E24 # E24 Physical Man-Made Thing
        self.flabel = "P108 has produced"
        self.rlabel = "P108B was produced by"
        
        ### Quantification: 1,n:1,1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 1
        self.range.max = 1
    def __str__(self):
        return "P108 has produced (was produced by)"
    
class P109(object):
    "P109 has current or former curator (is current or former curator of)"
    def __init__(self):
        self.domain = E78 # E78 Collection
        self.range = E39 # E39 Actor
        self.flabel = "P109 has current or former curator"
        self.rlabel = "P109B is current or former curator of"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P109 has current or former curator (is current or former curator of)"
    
class P110(P31):
    "P110 augmented (was augmented by)"
    def __init__(self):
        self.domain = E79 # E79 Part Addition
        self.range = E24 # E24 Physical Man-Made Thing
        self.flabel = "P110 augmented"
        self.rlabel = "P110B was augmented by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P110 augmented (was augmented by)"
    
class P111(object):
    "P111 added (was added by)"
    def __init__(self):
        self.domain = E79 # E79 Part Addition
        self.range = E18 # E18 Physical Thing
        self.flabel = "P111 added"
        self.rlabel = "P111B was added by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P111 added (was added by)"
    
class P112(P31):
    "P112 diminished (was diminished by)"
    def __init__(self):
        self.domain = E80 # E80 Part Removal
        self.range = E24 # E24 Physical Man-Made Thing
        self.flabel = "P112 diminished"
        self.rlabel = "P112B was diminished by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P112 diminished (was diminished by)"
    
class P113(object):
    "P113 removed (was removed by)"
    def __init__(self):
        self.domain = E80 # E80 Part Removal
        self.range = E18 # E18 Physical Thing
        self.flabel = "P113 removed"
        self.rlabel = "P113B was removed by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P113 removed (was removed by)"
    
class P114(object):
    "P114 is equal in time to"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P114 is equal in time to" # homonymic
        self.rlabel = "P114B is equal in time to" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P114 is equal in time to"
    
class P115(object):
    "P115 finishes (is finished by)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P115 finishes"
        self.rlabel = "P115B is finished by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P115 finishes (is finished by)"
    
class P116(object):
    "P116 starts (is started by)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P116 starts"
        self.rlabel = "P116B is started by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P116 starts (is started by)"
    
class P117(object):
    "P117 occurs during (includes)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P117 occurs during"
        self.rlabel = "P117B includes"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P117 occurs during (includes)"
    
class P118(object):
    "P118 overlaps in time with (is overlapped in time by)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P118 overlaps in time with"
        self.rlabel = "P118B is overlapped in time by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P118 overlaps in time with (is overlapped in time by)"
    
class P119(object):
    "P119 meets in time with (is met in time by)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P119 meets in time with"
        self.rlabel = "P119B is met in time by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P119 meets in time with (is met in time by)"
    
class P120(object):
    "P120 occurs before (occurs after)"
    def __init__(self):
        self.domain = E2 # E2 Temporal Entity
        self.range = E2 # E2 Temporal Entity
        self.flabel = "P120 occurs before"
        self.rlabel = "P120B occurs after"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P120 occurs before (occurs after)"

class P121(object):
    "P121 overlaps with"
    def __init__(self):
        self.domain = E53 # E53 Place
        self.range = E53 # E53 Place
        self.flabel = "P121 overlaps with" # homonymic
        self.rlabel = "P121B overlaps with" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P121 overlaps with"
    
class P122(object):
    "P122 borders with"
    def __init__(self):
        self.domain = E53 # E53 Place
        self.range = E53 # E53 Place
        self.flabel = "P122 borders with" # homonymic
        self.rlabel = "P122B borders with" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P122 borders with"
    
class P123(P92):
    "P123 resulted in (resulted from)"
    def __init__(self):
        self.domain = E81 # E81 Transformation
        self.range = E77 # E77 Persistent Item
        self.flabel = "P123 resulted in"
        self.rlabel = "P123B resulted from"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P123 resulted in (resulted from)"
    
class P124(P93):
    "P124 transformed (was transformed by)"
    def __init__(self):
        self.domain = E81 # E81 Transformation
        self.range = E77 # E77 Persistent Item
        self.flabel = "P124 transformed"
        self.rlabel = "P124B was transformed by"
        
        ### Quantification: 1:n,0:1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P124 transformed (was transformed by)"
        
class P126(object):
    "P126 employed (was employed in)"
    def __init__(self):
        self.domain = E11 # E11 Modification
        self.range = E57 # E57 Material
        self.flabel = "P126 employed"
        self.rlabel = "P126B was employed in"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P126 employed (was employed in)"
    
class P127(object):
    "P127 has broader term (has narrower term)"
    def __init__(self):
        self.domain = E55 # E55 Type
        self.range = E55 # E55 Type
        self.flabel = "P127 has broader term"
        self.rlabel = "P127B has narrower term"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P127 has broader term (has narrower term)"
    
class P129(P67):
    "P129 is about (is subject of)"
    def __init__(self):
        self.domain = E89 # E89 Propositional Object
        self.range = E1 # E1 CRM Entity
        self.flabel = "P129 is about"
        self.rlabel = "P129B is subject of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P129 is about (is subject of)"
        
class P131(P1):
    "P131 is identified by (identifies)"
    def __init__(self):
        self.domain = E39 # E39 Actor
        self.range = E82 # E82 Actor Appellation
        self.flabel = "P131 is identified by"
        self.rlabel = "P131B identifies"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P131 is identified by (identifies)"
    
class P132(object):
    "P132 overlaps with"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E4 # E4 Period
        self.flabel = "P132 overlaps with" # homonymic
        self.rlabel = "P132B overlaps with" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P132 overlaps with"
    
class P133(object):
    "P133 is separated from"
    def __init__(self):
        self.domain = E4 # E4 Period
        self.range = E4 # E4 Period
        self.flabel = "P133 is separated from" # homonymic
        self.rlabel = "P133B is separated from" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P133 is separated from"
    
class P134(P15):
    "P134 continued (was continued by)"
    def __init__(self):
        self.domain = E7 # E7 Activity
        self.range = E7 # E7 Activity
        self.flabel = "P134 continued"
        self.rlabel = "P134B was continued by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P134 continued (was continued by)"
    
class P135(P94):
    "P135 created type (was created by)"
    def __init__(self):
        self.domain = E83 # E83 Type Creation
        self.range = E55 # E55 Type
        self.flabel = "P135 created type"
        self.rlabel = "P135B was created by"
        
        ### Quantification: 1:n,0:1
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = 1
    def __str__(self):
        return "P135 created type (was created by)"
    
class P136(P15):
    "P136 was based on (supported type creation)"
    def __init__(self):
        self.domain = E83 # E83 Type Creation
        self.range = E1 # E1 CRM Entity
        self.flabel = "P136 was based on"
        self.rlabel = "P136B supported type creation"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P136 was based on (supported type creation)"
    
class P137(P2):
    "P137 exemplifies (is exemplified by)"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E55 # E55 Type
        self.flabel = "P137 exemplifies"
        self.rlabel = "P137B is exemplified by"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P137 exemplifies ( is exemplified by )"
    
class P138(P67):
    "P138 represents (has representation)"
    def __init__(self):
        self.domain = E36 # E36 Visual Item
        self.range = E1 # E1 CRM Entity
        self.flabel = "P138 represents"
        self.rlabel = "P138B has representation"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P138 represents (has representation)"
    
class P139(object):
    "P139 has alternative form"
    def __init__(self):
        self.domain = E41 # E41 Appellation
        self.range = E41 # E41 Appellation
        self.flabel = "P139 has alternative form" # homonymic
        self.rlabel = "P139B has alternative form" # homonymic
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P139 has alternative form"
        
class P142(P16):
    "P142 used constituent (was used in)"
    def __init__(self):
        self.domain = E15 # E15 Identifier Assignment
        self.range = E41 # E41 Appellation
        self.flabel = "P142 used constituent"
        self.rlabel = "P142B was used in"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P142 used constituent (was used in)"
    
class P143(P11):
    "P143 joined (was joined by)"
    def __init__(self):
        self.domain = E85 # E85 Joining
        self.range = E39 # E39 Actor
        self.flabel = "P143 joined"
        self.rlabel = "P143B was joined by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P143 joined (was joined by)"
    
class P144(P11):
    "P144 joined with (gained member by)"
    def __init__(self):
        self.domain = E85 # E85 Joining
        self.range = E74 # E74 Group
        self.flabel = "P144 joined with"
        self.rlabel = "P144B gained member by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P144 joined with (gained member by)"
    
class P145(P11):
    "P145 separated (left by)"
    def __init__(self):
        self.domain = E86 # E86 Leaving
        self.range = E39 # E39 Actor
        self.flabel = "P145 separated"
        self.rlabel = "P145B left by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P145 separated (left by)"
    
class P146(P11):
    "P146 separated from (lost member by)"
    def __init__(self):
        self.domain = E86 # E86 Leaving
        self.range = E74 # E74 Group
        self.flabel = "P146 separated from"
        self.rlabel = "P146B lost member by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P146 separated from (lost member by)"
    
class P147(object):
    "P147 curated (was curated by)"
    def __init__(self):
        self.domain = E87 # E87 Curation Activity
        self.range = E78 # E78 Collection
        self.flabel = "P147 curated"
        self.rlabel = "P147B was curated by"
        
        ### Quantification: 1:n,0:n
        self.domain.min = 1
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P147 curated (was curated by)"
    
class P148(object):
    "P148 has component (is component of)"
    def __init__(self):
        self.domain = E89 # E89 Propositional Object
        self.range = E89 # E89 Propositional Object
        self.flabel = "P148 has component"
        self.rlabel = "P148B is component of"
        
        ### Quantification: 0:n,0:n
        self.domain.min = 0
        self.domain.max = -1
        self.range.min = 0
        self.range.max = -1
    def __str__(self):
        return "P148 has component (is component of)"
    