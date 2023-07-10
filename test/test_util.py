from unittest import mock
from unittest.mock import patch

import pytest

from hooks.util import cmd_output, CalledProcessError


def test_cmd_output_sys_error():
    with patch("hooks.util.Popen.communicate") as pro:
        pro.return_value =(None, "error")
        with pytest.raises(CalledProcessError):
            cmd_output("git", retcode=1)


def test_cmd_output_sys():
    with patch("hooks.util.Popen.communicate") as pro:
        pro.return_value =("output", None)
        assert "output" == cmd_output("git",retcode=None)



