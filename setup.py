from setuptools import setup, find_packages

setup(
    name='cbapi',
    packages=['cbapi'],
    url='https://github.com/keesters/baruch-mfe-python-summer/tree/master/cbapi',
    description='CrunchBase API for pulling people and organization data',
    long_description=open('README.md').read(),
    install_requires=['json','requests','pandas'],
    # dependency_links = ['https://github.com/keesters/baruch-mfe-python-summer/tree/master/cbapi'],
    include_package_data=True,
)
