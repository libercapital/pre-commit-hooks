"""
Script para validar os resources do terraform
- terraform init
- checkov
- terraform validate
- terraform fmt
- tflint
"""
from __future__ import annotations

import subprocess
import sys


def checkov_is_valid(path: str) -> bool:
    """Executa checkov para validar os resources do terraform"""

    print("Validando os resources do terraform com checkov")
    result = subprocess.run([
        "checkov",
        "-d",
        path
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def terraform_init(path: str) -> bool:
    """Executa terraform init para inicializar o projeto"""

    print("Inicializando terraform init")
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "init",
        "-backend=false"
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def terraform_fmt_is_valid(path: str) -> bool:
    """Executa terraform fmt para validar o formato dos arquivos"""

    print("Validando formatação dos conteúdos")
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "fmt",
        "-diff",
        "-check"
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def terraform_validate_is_valid(path: str) -> bool:
    """Executa terraform validate para validar os arquivos"""

    print("Validando estrutura do terraform")
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "validate"
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def tflint_init(path: str) -> bool:
    """Executa tflint init para inicializar o projeto"""

    print("Inicializando tflint")
    result = subprocess.run([
        "tflint",
        "--chdir=" + path,
        "--init"
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def tflint_is_valid(path: str) -> bool:
    """Executa tflint para validar os arquivos"""

    print("Validando conteúdo com tflint")
    result = subprocess.run([
        "tflint",
        "--chdir=" + path
    ], capture_output=True, check=False)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    sys.exit(1)


def main() -> int:
    """Executa os comandos para validar os resources do terraform"""

    path = "terraform"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    print("Terraform Lint")
    print("path: " + path)

    terraform_init(path)
    checkov_is_valid(path)
    terraform_validate_is_valid(path)
    terraform_fmt_is_valid(path)
    tflint_init(path)
    tflint_is_valid(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
