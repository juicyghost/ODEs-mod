from setuptools import setup, find_packages

   setup(
       name='ode_tools',
       version='0.1',
       packages=find_packages(),
       install_requires=[
           'numpy',
           'matplotlib',
           'scipy',
       ],
   )
