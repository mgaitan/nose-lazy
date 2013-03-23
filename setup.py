import sys
from setuptools import setup, find_packages


extra_setup = {}
if sys.version_info >= (3,):
    extra_setup['use_2to3'] = True

setup(
    name='nose-lazy',
    version='0.1',
    description='Nose plugin to run only needed tests based on the CVS diff',
    long_description=open('README.rst').read(),
    author='Martín Gaitán',
    author_email='gaitan@gmail.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['nose>=1.2.1'],
    test_suite='nose.collector',
    url='https://github.com/mgaitan/nose-lazy',
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        noselazy = noselazy:LazyPlugin
        """,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
        ],
    **extra_setup
)
