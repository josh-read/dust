from setuptools import setup, find_packages

from Cython.Build import cythonize

setup(
    name='Dust',
    description="Particle dynamics simulation/visualisation built on Pygame.",
    author='Joshua Read, Benjamin Read',
    packages=find_packages(),
    ext_modules=cythonize("dust/vector.pyx")
    )
