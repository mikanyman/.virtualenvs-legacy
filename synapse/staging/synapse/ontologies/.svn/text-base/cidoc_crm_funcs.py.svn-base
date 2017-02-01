from cidoc_crm_502 import cidoc_crm as crm

#def get_domain(cls): return cls
#def get_range(cls): return cls

def introspections_1():
    e87 = crm.E87()
    ### Examples from http://www.ibm.com/developerworks/library/l-print.html
    ### Guide to Python introspection
    #print hasattr(e87.p147, 'domain')   # returns Boolean (True)
    #print id(e87.p147.domain)           # returns id (15368664)
    #print hasattr(15368664, '__doc__')  # returns Boolean (True)
    #print getattr(e87.p147, 'domain')   # returns value
    #print e87.p147.domain               # returns value; equal to above
    #print callable(e87.__str__)         # returns Boolean (True)
    
    #print e87.p147.__getattribute__('domain').__doc__
    #print e87.p147.__getattribute__('range').__doc__

def list_crm_classes():
    
    import sys
    sys.setrecursionlimit(100) # minimum limit
    import inspect

    class_list = [
             '1', '2', '3', '4', '5', '6', '7', '8', '9',
       '10','11','12','13','14','15','16','17','18','19',
       '20','21','22',     '24','25','26','27','28','29',
       '30','31','32','33','34','35','36','37','38','39',
       '40','41','42',     '44','45','46','47','48','49',
       '50','51','52','53','54','55','56','57','58','59',
       '60','61','62','63','64','65','66','67','68','69',
       '70','71','72','73','74','75',     '77','78','79',
       '80','81','82','83','84','85','86','87',     '89',
       '90',
       ]

    ### Instantiate and print class names, e.g. "E1, E2, etc."
    """
    for cls in class_list:
        exec "e%s = crm.E%s()" % (cls, cls)
        exec "print e%s.__class__.__name__" % (cls,)"""
    
    e87 = crm.E87()
    print e87.__class__.__bases__

def gmems():
    """
    This stuff is for Python 2.5 
    Documentation for inspection (Python 2.5)
    http://www.doughellmann.com/PyMOTW/inspect/
    
    """
    import inspect
    
    e87 = crm.E87()
    #from pprint import pprint
    #print inspect.getmembers(crm.E87())
    print inspect.getclasstree([crm.E87])
    #for node in tree:
    #    print node[0].__name__
    #pprint(inspect.getmembers(crm.E87).__class__.__doc__)
    
def get_classtree():
    pass

    import inspect
    import example

    class C(example.B):
        pass

    class D(C, example.A):
        pass

    def print_class_tree(tree, indent=-1):
        if isinstance(tree, list):
            for node in tree:
                print_class_tree(node, indent+1)
        else:
            print '  ' * indent, tree[0].__name__
        return

if __name__ == '__main__':
    print 'A, B, C, D:'
    print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))


def main():
    #introspections_1()
    #list_crm_classes()
    #gmems()
    get_classtree()

if __name__ == "__main__":
    main()
else:
    pass


#e87 = crm.E87()
#print e87.p147.__getattribute__('domain').__doc__
#print e87.p147.__getattribute__('range').__doc__

#print e87.__class__.__name__