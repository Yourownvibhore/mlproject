from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filename)->List[str]:
    '''return the list of requirements from requirements.txt'''

    requirements=[]
    with open(filename) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='vibhore jain',
    author_email='vjmj4005@gmail.com',packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )