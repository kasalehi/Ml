#the reason for setup.py is we want to create whole application 
from setuptools import setup,find_packages
from typing import  List

HYPHEN_E_DOT='-e .'

def get_file(file_path:str)->list[str]:
    requirements=[]
    with open (file_path,encoding='utf-8') as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='1.0',
    author='keyvan',
    author_email='ksalehi56@yahoo.com',
    install_requires=get_file('requirements.txt') 
)

