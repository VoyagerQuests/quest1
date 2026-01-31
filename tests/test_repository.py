# tests/test_repository.py
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from domain import Character
from repository import CharacterRepositoryJsonFile


def make_character(
    *,
    id_: str = "char_ABCDEFGHIJKL",  # "char_" + 12 chars
    name: str = "Some Character",    # >= 10 chars
    health: int = 80,
    might: int = 10,
    agility: int = 20,
    vitality: int = 30,
    insight: int = 40,
    arcana: int = 50,
    presence: int = 60,
) -> Character:
    return Character.model_validate(
        {
            "id": id_,
            "name": name,
            "health": health,
            "attributes": {
                "might": might,
                "agility": agility,
                "vitality": vitality,
                "insight": insight,
                "arcana": arcana,
                "presence": presence,
            },
        }
    )


@pytest.fixture
def repo(tmp_path: Path) -> CharacterRepositoryJsonFile:
    return CharacterRepositoryJsonFile(file_path=tmp_path / "characters.json")


def test_list_all_empty_when_file_missing(repo: CharacterRepositoryJsonFile):
    assert repo.list_all() == []


def test_add_then_list_all_reads_back(repo: CharacterRepositoryJsonFile):
    c = make_character()
    repo.add(c)

    chars = repo.list_all()
    assert len(chars) == 1
    assert chars[0].id == c.id
    assert chars[0].name == c.name
    assert chars[0].health == c.health
    assert chars[0].attributes.might == c.attributes.might


def test_get_by_id(repo: CharacterRepositoryJsonFile):
    c1 = make_character(id_="char_ABCDEFGHIJKL", name="Character One")
    c2 = make_character(id_="char_MNOPQRSTUVWX", name="Character Two")
    repo.add(c1)
    repo.add(c2)

    found = repo.get_by_id(c2.id)
    assert found is not None
    assert found.id == c2.id
    assert found.name == c2.name

    assert repo.get_by_id("char_YYYYYYYYYYYY") is None  # type: ignore[arg-type]


def test_update_changes_existing_character(repo: CharacterRepositoryJsonFile):
    c = make_character(name="Original Name")
    repo.add(c)

    updated = c.model_copy(update={"name": "Updated Name"})
    repo.update(updated)

    found = repo.get_by_id(c.id)
    assert found is not None
    assert found.name == "Updated Name"


def test_delete_removes_character(repo: CharacterRepositoryJsonFile):
    c1 = make_character(id_="char_ABCDEFGHIJKL", name="Character One")
    c2 = make_character(id_="char_MNOPQRSTUVWX", name="Character Two")
    repo.add(c1)
    repo.add(c2)

    repo.delete(c1.id)

    remaining = repo.list_all()
    assert len(remaining) == 1
    assert remaining[0].id == c2.id
    assert repo.get_by_id(c1.id) is None


def test_read_raw_not_a_list_raises_value_error(tmp_path: Path):
    # Repository should raise ValueError if JSON root isn't a list
    file_path = tmp_path / "characters.json"
    file_path.write_text(json.dumps({"not": "a list"}), encoding="utf-8")

    repo = CharacterRepositoryJsonFile(file_path=file_path)
    with pytest.raises(ValueError, match="must contain a JSON array"):
        repo.list_all()


def test_invalid_item_in_file_raises_value_error_if_repo_validates(tmp_path: Path):
    """
    This test assumes your repository validates file items using a Pydantic schema
    (e.g., CharacterSchema via TypeAdapter) and wraps ValidationError as ValueError.

    If your current repository does NOT validate on read, delete this test.
    """
    file_path = tmp_path / "characters.json"

    # Invalid because:
    # - id doesn't match pattern ^char_.{12}$
    # - name too short
    # - missing health
    # - attributes missing required fields
    file_path.write_text(
        json.dumps(
            [
                {
                    "id": "bad",
                    "name": "short",
                    "attributes": {"might": 1},
                }
            ]
        ),
        encoding="utf-8",
    )

    repo = CharacterRepositoryJsonFile(file_path=file_path)
    with pytest.raises(ValueError):
        repo.list_all()
