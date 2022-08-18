from setuptools import setup

setup(
    name='pyFoam',
    version='0.0.1',
    description='Package used to manipulate OpenFOAM files',
    author='Gustavo Pires Villela de Almeida',
    author_email='comp.cfd@gmail.com',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)