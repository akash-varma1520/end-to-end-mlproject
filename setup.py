from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    

name = 'end to end ml project',
version = '0.0.1',
author = 'Akash Varma',
author_email = 'akashvarma1520@gmail.com',
packages = get_requirements('requirements.txt'),
install_requires = ['numpy','pandas','seaborn'],
include_package_data=True,
zip_safe=False,

)