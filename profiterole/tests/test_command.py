import mock
import pytest
import sh

from profiterole import command

from test_profiterole_module import version  # flake8: noqa


@pytest.fixture
def profit():
    '''
    Profiterole package module
    '''
    return sh.profit


def test_main_from_shell(profit, version):
    'Test command line profit.'

    result = profit('--version')

    assert version + '\n' == result


def test_main_with_argv_and_success(version):
    with mock.patch.object(command.sys, 'stdout') as stdout:

        result = command.main(['--version'])

        assert 0 == result
        stdout.write.assert_called_once_with(version + '\n')


def test_main_without_argv_and_success(version):
    with mock.patch.object(command.sys, 'stdout') as stdout:
        with mock.patch.object(command.sys, 'argv', ['--version']):

            result = command.main()

        assert 0 == result
        stdout.write.assert_called_once_with(version + '\n')
