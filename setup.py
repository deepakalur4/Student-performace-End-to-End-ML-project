from setuptools import find_packages,setup
from typing import List

def get_pack(file_path:str)-> list:
    '''
    This function returns the list of packages from requrirements file
    '''
    with open(file_path,"r") as pacakges:
        pack=pacakges.readlines()
        pack=[pac.replace("\n","") for pac in pack if pac not in "-e ."] 
        return pack


setup(
    name="Student_performace_predictor_ML_Project",
    version="0.0.0.0",
    author="Deepak S Alur",
    author_email="Deepakalur4@gmail.com",
    packages=find_packages(),
    install_requires=get_pack("requirements.txt")



)
