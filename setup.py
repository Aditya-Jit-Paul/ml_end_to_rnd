from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List:
    requirements = []
    HYPEN_E_DOT = "-e ."
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n" , "") for r in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
setup(
    name='ml_end_to_end',
    version='0.0.1',
    author='Aditya Jit Paul',
    author_email='padityajit@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)