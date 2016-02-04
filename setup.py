

import os
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


def read(filename):
    '''
    Reads a text file
    '''
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name="profiterole",
    version=profiterole.__version__,
    author="Federico Ressi",
    author_email="federico.ressi@gmail.com",
    description=(
        "Automate and standardize testing using a provisioned environment."),

    license='Apache License 2.0',
    keywords="strategy game",
    url=profiterole.URL,
    download_url=profiterole.URL + "/archive/master.zip",

    # package content
    packages=find_packages(),

    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Games",
        "License :: OSI Approved :: GPL3 License",
    ],
    platforms=["Linux", "Mac OS-X"],

    # TOX integration
    tests_require=['tox'],
    cmdclass={'test': Tox})
