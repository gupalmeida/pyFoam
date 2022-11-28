from setuptools import setup,find_packages

setup(
    name='pyFoamTools',
    version='0.0.1',
    description='Package to use for pre and post-processing OpenFOAM cases.',
    author='Gustavo Pires Villela de Almeida',
    author_email='comp.cfd@gmail.com',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.7"',
        'numpy',
        'pandas',
        'pyyaml'
    ],
    packages = find_packages(exclude=["templates","tests"])
)