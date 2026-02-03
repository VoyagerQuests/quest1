# tests/test_cli.py
from pathlib import Path

import pytest

import cli
from repository import CharacterRepositoryJsonFile


@pytest.fixture
def cli_instance(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> cli.CharacterCLI:
    repo = CharacterRepositoryJsonFile(file_path=tmp_path / "characters.json")

    def _repo_factory(*_args, **_kwargs):
        return repo

    monkeypatch.setattr(cli, "CharacterRepositoryJsonFile", _repo_factory)
    return cli.CharacterCLI()


def test_cli_create_and_get(cli_instance: cli.CharacterCLI) -> None:
    created = cli_instance.create(
        name="Some Character",
        might=10,
        agility=20,
        vitality=30,
        insight=40,
        arcana=50,
        presence=60,
    )
    assert created["id"].startswith("char_")
    assert created["name"] == "Some Character"

    all_chars = cli_instance.get()
    assert len(all_chars) == 1
    assert all_chars[0]["id"] == created["id"]

    one = cli_instance.get(character_id=created["id"])
    assert len(one) == 1
    assert one[0]["id"] == created["id"]


def test_cli_update_attributes(cli_instance: cli.CharacterCLI) -> None:
    created = cli_instance.create(
        name="Another Character",
        might=1,
        agility=2,
        vitality=3,
        insight=4,
        arcana=5,
        presence=6,
    )

    updated = cli_instance.update_attributes(
        character_id=created["id"],
        might=11,
        agility=22,
        vitality=33,
        insight=44,
        arcana=55,
        presence=66,
    )
    assert updated["id"] == created["id"]
    assert updated["attributes"]["presence"] == 66


def test_normalize_attributes_rejects_unknown() -> None:
    with pytest.raises(ValueError, match="Unknown attribute"):
        cli._normalize_attributes({"power": 10})
