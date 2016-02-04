'''
Test profiterole main package.
@author: Federico Ressi
'''

from pytest import fixture  # pylint: disable=no-name-in-module


@fixture
def module():
    '''
    Profiterole package module
    '''

    import profiterole
    return profiterole


def test_version_format(module):
    'Package version has following format: A.B.C'

    version = module.__version__.split('.')
    assert len(version) == 3
    for num in version:
        assert int(num) >= 0
