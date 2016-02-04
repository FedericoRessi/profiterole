import mock
import pytest

from profiterole import command

from test_init import version  # flake8: noqa


@pytest.fixture
def mocked_sys():
    mocked = mock.patch.object(command, 'sys')
    return mocked.start()


def test_main_without_argv_and_success(version, mocked_sys):
    mocked_sys.argv = ['profit', '--version']

    result = command.main()

    assert 0 == result
    mocked_sys.stdout.write.assert_called_once_with(version + '\n')


def test_main_with_argv_and_success(version, mocked_sys):

    result = command.main(['profit', '--version'])

    assert 0 == result
    mocked_sys.stdout.write.assert_called_once_with(version + '\n')


def test_main_with_no_args(mocked_sys):

    result = command.main([])

    assert 1 == result
    mocked_sys.stdout.write.assert_called_once_with('Invalid command: \n')


def test_get_sources(mocked_sys):

    result = command.main(['profit', 'get-sources'])

    assert 0 == result
    assert False == mocked_sys.stdout.write.called
