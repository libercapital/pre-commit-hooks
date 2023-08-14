import glob
import os
import random
import string
import sys
from unittest.mock import patch

import pytest

from hooks import commit_msg


def get_file_resources_path(file_name: str) -> str:
    data_dir = os.path.join(os.path.dirname(__file__), "resources")
    data_path = os.path.join(data_dir, file_name)
    return data_path


def test_read_commit():
    data_path = get_file_resources_path("file_with_content.txt")
    msg = commit_msg.read_commit(data_path)
    assert msg == "TEXT\n"


def test_read_commit_empty():
    data_path = get_file_resources_path("file_without_content.txt")
    msg = commit_msg.read_commit(data_path)
    assert msg == ""


def test_white_commit():
    commit_text = "".join(random.choice(string.ascii_letters) for i in range(10))
    commit_msg_filepath = get_file_resources_path("test_white_commit.txt")

    commit_msg.white_commit(commit_text, commit_msg_filepath)

    file = open(commit_msg_filepath, "r")
    file_text = file.read()
    file.close()

    assert file_text == commit_text


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (" exemplo", "exemplo"),
        (" exemplo ", "exemplo"),
        (" exemplo    ", "exemplo"),
        ("exemplo ", "exemplo"),
    ],
)
def test_clean_text(test_input: str, expected: str):
    assert commit_msg.clean_text(test_input) == expected


@pytest.mark.parametrize(
    "commit", [("feat(TEST-01): Adicionar funcionalidade de pesquisa por categoria"),
               ("fix(TEST-02): Corrigir erro de renderização no formulário de cadastro"),
               ("refactor(TEST-03): Refatorar função de validação de entrada para melhor legibilidade"),
               ("chore(TEST-04): Adicionar pasta de imagens de perfil de usuário")],
)
def test_valid_commit(commit: str):
    assert commit_msg.is_valid_commit(commit)



@pytest.mark.parametrize(
    "commit", [("(TEST-01): Adicionar funcionalidade de pesquisa por categoria"),
               ("TEST-02: Corrigir erro de renderização no formulário de cadastro"),
               ("blabla(TEST-03): Refatorar função de validação de entrada para melhor legibilidade"),
               ("testando(TEST-04): Adicionar pasta de imagens de perfil de usuário")],
)
def test_valid_commit_invalid_code_pype(commit: str):
    assert not commit_msg.is_valid_commit(commit)


@pytest.mark.parametrize(
    "commit", [("feat(TEST-01): "),
               ("fix(TEST-02):")],
)
def test_commit_without_message(commit: str):
    assert not commit_msg.is_valid_commit(commit)


@pytest.mark.parametrize(
    "file", [("correct_commit_msg-01.txt"),
             ("correct_commit_msg-02.txt"),
             ("correct_commit_msg-03.txt")
             ],
)
def test_main(file: str):
    file_path = get_file_resources_path(file)
    test_args = ["", file_path]
    with patch.object(sys, 'argv', test_args):
        assert commit_msg.main() == 0


@pytest.mark.parametrize(
    "file", [("incorrect_commit_msg-01.txt"),
             ("incorrect_commit_msg-02.txt"),
             ("incorrect_commit_msg-03.txt")
             ],
)
def test_main_error(file: str):
    file_path = get_file_resources_path(file)
    test_args = ["", file_path]
    with patch.object(sys, 'argv', test_args):
        assert not commit_msg.main() == 0
