from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='package',
      version='1.0.0',
      description='Challenge-1 Script',
      long_description=readme(),
      long_description_content_type='text/markdown',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'challenge-1 = package.main:main',
        ],
      },
)