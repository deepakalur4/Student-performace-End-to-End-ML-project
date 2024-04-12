from setuptools import find_packages,setup

def get_pack(file_path:str):
    '''
    This function returns the list of packages in requierements file
    '''
    with open(file_path,"r") as file_obj:
        pack=file_obj.readlines()
        pack=[i.replace("\n","") for i in pack if i not in "-e ."]
        return pack


setup(
    name="ml_project_practice",
    version="0.0.0.0",
    author="Deepak",
    author_email="Deepakalur4@gmail.com",
    packages=find_packages(),
    install_requires=get_pack("requirements.txt")

)
