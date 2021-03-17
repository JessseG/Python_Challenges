from setuptools import setup
from setuptools import find_packages

setup(name='package',
      version='1.0.0',
      description='Challenge-4 Script',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'challenge-4 = package.main:main',
        ],
      },
)