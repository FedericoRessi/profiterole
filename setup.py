

import codecs
from os import path

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import profiterole


class Tox(TestCommand):  # pylint: disable=too-many-public-methods

    '''
    Command to be used for python setup.py test
    '''

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    tox_args = None
    test_args = None
    test_suite = False

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        tox.cmdline(args=shlex.split(self.tox_args))


def open_text_file(filename):
    '''
    Open a text file
    '''
    here = path.abspath(path.dirname(__file__))
    # Get the long description from the README file
    return codecs.open(path.join(here, filename), encoding='utf-8')


def read(filename):
    '''
    Reads a text file.
    '''
    # Get the long description from the README file
    with open_text_file(filename) as f:
        return f.read()

def read_lines(filename):
    '''
    Reads a text file line per line.
    '''
    # Get the long description from the README file
    with open_text_file(filename) as f:
        return [l.strip() for l in f if l.strip()]

setup(
    name="profiterole",

    version=profiterole.__version__,

    description=
        "Automate and standardize testing using a provisioned environment.",
    long_description=read('README.md'),

    url=profiterole.URL,

    author="Federico Ressi",
    author_email="federico.ressi@gmail.com",

    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],

    keywords="testing automation provisioning",

    # package content
    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=read('requirements.txt'),

    download_url=profiterole.URL + "/archive/master.zip",

    platforms=["Linux", "Mac OS-X"],

    # TOX integration
    tests_require=['tox'],
    cmdclass={'test': Tox},

    # generate profit script
    entry_points={
        'console_scripts': [
            'profit=profiterole.command:main']})
