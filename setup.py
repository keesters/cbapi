from setuptools import setup, find_packages

setup(
    name='cbapi',
    packages=['cbapi'],
    url='https://github.com/keesters/cbapi.git',
    description='CrunchBase API for pulling people and organization data',
    long_description=open('README.md').read(),
    install_requires=['requests','pandas'],
    include_package_data=True,
)
