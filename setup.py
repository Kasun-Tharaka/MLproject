
"""
from importlib.resources import Package
from lib2to3.pgen2.token import NAME
from setuptools import setup, find_packages
from typing import List
import re


#declaring variables for setup function
PROJECT_NAME = 'housing predictor'
VERSION = '0.0.3'
AUTHOR = 'Kasun Tharaka'
DESCRIPTION = 'this is a testing house pricing project'
PACKAGES = find_packages()
REQUIREMENT_FILE_NAME = 'requirements.txt'



def get_requirements_list()->List[str]:
   
    # Description: This functio is going to return requirement 
    # mentioned requirement.txt file
    
    # returns this functio is going to return list which will content name 
    # of libraries mentioned in requirement.txt file
  
    with open(REQUIREMENT_FILE_NAME) as requirment_file:
        return requirment_file.readlines().remove('-e .')


setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    package = PACKAGES,
    install_requires = get_requirements_list()
)
"""

"""
why -e remove, 
    -e and find_packages are doing same job. 
    -e job is describ in requirement.txt file.
    find_package() will find all of libraries inside our project and then install.
    so now we have find_package() function, so we don't need -e, then you can remove it dinamically
"""


""""
 this seetup.py is works well on Linux, in Windows some kind of issure, 
 so in terminal pip install -r requirement.txt
 """


"""
 why we are using setup.py file, when we need to deploy 
 this project as a library then we use this file.
 """

