from unittest.mock import patch

import pytest

from hooks import branch_name


@pytest.mark.parametrize(
    "name", [
        ("feature/RSS-13-novo-campo"),
        ("task/RSS-13-novo-campo"),
        ("hotfix/RSS-13-corrigir-campo"),
        ("bugfix/RSS-13-corrigir-campo"),
        ("test/nome-do test"),
        ("release/v1.0.1"),
        ("main"),
        ("developer")
    ],
)
def test_valid_branch_name(name: str):
    assert branch_name.is_valid_branch_name(name) == True


@pytest.mark.parametrize(
    "name", [
        ("RSS-13-novo-campo"),
        ("task/"),
        ("hotfix/RSS"),
        ("bugfix/RSS-corrigir-campo"),
        ("test-nome-do test"),
        ("")
    ],
)
def test_invalid_branch_name(name: str):
    assert branch_name.is_valid_branch_name(name) == False


@pytest.mark.parametrize(
    "name", [
        ("refs/heads/feature/RSS-13-novo-campo"),
        ("refs/heads/task/RSS-13-novo-campo"),
        ("refs/heads/hotfix/RSS-13-corrigir-campo"),
        ("refs/heads/bugfix/RSS-13-corrigir-campo"),
        ("refs/heads/test/nome-do test"),
        ("refs/heads/release/v1.0.1")
    ],
)
def test_get_branch_name_env(name: str):
    with patch("hooks.branch_name.getenv") as cmd_output:
        cmd_output.return_value = name
        cmd_output.call_args = "PRE_COMMIT_REMOTE_BRANCH"
        assert name.split("refs/heads/")[1] == branch_name.get_branch_name()



@pytest.mark.parametrize(
    "name", [
        ("feature/RSS-13-novo-campo"),
        ("task/RSS-13-novo-campo"),
        ("hotfix/RSS-13-corrigir-campo"),
        ("bugfix/RSS-13-corrigir-campo"),
        ("test/nome-do test"),
        ("release/v1.0.1")
    ],
)
def test_get_branch_name_git(name: str):
    with patch("hooks.branch_name.getenv") as local_env:
        local_env.return_value = None
        local_env.call_args = "PRE_COMMIT_REMOTE_BRANCH"

        with patch("hooks.branch_name.cmd_output") as cmd_output:
            cmd_output.return_value = name
            cmd_output.call_args_list = ["git", "branch", "--show-current"]

            assert name == branch_name.get_branch_name()



@pytest.mark.parametrize(
    "name", [
        ("refs/heads/feature/RSS-13-novo-campo"),
        ("refs/heads/task/RSS-13-novo-campo"),
        ("refs/heads/hotfix/RSS-13-corrigir-campo"),
        ("refs/heads/bugfix/RSS-13-corrigir-campo"),
        ("refs/heads/test/nome-do test"),
        ("refs/heads/release/v1.0.1"),
        ("refs/heads/main"),
        ("refs/heads/developer")
    ],
)
def test_main(name: str):
    with patch("hooks.branch_name.getenv") as cmd_output:
        cmd_output.return_value = name
        cmd_output.call_args = "PRE_COMMIT_REMOTE_BRANCH"
        assert branch_name.main() == 0


@pytest.mark.parametrize(
    "name", [
        ("refs/heads/RSS-13-novo-campo"),
        ("refs/heads/task/"),
        ("refs/heads/hotfix/RSS"),
        ("refs/heads/bugfix/RSS-corrigir-campo"),
        ("refs/heads/test-nome-do test")
    ],
)
def test_main_error(name: str):
    with patch("hooks.branch_name.getenv") as cmd_output:
        cmd_output.return_value = name
        cmd_output.call_args = "PRE_COMMIT_REMOTE_BRANCH"
        assert branch_name.main() == 1
