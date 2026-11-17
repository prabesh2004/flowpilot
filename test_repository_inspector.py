import pytest

from repository_inspector import parse_repository_id


def test_parse_repository_id_returns_owner_and_repo():
    result = parse_repository_id("octocat/Hello-World")
    assert result == ("octocat", "Hello-World")


def test_parse_repository_id_strips_surrounding_whitespace():
    result = parse_repository_id("  octocat/Hello-World  ")
    assert result == ("octocat", "Hello-World")


@pytest.mark.parametrize(
    "invalid_id",
    [
        "",
        "Hello-World",
        "/Hello-World",
        "octocat/",
        "one/two/three",
    ],
)
def test_parse_repository_id_rejects_invalid_identifiers(invalid_id):
    with pytest.raises(ValueError):
        parse_repository_id(invalid_id)
