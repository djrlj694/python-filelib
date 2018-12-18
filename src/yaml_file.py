#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
yaml_file.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
YAML(subpath1[, subpath2, ..., dir=dir])

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The class "YAML", a subclass of "File":
* Encapulates YAML file metadata;
* Handles YAML file operations.

EXAMPLES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
from yaml_file import YAML

yaml1 = YAML('test1')
yaml1_dict = yaml.load()
print(yaml1_dict["SectionA"]
print(yaml1_dict["SectionA"]["rowA1"]
print(yaml1_dict["SectionA"]["rowA2"]
print(yaml1_dict["SectionB"]
print(yaml1_dict["SectionB"]["rowB1"]
print(yaml1_dict["SectionB"]["rowB2"]

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://www.geeksforgeeks.org/python-docstrings/
2. https://github.com/bc-python/mistool/blob/master/mistool/os_use.py
3. https://pythonhosted.org/six/
4. https://pyyaml.org/wiki/PyYAMLDocumentation
5. http://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
6. https://stackoverflow.com/questions/18090672/convert-dictionary-entries-into-variables-python
'''

__author__ = 'Robert (Bob) L. Jones'
__coauthor__ = 'N/A'
__copyright__ = 'Copyright 2018, YAML'
__credits__ = ['Robert (Bob) L. Jones']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Robert (Bob) L. Jones'
__status__ = 'Development'
__created_date__= 'Dec 17, 2018'
__modified_date__= 'Dec 17, 2018'


#ARGUMENTS:
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    
#The "__init__" method of the class "YAML" accepts 2 arguments:
#
#Required:
#1. name: The file's name (with or without the log file's extension)
#
#Optional:
#2. dir: The path (absolute or relative) of the log file's parent directory 
#
#Log level is defaulted to INFO. 
#
#Please use logger.setLevel(<lvlname>) to override the default in your script.



### Libraries ###

# 3rd-party

import yaml

# Custom

from file import File


### Class Declaration ###

class YAML(File):
    '''
    The class "YAML", a subclass of "File":
        * Encapulates YAML file metadata;
        * Handles YAML file operations.
    
    Attributes:
        All attributes are inherited from the parent class "File".
    '''

    def __new__(cls, *args, **kwargs):
    
        '''
        The constructor for the class "YAML" that exists solely for creating the object.
        
        Parameters:
            args (list): A comma-separated list of arguments representing parts of path.
            kwargs (dict): An optional comma-separated list of key/value pairs.
        
        Returns:
            YAML: An uninitialized "YAML" class instance.
        '''

        extension = kwargs.get('extension', '.yaml') # The file's extension (e.g., ".yaml")
        dir = kwargs.get('dir', '')                  # The path (absolute or relative) of the file's parent directory

        return super(YAML, cls).__new__(cls, *args, extension=extension, dir=dir)


    def load(self):
        '''
        Returns a string representing the YAML file's content.
        
        Parameters:
            N/A
            
        Returns:
            str: The YAML file's content.
        '''
        
        dict = yaml.load(open(str(self), 'r'))
        
        return dict


### Main ###

if __name__ == "__main__":
    #pass
    
    from argparse import Namespace
    
    print(__doc__)
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    yaml1 = YAML('test1', dir='../etc')
    print("yaml1 = YAML('test1', dir='../etc')")
    print("TEST 1a: yaml1.name=%s" % yaml1.name)
    print("TEST 1b: yaml1.stem=%s" % yaml1.stem)
    print("TEST 1c: yaml1.parent=%s" % yaml1.parent)
    print("TEST 1d: yaml1.suffix=%s" % yaml1.suffix)
    print("TEST 1e: yaml1=%s" % yaml1)
    print("")

    yaml1_dict = yaml1.load()
    
    # PASS
    #print(yaml1_dict["SectionA"])
    #print(yaml1_dict["SectionA"]["rowA1"])
    #print(yaml1_dict["SectionA"]["rowA2"])
    #print(yaml1_dict["SectionB"])
    #print(yaml1_dict["SectionB"]["rowB1"])
    #print(yaml1_dict["SectionB"]["rowB2"])
    
    print(yaml1_dict)
    
    print(yaml1_dict["SectionA"])
    print(Namespace(**yaml1_dict).SectionA)
    
    print(yaml1_dict["SectionA"]["rowA1"])
    print(Namespace(**(Namespace(**yaml1_dict).SectionA)).rowA1)
    
    #print(yaml1_dict.SectionA)
    #print(yaml1_dict)
    #print(yaml1_dict.SectionA["rowA1"])
    #print(yaml1_dict.SectionA.rowA2)
    #print(yaml1_dict.SectionB)
    #print(yaml1_dict.SectionB.rowB1)
    #print(yaml1_dict.SectionB.rowB2)
