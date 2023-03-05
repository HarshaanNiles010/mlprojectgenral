
from typing import List
from setuptools import find_packages, setup

def get_requirements(file_path:str)->List:
    '''
    This function returns the list of requirements
    '''
    req = [] 
    with open(file_path) as f:
        req = f.readlines()
        req = [r.replace("\n"," ") for r in req]
        
        if "-e ." in req:
            req.remove("-e .")
            
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author='Harshaan',
    author_email='harshaanniles010@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)