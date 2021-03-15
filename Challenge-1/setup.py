from setuptools import setup
from setuptools import find_packages

setup(name='package',
      version='1.0.0',
      description='Challenge-1 Script',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'challenge-1 = package.main:main',
        ],
      },
)
