#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
jinja_file.py

DECLARATION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
JINJA(subpath1[, subpath2, ..., dir=dir])

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The class "JINJA", a subclass of "File":
* Encapulates YAML file metadata;
* Handles YAML file operations.

EXAMPLES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
from jinja_file import JINJA
from yaml_file import YAML

jinja1 = JINJA('test1')
yaml1 = YAML('pl_quest_onboard_part1', dir='../etc')

template1 = jinja1.load()
template1_dict = yaml1.load()

rendered1_str = template1.render(template1_dict)
print(rendered1_str)

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://www.geeksforgeeks.org/python-docstrings/
2. https://github.com/bc-python/mistool/blob/master/mistool/os_use.py
3. https://gist.github.com/wrunk/1317933/d204be62e6001ea21e99ca0a90594200ade2511e
4. http://jinja.pocoo.org/docs/2.10/api/#loaders
5. https://pythonhosted.org/six/
6. https://pyyaml.org/wiki/PyYAMLDocumentation
7. http://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
'''

__author__ = 'Robert (Bob) L. Jones'
__coauthor__ = 'N/A'
__copyright__ = 'Copyright 2018, JINJA'
__credits__ = ['Robert (Bob) L. Jones']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Robert (Bob) L. Jones'
__status__ = 'Development'
__created_date__= 'Dec 17, 2018'
__modified_date__= 'Dec 17, 2018'


### Libraries ###

# 3rd-party

import argparse
import sys

#from jinja2 import BaseLoader, Environment, FileSystemLoader, Template
from jinja2 import Environment, FileSystemLoader

# Custom

from file import File
from yaml_file import YAML


### Class Declaration ###

class JINJA(File):
	'''
	The class "JINJA", a subclass of "File":
		* Encapulates JINJA file metadata;
		* Handles JINJA file operations.
	
	Attributes:
		All attributes are inherited from the parent class "File".
	'''

	def __new__(cls, *args, **kwargs):
	
		'''
		The constructor for the class "JINJA" that exists solely for creating the object.
		
		Parameters:
			args (list): A comma-separated list of arguments representing parts of path.
			kwargs (dict): An optional comma-separated list of key/value pairs.
		
		Returns:
			JINJA: An uninitialized "YAML" class instance.
		'''

		extension = kwargs.get('extension', '.jinja') # The file's extension (e.g., ".jinja")
		dir = kwargs.get('dir', '')                   # The path (absolute or relative) of the file's parent directory

		return super(JINJA, cls).__new__(cls, *args, extension=extension, dir=dir)


	def load(self):
		'''
		Returns a string representing the JINJA file's content.
		
		Args:
			N/A
			
		Returns:
			str: The JINJA file's content.
		'''
		
		with open(str(self)) as f:
			return Environment(loader=FileSystemLoader(str(self.parent))).from_string(f.read())


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
   
		# Instantiate and load JINJA object.
		jinja_obj = JINJA(args.template) # Added. 15OCT2018, RLJ
		template = jinja_obj.load()
		
		# Instantiate and load YAML object.
		yaml_obj = YAML(args.dictionary)
		template_dict = yaml_obj.load()
		
		# Print rendered JINJA template.
		rendered_str = template.render(template_dict)
		print(str(rendered_str))

def test():
	
	print(__doc__)
	print('UNIT TESTS: PASS')
	print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
	print('')
	
	#jinja1 = JINJA('example.html', dir='templates') # PASS
	jinja1 = JINJA('test1.jil', dir='../etc') # PASS
	print("jinja1 = JINJA('test1.jil', dir='../etc')")
	print('TEST 1a: jinja1.name = %s' % jinja1.name)
	print('TEST 1b: jinja1.stem = %s' % jinja1.stem)
	print('TEST 1c: jinja1.parent = %s' % jinja1.parent)
	print('TEST 1d: jinja1.suffix = %s' % jinja1.suffix)
	print('TEST 1e: jinja1=%s' % jinja1)
	print('')
	
	template1 = jinja1.load()
	
	yaml1 = YAML('test1', dir='../etc')
	print('yaml1 = {}'.format(yaml1))
	print('')
	
	template1_dict = yaml1.load()
	print('template1_dict = {}'.format(template1_dict))
	print('')
	
	rendered1_str = template1.render(template1_dict)
	print(str(rendered1_str))
	print('')


def cli_parser():
	
	### Define command-line interface (CLI) and how to parse it.
	
	parser = argparse.ArgumentParser(description='This is a demo script by RLJ.')
	
	# Required arguments (except for unit testing)
	parser.add_argument('-D', '--dictionary', help='Dictionary.', required=True)
	parser.add_argument('-T', '--template', help='Template.', required=True)
	
	return parser


### Main ###

if __name__ == "__main__":
	#pass
	
	main()
