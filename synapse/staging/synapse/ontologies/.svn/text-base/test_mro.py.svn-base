from LAM import cidoc_crm_502 as crm

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
    crm_class_list = [
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
    
    data = ''

    for class_ in crm_class_list:
        exec "e%s = crm.E%s()" % (class_, class_)
        exec "superclasses = crm.E%s.__mro__" % class_
        for i in range(len(superclasses)):
            if superclasses[i].__name__ != 'object':
                
                if i == 0:
                    # Class name & underline
                    data += superclasses[i].__doc__ + '\n'
                    data += len(superclasses[i].__doc__) * '=' + '\n\n'
                
                if i == 0:
                    # Header & underline for declard properties
                    data += "    Properties declared for '%s':\n" % (superclasses[i].__doc__)
                    data += "    " + (26 * '-') + len(superclasses[i].__doc__) * '-' + '\n'
                else:
                    # Header & underline for inherited properties
                    data += "    Properties inherited from '%s':\n" % (superclasses[i].__doc__)
                    data += "    " + (29 * '-') + len(superclasses[i].__doc__) * '-' + '\n'
                
                # Call method to create fproperty listing for class
                exec "data += list_fproperty_names(crm.%s(), i)" % (superclasses[i].__name__)
                
                # Call method to create rproperty listing for class
                exec "data += list_rproperty_names(crm.%s(), i)" % (superclasses[i].__name__)
                
        data += '\n'
        
    # Write to file
    #outfile = 'frbroo_101_out.txt'
    outfile = 'crm_502_out.txt'
    file_handle = open(outfile, 'w')
    file_handle.write(data)
    file_handle.close()
    
if __name__ == '__main__':
    #list_property_names(crm.E1())
    test()
    
    