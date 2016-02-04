'''
Test profiterole main package.
@author: Federico Ressi
'''

import pytest


@pytest.fixture
def version():
    import profiterole
    return profiterole.__version__


def test_version_format(version):
    'Package version has following format: A.B.C'

    version_nums = [int(v) for v in version.split('.')]
    assert len(version_nums) == 3
    for num in version_nums:
        assert num >= 0
