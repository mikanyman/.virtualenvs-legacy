from LAM import cidoc_crm_502 as crm
from LAM import FRBRoo_101 as foo

import sys
sys.setrecursionlimit(100) # minimum limit

# IMPORTANT
# http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html

def list_fproperty_names(cls, i):
    
    f_data = ''
    fproperties = cls.crm_fproperties()
        
    if fproperties:
        for p in fproperties:
            f_data += '    ' + p.flabel + ': ' + p.range.__doc__ + '\n'
    else:
        if i == 0:
            f_data += '    No declared forward properties\n'
        else:
            f_data += '    No inherited forward properties\n'
    
    f_data += '\n'
    return f_data

def list_rproperty_names(cls, i):
    
    r_data = ''
    rproperties = cls.crm_rproperties()
    
    if rproperties:
        for p in rproperties:
            r_data += '    ' + p.rlabel + ': ' + p.domain.__doc__ + '\n' # REVERSE!
    else:
        if i == 0:
            r_data += '    No declared reverse properties\n'
            pass
        else:
            r_data += '    No inherited reverse properties\n'
            pass
    
    r_data += '\n'
    return r_data

def test():
   
    foo_class_list = [
                     'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 
              'F10','F11','F12','F13','F14','F15','F16','F17','F18','F19',
              'F20','F21','F22','F23','F24','F25','F26','F27','F28','F29',
              'F30','F31','F32','F33',
              'F40','F41','F42','F43','F44'
              ]
    
    data = ''

    for c in foo_class_list:
        exec "%s = foo.%s()" % (c.lower(), c)
        exec "superclasses = foo.%s.__mro__" % (c,)
        
        ### create list of superclasses:
        sclasses = ''
        for sc in superclasses:
            sclasses += "%s, " % str(sc.__name__)
        
        
        for i in range(len(superclasses)):
            if superclasses[i].__name__ != 'object':
                
                if i == 0:
                    # Class name & underline
                    data += superclasses[i].__doc__ + '\n'
                    data += len(superclasses[i].__doc__) * '=' + '\n\n'
                    
                    # List of superclasses
                    data += '    List of superclasses:\n'
                    data += '    ---------------------\n'
                    data += '    %s\n\n' % sclasses
                
                if i == 0:
                    # Header & underline for declard properties
                    data += "    Properties declared for '%s':\n" % (superclasses[i].__doc__)
                    data += "    " + (26 * '-') + len(superclasses[i].__doc__) * '-' + '\n'
                else:
                    # Header & underline for inherited properties
                    data += "    Properties inherited from '%s':\n" % (superclasses[i].__doc__)
                    data += "    " + (29 * '-') + len(superclasses[i].__doc__) * '-' + '\n'
                
                # Call method to create fproperty listing for class
                if superclasses[i].__module__ == 'LAM.FRBRoo_101':
                    exec "data += list_fproperty_names(foo.%s(), i)" % (superclasses[i].__name__)
                else:
                    exec "data += list_fproperty_names(crm.%s(), i)" % (superclasses[i].__name__)
                    
                # Call method to create rproperty listing for class
                if superclasses[i].__module__ == 'LAM.FRBRoo_101':
                    exec "data += list_rproperty_names(foo.%s(), i)" % (superclasses[i].__name__)
                else:
                    exec "data += list_rproperty_names(crm.%s(), i)" % (superclasses[i].__name__) 
                
        data += '\n'
        
    # Write to file
    outfile = 'frbroo_101_out.txt'
    file_handle = open(outfile, 'w')
    file_handle.write(data)
    file_handle.close()
    
if __name__ == '__main__':
    #list_property_names(crm.E1())
    test()
    
    