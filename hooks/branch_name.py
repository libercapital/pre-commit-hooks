"""
Script para validar nome da branch.
Ver documentação em https://pre-commit.com/#intro
"""
import re
from os import getenv


BRANCH_REGEX = (r"^(((feature|task|hotfix|bug))"
                r"(\/)(.+))"
                r"|((test)(\/)(.+))"
                r"|(main|developer|release)")


def get_remot_branch_name() -> str:
    """
    Recupera nome da branch corrente
    :return: nome da branch
    """
    if getenv("PRE_COMMIT_REMOTE_BRANCH", None):
        name = getenv("PRE_COMMIT_REMOTE_BRANCH")
        if name.startswith("refs/heads/"):
            return name.split("refs/heads/")[1].strip()
        return name

    return None


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
    branch_name = get_remot_branch_name()

    if branch_name is None:
        print("Essa branch não tem uma branch remota associada")
        print("Execute o seguinte comando antes e tente novamente")
        print("")
        print("git branch -u <remote/branch name>")
        return 1

    if is_valid_branch_name(branch_name):
        return 0

    print("Erro ao ao validar branch")
    print(branch_name)
    print('Nome da branch não corresponde ao padrão.')
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
