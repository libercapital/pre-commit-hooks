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


def cmd_output(*cmd: str, code: int | None = 0, **kwargs: Any) -> str:
    """
    Executa comando script
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    with Popen(cmd, **kwargs) as proc:
        stdout, stderr = proc.communicate()
        proc.wait(5000)

        if stderr is not None:
            raise CalledProcessError(cmd, code,
                                     proc.returncode,
                                     stdout, stderr)

        if code != 0 & proc.returncode != code:
            raise CalledProcessError(cmd, code,
                                     proc.returncode,
                                     stdout, stderr)

        return stdout
