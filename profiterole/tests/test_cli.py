import pytest
import sh


from test_init import version  # flake8: noqa


@pytest.fixture
def profit():
    '''
    Profiterole package module
    '''
    return sh.profit


def test_get_vesrsion(profit, version):
    'Test command line profit.'

    result = profit('--version')

    assert version + '\n' == result


def test_get_sources(profit):
    'Test command line profit.'

    result = profit('get-sources')

    assert '' == result
