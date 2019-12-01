#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
file.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
File(subpath1[, subpath2, ..., extension=extension, dir=dir])

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The class "File", a subclass of "Path":
* Encapulates file metadata;
* Handles file operations.

EXAMPLES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
from file import File

file1 = File('file1.csv', dir='~')
print('TEST 1a: file1.name = %s' % file1.name)
print('TEST 1b: file1.stem = %s' % file1.stem)
print('TEST 1c: file1.parent = %s' % file1.parent)
print('TEST 1d: file1.suffix = %s' % file1.suffix)
print('TEST 1e: file1 = %s' % file1)

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://codereview.stackexchange.com/questions/162426/subclassing-pathlib-path
2. https://cpython-test-docs.readthedocs.io/en/latest/library/pathlib.html
3. https://www.geeksforgeeks.org/python-docstrings/
4. https://github.com/bc-python/mistool/blob/master/mistool/os_use.py
5. https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf
6. https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
7. https://pythonhosted.org/six/
8. https://realpython.com/python-pathlib/
9. https://spyhce.com/blog/understanding-new-and-init
10. http://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
11. https://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass
12. https://stackoverflow.com/questions/21639788/difference-between-super-and-calling-superclass-directly
13. https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
'''

__version__ = '0.0.0'

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__copyright__ = 'Copyright 2019, File'
__license__ = 'MIT'

__created_date__= 'Dec 17, 2018'
__modified_date__= 'Dec 01, 2019'

### Libraries ###

# 3rd-party

import argparse
import re
import sys

#from pathlib import Path, _windows_flavour, _posix_flavour
from pathlib import Path

# Custom


### Class Declaration ###

class File(type(Path())):
    '''
    The class "File", a subclass of "Path":
        * Encapulates file metadata;
        * Handles file operations.
    
    Attributes:
        All attributes are inherited from the parent class "Path".
    '''

    def __new__(cls, *args, **kwargs):
        
        '''
        The constructor for the class "File" that exists solely for creating the object.
        
        Parameters:
            args (list): A comma-separated list of arguments representing parts of path.
            kwargs (dict): An optional comma-separated list of key/value pairs.
        
        Returns:
            File: An uninitialized "File" class instance.
        '''

        extension = kwargs.get('extension', '') # The file's extension (e.g., ".csv")
        dir = kwargs.get('dir', '')             # The path (absolute or relative) of the file's parent directory

        name = args[-1]
        name_part = name.split('/')[-1] or name.split('\\')[-1]
        name_stem = name_part.split('.')[0]
        name_extension = name_part[len(name_stem):]
        new_name = name if name_extension.endswith(extension) else name + extension
        #print('File(): new_name = %s, name = %s, extension = %s, name_extension = %s' % (new_name, name, extension, name_extension))
        
        return super(File, cls).__new__(cls, dir, new_name, **kwargs)


### Function Declarations ###

def main():
    
    ### Read command-line input.
    
    # If no command-line arguments are specified, conduct unit test.
    if len(sys.argv) == 1:
        test()
    
    # Otherwise, proceed as normal.
    else:
    
        # Process command-line input.
        parser = cli_parser()
        args = parser.parse_args()
   
        # Instantiate File object.
        file_obj = File(args.file) # Added. 15OCT2018, RLJ
        ###file.pattern = args.pattern # PASS
    
        # Print selected property value.
        if args.extension:
            print(file_obj.suffix)
        elif args.name:
            print(file_obj.name)
        #elif args.regexp:
        #    print(file_obj.regexp)
        elif args.stem:
            print(file_obj.stem)
        else:
            print(file_obj)

def test():
    
    print(__doc__)
    print('UNIT TESTS: PASS')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    file1 = File('file1.csv', dir='~')
    print("file1 = File('file1.csv', dir='~')")
    print('TEST 1a: file1.name = %s' % file1.name)
    print('TEST 1b: file1.stem = %s' % file1.stem)
    print('TEST 1c: file1.parent = %s' % file1.parent)
    print('TEST 1d: file1.suffix = %s' % file1.suffix)
    print('TEST 1e: file1 = %s' % file1)
    print('')
    
    file2 = File('file2', extension='.csv', dir='.')
    print("file2 = File('file2', extension='.csv', dir='.')")
    print('TEST 2a: file2.name = %s' % file2.name)
    print('TEST 2b: file2.stem = %s' % file2.stem)
    print('TEST 2c: file2.parent = %s' % file2.parent)
    print('TEST 2d: file2.suffix = %s' % file2.suffix)
    print('TEST 2e: file2 = %s' % file2)
    print('')
    
    file3 = File('file3', extension='.json.jinja', dir='.')
    print("file3 = File('file3', extension='.json.jinja', dir='.')")
    print('TEST 3a: file3.name= %s' % file3.name)
    print('TEST 3b: file3.stem= %s' % file3.stem)
    print('TEST 3c: file3.parent= %s' % file3.parent)
    print('TEST 3d: file3.suffix= %s' % file3.suffix)
    print('TEST 3e: file3= %s' % file3)
    print('')
    
    file4 = File('file4.json.jinja', extension='.json.jinja', dir='.')
    print("file4 = File('file4.json.jinja', extension='.json.jinja', dir='.')")
    print('TEST 4a: file4.name= %s' % file4.name)
    print('TEST 4b: file4.stem= %s' % file4.stem)
    print('TEST 4c: file4.parent= %s' % file4.parent)
    print('TEST 4d: file4.suffix= %s' % file4.suffix)
    print('TEST 4e: file4= %s' % file4)
    print('')
    
    file5 = File('../etc/file5.json.jinja', extension='.json.jinja', dir='.')
    print("file5 = File('../etc/file5.json.jinja', extension='.json.jinja', dir='.')")
    print('TEST 5a: file5.name= %s' % file5.name)
    print('TEST 5b: file5.stem= %s' % file5.stem)
    print('TEST 5c: file5.parent= %s' % file5.parent)
    print('TEST 5d: file5.suffix= %s' % file5.suffix)
    print('TEST 5e: file5= %s' % file5)
    print('')
    
    file6 = File('../etc/file6.json.jinja', dir='.')
    print("file6 = File('../etc/file6.json.jinja', dir='.')")
    print('TEST 6a: file6.name= %s' % file6.name)
    print('TEST 6b: file6.stem= %s' % file6.stem)
    print('TEST 6c: file6.parent= %s' % file6.parent)
    print('TEST 6d: file6.suffix= %s' % file6.suffix)
    print('TEST 6e: file6= %s' % file6)
    print('')
    
    file7a = File('../etc/file7.json', dir='.')
    file7b = File(file7a.name, extension='.jinja', dir=file7a.parent)
    print("file7a = File('../etc/file7.json', dir='.')")
    print("file7b = File(file7a.name, extension='.jinja', dir=file7a.parent)")
    print('TEST 7a: file7b.name= %s' % file7b.name)
    print('TEST 7b: file7b.stem= %s' % file7b.stem)
    print('TEST 7c: file7b.parent= %s' % file7b.parent)
    print('TEST 7d: file7b.suffix= %s' % file7b.suffix)
    print('TEST 7e: file7b= %s' % file7b)
    print('')

    file8 = File('file8.json.jinja', extension='.jinja', dir='.')
    print("file8 = File('file8.json.jinja', extension='.jinja', dir='.')")
    print('TEST 8a: file8.name = %s' % file8.name)
    print('TEST 8b: file8.stem = %s' % file8.stem)
    print('TEST 8c: file8.parent = %s' % file8.parent)
    print('TEST 8d: file8.suffix = %s' % file8.suffix)
    print('TEST 8e: file8 = %s' % file8)
    print('')

def cli_parser():
    
    ### Define command-line interface (CLI) and how to parse it.
    
    parser = argparse.ArgumentParser(description='This is a demo script by RLJ.')
    
    # Required arguments (except for unit testing)
    parser.add_argument('-F', '--file', help='File.', required=True)
    
    # Optional arguments (without values)
    parser.add_argument('-e', '--extension', action='store_true', help='File extension/suffix.', required=False)
    parser.add_argument('-n', '--name', action='store_true', help='File name.', required=False)
    parser.add_argument('-r', '--regexp', action='store_true', help='Regular expression pattern.', required=False)
    parser.add_argument('-s', '--stem', action='store_true', help='File stem.', required=False)
    
    return parser
    

### Main ###

if __name__ == '__main__':
    #pass
    
    main()
