"""
Script para validar nome da branch.
Ver documentação em https://pre-commit.com/#intro
"""
import re
from os import getenv

from hooks.util import cmd_output

BRANCH_REGEX = r"^(((feature|task|hotfix|bugfix))" \
               r"(\/)([A-Z]{2,}-[0-9]+))|((test)(\/)(.+))|" \
               r"(main|developer)|(release|test)(\/).+"


def get_branch_name() -> str:
    """
    Recupera nome da branch corrente
    :return: nome da branch
    """
    if getenv("PRE_COMMIT_REMOTE_BRANCH", None):
        name = getenv("PRE_COMMIT_REMOTE_BRANCH")
        return name.split("refs/heads/")[1].strip()

    return cmd_output("git", "branch", "--show-current")


def is_valid_branch_name(name: str) -> bool:
    """
    Valida nome se o nome da branch é válida
    :param name: nome da branch
    :return: True ou False
    """
    if re.match(BRANCH_REGEX, name):
        return True
    return False


def main() -> int:
    """

    :param:
    :return: 0 - executado com successo | 1- erro ao executar
    """
    branch_name = get_branch_name()
    if is_valid_branch_name(branch_name):
        return 0
    print("Erro ao ao validar branch")
    print(branch_name)
    print('Nome da branch não corresponde ao padrão.')
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
