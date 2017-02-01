import inspect
import example
from cidoc_crm_502 import cidoc_crm as crm

#http://www.doughellmann.com/PyMOTW/inspect/

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
    #print 'A, B, C, D:'
    #print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))
    print_class_tree(inspect.getclasstree([crm.E4, crm.E2, crm.E7, crm.E9, crm.E5]))
