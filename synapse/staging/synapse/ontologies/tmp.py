class E1(object):
    pass

class E55(object):
    pass

class P2(object):
    "P2 has type (is type of)"
    def __init__(self):
        self.domain = E1 # E1 CRM Entity
        self.range = E55 # E55 Type
        self.flabel = "P2 has type"
        self.rlabel = "P2B is type of"
        self.domain.min = None
        self.domain.max = None
        self.range.min = None
        self.range.max = None
    def __str__(self):
        return "P2 has type (is type of)"
    
p2 = P2()
print p2.domain.max