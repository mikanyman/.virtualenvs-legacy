import cidoc_crm_502 as crm
import FRBRoo_101 as foo

import sys
sys.setrecursionlimit(10) # minimum limit

class F1(crm.E89):
    "F1 Work"
    def __init__(self):
        
        ### Forward FRBRoo properties
        self.r1 = R1()
        self.r2 = R2()
        self.r3 = R3()
        
        ### Forward FRBRoo Identifier Creation Model properties
        self.r40 = R40()
        
        ### Reverse FRBRoo properties
        pass
        
    def crm_fproperties(self):
        return (self.r1, self.r2, self.r3, self.r40)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F1 Work"
    
class F2(crm.E73):
    "F2 Expression"
    def __init__(self):
        
        ### Forward FRBRoo properties
        self.r4 = R4()
        self.r5 = R5()

        ### Forward FRBRoo Identifier Creation Model properties
        self.r41 = R41()
        
        ### Reverse FRBRoo properties
        pass
        
    def crm_fproperties(self):
        return (self.r4, self.r5, self.r41)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F2 Expression"

class F40(crm.E15):
    "F40 Identifier Assignment"
    def __init__(self):
        
        ### Forward FRBRoo Identifier Creation Model properties
        self.r45 = foo.R45()
        self.r46 = foo.R46()
        self.r47 = foo.R47()
        self.r48 = foo.R52()
        
    def crm_fproperties(self):
        return (self.r45, self.r46, self.r47, self.r48)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F40 Identifier Assignment"
    
class F41(crm.E13):
    "F41 Representative Manifestation Assignment"
    def __init__(self):
        
        ### Forward FRBRoo Identifier Creation Model properties
        self.r43 = foo.R43()
        self.r48 = foo.R48()
        self.r49 = foo.R49()
        self.r53 = foo.R53()
        
    def crm_fproperties(self):
        return (self.r43, self.r48, self.r49, self.r53)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F41 Representative Manifestation Assignment"
    
class F42(crm.E13):
    "F42 Representative Expression Assignment"
    def __init__(self):
        
        ### Forward FRBRoo Identifier Creation Model properties
        self.r44 = foo.R44()
        self.r50 = foo.R50()
        self.r51 = foo.R51()
        
    def crm_fproperties(self):
        return (self.r44, self.r50, self.r51)
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F42 Representative Expression Assignment"
    
class F43(crm.E29):
    "F43 Identifier Rule"
    def __init__(self):
        pass

    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return "F43 Identifier Rule"
    
class F44(foo.F11):
    "F44 Bibliographic Agency"
    def __init__(self):
        pass
        
    def crm_fproperties(self):
        return ()
    def crm_rproperties(self):
        return ()
    def __str__(self):
        return ""