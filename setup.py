from importlib.resources import Package
from lib2to3.pgen2.token import NAME
from setuptools import setup
from typing import List
import re


#declaring variables for setup function
PROJECT_NAME = 'housing predictor'
VERSION = '0.0.1'
AUTHOR = 'Kasun Tharaka'
DESCRIPTION = 'this is a testing house pricing project'
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'


def get_requirements_list()->List[str]:
    """
    Description: This functio is going to return requirement 
    mentioned requirement.txt file
    
    returns this functio is going to return list which will content name 
    of libraries mentioned in requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirment_file:
        
        # my_str = requirment_file.read()
        # m = re.findall(r'\w', my_str)
        # return m
        
        m = requirment_file.readlines()
        return m


setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    package = PACKAGES,
    install_requires = get_requirements_list()
)
