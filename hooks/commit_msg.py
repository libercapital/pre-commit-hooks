"""
Script para validar a mensagem escrita no commando git commit.
Ver documentação em https://pre-commit.com/#intro
"""
from __future__ import annotations

import re
import sys

COMMIT_REGEX = (r"(^Revert .+$|^Merge .+$)|"
                r"(^(feat|fix|refactor|perf|test|chore|docs"
                r"|style|build|ci|merge|revert)"
                r"\([A-Z]{2,}-[0-9]+\): .+$)")


def read_commit(commit_msg_filepath: str) -> str:
    """
    Lê a mensagem do commit
    :param commit_msg_filepath: File path
    :return: Mensagem do commit
    """
    with open(commit_msg_filepath, encoding="utf-8") as file:
        file_text = file.read()
        file.close()
        return file_text


def white_commit(text: str, commit_msg_filepath: str):
    """
    Reescreve a mensagem do commit
    :param text: Texto que irá substituir a mensagem original
    :param commit_msg_filepath: File path
    """
    with open(commit_msg_filepath, mode="w", encoding="utf-8") as file:
        file.write(text)
        file.close()


def clean_text(text: str) -> str:
    """
    Limpa o texto
    :param text: Texto
    :return: Texto limpo
    """
    return text.strip()


def is_valid_commit(msg: str) -> bool:
    """
    Valida se a mensagem do commit é valida
    :param msg: Mensagem do commit
    :return: True ou False
    """
    if re.match(COMMIT_REGEX, msg, flags=re.DOTALL):
        return True
    return False


def main() -> int:
    """

    :param:
    :return: 0 - executado com successo | 1- erro ao executar
    """

    commit_msg_filepath = sys.argv[1]
    commit_msg = read_commit(commit_msg_filepath)
    commit_msg_clean = clean_text(commit_msg)
    if is_valid_commit(commit_msg_clean):
        white_commit(commit_msg_clean, commit_msg_filepath)
        return 0
    print("Erro ao ao validar a seguinte mensagem de commit")
    print(commit_msg)
    print('Mensagem não corresponde ao padrão.')
    print('Tente utilizar a seguinte  formatação:')
    print('<code-type>(<jira-code>): Mensage do commit')
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
