from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path : str)->List[str]:
    '''
    This function returns the list of requirements mentioned in the file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements if '-e .' not in req]

    return requirements
    

setup( 
    name = 'mlproject',
    version = '0.0.1',
    author = 'Arun',
    author_email = 'arun_eshwar@yahoo.com',
    packages = find_packages() , 
    install_requires = get_requirements('requirements.txt')
)