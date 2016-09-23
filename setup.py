from setuptools import setup

setup(name='cryptotik',
      version='0.1',
      description='Standardized common API for several cryptocurrency exchanges.',
      url='https://github.com/peerchemist/cryptotik',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='GLP',
      packages=['cryptotik'],
      install_requires=['requests'],
      zip_safe=False)