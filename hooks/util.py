"""
Utis para utilização no projeto
"""

import subprocess
from typing import Any
from subprocess import Popen


class CalledProcessError(RuntimeError):
    """
    Erro ao esxecutar script
    """


def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    """
    Executa comando script
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    with Popen(cmd, **kwargs) as proc:
        stdout, stderr = proc.communicate()
        if retcode is not None and proc.returncode != retcode:
            raise CalledProcessError(cmd, retcode,
                                     proc.returncode,
                                     stdout, stderr)
        return stdout
