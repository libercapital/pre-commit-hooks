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
    result = subprocess.run([
        "checkov",
        "-d",
        path
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def terraform_init(path: str) -> bool:
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "init",
        "-backend=false"
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def terraform_fmt_is_valid(path: str) -> bool:
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "fmt",
        "-diff",
        "-check"
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def terraform_validate_is_valid(path: str) -> bool:
    result = subprocess.run([
        "terraform",
        "-chdir=" + path,
        "validate"
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def tflint_init(path: str) -> bool:
    result = subprocess.run([
        "tflint",
        "--chdir=" + path,
        "--init"
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def tflint_is_valid(path: str) -> bool:
    result = subprocess.run([
        "tflint",
        "--chdir=" + path
    ], capture_output=True)
    if result.returncode == 0:
        return True

    print(result.stdout.decode("utf-8"))
    return False


def main() -> int:
    path = sys.argv[1] or "terraform"

    if not terraform_init(path):
        return 1

    if not checkov_is_valid(path):
        return 1

    if not terraform_validate_is_valid(path):
        return 1

    if not terraform_fmt_is_valid(path):
        return 1

    if not tflint_init(path):
        return 1

    if not tflint_is_valid(path):
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
